"""Filtro de pessoa do ICP CX (campaigns/cx/icp/filtros.md).

is_pessoa_elegivel = PES-02 (gerente ou acima) E alguma área (PES-04, 05, 06, 07 ou 17).

Lê o headline INTEIRO, menos os trechos de passado ("ex-", "Formerly", "anteriormente"...).
As exclusões da triagem (fornecedor, BPO, banco, agência) são reconferidas no texto atual:
- empregador antigo não derruba ninguém ("Formerly Banco X" não é banco);
- palestrante, mentor, professor, advisor etc. só derrubam se forem o cargo principal (1º trecho);
  marca de vendor (Zendesk, Sinch...) e consultoria/agência como empresa derrubam em qualquer trecho;
- "Gestão de Fornecedores (BPO)" é quem contrata BPO, não quem é BPO.

Uso: python3 filtro_pessoa.py <entrada_triada.csv> <saida.csv> <total_engajados> [vocab.json]
vocab default: campaigns/cx/icp-vocab.json (mesmo arquivo da triagem).
"""
import csv, json, re, sys, unicodedata, collections
from pathlib import Path


def n(t): return unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
B = lambda p: re.compile(r"\b(" + p + r")\b")

SEP = re.compile(r"\s*[|·•]\s*|\s+l\s+")  # " l " aparece no lugar de "|" em alguns headlines
PASSADO = re.compile(r"^(ex[- ]|former(ly)?\b|previously\b|anteriormente\b|passagens?( por)?\b|past\b)")

PES02 = B(r"gerente|manager|head|superintendente|diretor\w*|director|vp|vice.?presiden\w*|chief|ceo|coo|cxo|cco|cmo|cdo|cio|cto|presidente|c-level"
          r"|executive|executiv[oa]|gestor[a]?")
PES03 = B(r"diretor\w*|director|vp|vice.?presiden\w*|chief|ceo|coo|cxo|cco|cmo|cdo|presidente|superintendente executiv\w*")
# executive/gestor contam como gestão, menos os cargos de vendas e operação de mídia abaixo
NAO_GESTOR = B(r"analista|assistente|estagiari\w*|project manager|product manager|account manager|community manager"
               r"|account executive|executiv[oa] de (contas|vendas)|gestor[a]? de trafego")
AREA = {
 "PES-04": B(r"cx|customer experience|experiencia d[oe]s? (cliente|consumidor)|atendimento|sac|ouvidori\w*|ombudsman|customer (care|service|relations)"
             r"|relacionamento com (o )?cliente|central de relacionamento|contact ?cent\w*|call ?cent\w*|voz do cliente|voc|voice of (the )?customer|cxo|cco|chief customer"
             r"|customer journey|jornada do cliente|gestao de clientes|servico ao cliente|pos.?venda"),
 "PES-05": B(r"marketing|mkt|social|marca|brand\w*|comunicacao|communications?|corporate affairs|insights?|conteudo|content|cmo"),
 "PES-06": B(r"martech|crm|ccaas|dados de cliente|customer data|ti de cx|cx tech\w*|canais digitais|omnichannel|omnicanal"),
 "PES-07": B(r"marketplace|seller|parceiros|partners?|e-?commerce"),
 "PES-17": B(r"operacoes de atendimento|customer operations|planejamento|wfm|workforce|qualidade|quality|monitoria"),
}
# fornecedor: estes termos descrevem atividade paralela; só derrubam quando são o cargo principal
LATERAL = B(r"consultor\w*|consultant|palestrante|speaker|keynote|mentor\w*|professor\w*|autor\w*|author|co-?autor\w*|instrutor\w*|treinador\w*|coach"
            r"|freelanc\w*|business development|account executive|executiv[oa] de contas|sdr|bdr|pre.?sales|pre.?vendas|solution delivery|solutions? architect")
CS = B(r"customer success|sucesso do cliente")
OPS = B(r"operations|operacoes|operacional")
# quem entrega projeto/serviço para clientes trabalha do lado do fornecedor
ENTREGA = B(r"professional services|service delivery|servicos profissionais")
# dono de firma própria que vive de palestra/mentoria/advisory é fornecedor, não comprador
DONO = B(r"founder|co-?founder|fundador\w*|cofundador\w*|socio\w*|owner|proprietari\w*")
SERVICO = B(r"palestr\w*|speaker|keynote|mentor\w*|advisor\w*|consultor\w*|consultoria|consulting|treinamentos?")
CONTRATA_BPO = re.compile(r"(gestao de )?fornecedores?\s*\(?\s*bpo\s*\)?|vendor management|gestao de terceiros")


def carregar_vocab(path):
    v = json.loads(Path(path).read_text(encoding="utf-8"))
    rx = lambda p: re.compile(n(p))
    return {"fornecedor": rx(v["fornecedor"]), "bpo": rx(v["bpo"]),
            "fora": {k: rx(p) for k, p in v["fora_de_lista"].items()}}


def avaliar(headline, empresa, V):
    """Devolve (elegivel, motivo_corte, dados). Só olha o headline atual + empresa (se houver)."""
    segs = [s for s in SEP.split(headline or "") if s.strip()]
    atuais = [s for s in segs if not PASSADO.match(n(s).strip())] or segs[:1]
    seg1, cur = n(atuais[0]), n(" | ".join(atuais))
    atual_emp = cur + " | " + n(empresa)

    # cargo = todo trecho atual que traz palavra de gestão (não só os 2 primeiros);
    # área tem que estar no mesmo trecho do cargo, senão é lista de competências
    titulos = [n(s) for s in atuais if PES02.search(n(s))]
    tit = " | ".join(titulos)
    p2 = bool(titulos) and not NAO_GESTOR.search(seg1)
    p3 = bool(PES03.search(tit)) and not NAO_GESTOR.search(seg1)
    areas = [k for k, rx in AREA.items() if rx.search(tit)]
    if CS.search(tit) and AREA["PES-04"].search(cur) and "PES-04" not in areas:
        areas.append("PES-04")  # gestor de CS que declara CX/atendimento no headline
    if OPS.search(tit) and (AREA["PES-04"].search(cur) or AREA["PES-17"].search(cur)) and "PES-17" not in areas:
        areas.append("PES-17")  # gestor de operações que declara customer operations/CX no headline
    if not p2: return False, "PES-02 (abaixo de gerente)", {}
    if not areas: return False, "sem área PES-04/05/06/07/17", {}

    for nome, rx in V["fora"].items():
        if rx.search(atual_emp): return False, f"empresa fora ({nome})", {}
    if V["bpo"].search(CONTRATA_BPO.sub(" ", atual_emp)): return False, "empresa fora (BPO)", {}
    if ENTREGA.search(cur):
        return False, "empresa fora (Fornecedor: entrega serviço a clientes)", {}
    if DONO.search(seg1) and SERVICO.search(cur):
        return False, "empresa fora (Fornecedor: dono que vende palestra/consultoria)", {}
    cargo_principal = bool(PES02.search(seg1)) and any(rx.search(seg1) for rx in AREA.values())
    for m in V["fornecedor"].finditer(atual_emp):
        termo = m.group(0)
        # atividade lateral só é ignorada quando o 1º trecho é um cargo de gestão na área-alvo
        if not LATERAL.fullmatch(termo) or not cargo_principal or LATERAL.search(seg1):
            return False, f"empresa fora (Fornecedor: {termo})", {}
    return True, "", {"cargo_avaliado": tit, "p3": p3, "areas": areas}


def demo(V):
    """Casos sintéticos que já deram errado. Trava regressão."""
    casos = [
        ("Gerente de Atendimento", True),
        ("Coordenadora de CX", False),
        ("Diretor de Operações e Experiência do Cliente | TEDx Speaker | Palestrante e Professor", True),  # palestra é lateral
        ("Palestrante | Ex-Diretor de CX", False),                                                       # palestra é o cargo
        ("Head de CX | Zendesk", False),                                                                 # vendor em qualquer trecho
        ("Communications Director | Advisor | Business Development", True),
        ("Gerente Gestão de Clientes", True),                                                           # sinônimo de CX
        ("Diretor Comercial & MKT l Gerente Geral", True),
        ("Gestora de Canais Digitais", True),
        ("Gestor de Tráfego | Marketing", False),
        ("CX Executive | Formerly Banco Exemplo", True),                                                # empregador antigo
        ("Gerente de CX | Banco Exemplo", False),
        ("Gerente de Operações / Gestão de Fornecedores (BPO) / Qualidade", True),                       # contrata BPO
        ("Diretor de Operações | Teleperformance", False),
        ("Diretora E-commerce | Varejo", True),
        ("Account Executive | Customer Experience", False),
        ("Founder & CEO • Palestras em Customer Experience | Executiva de CX", False),             # dono que palestra
        ("Executive Director | Strategic Marketing, Customer Experience", False),                    # área só em competências
        ("VP | Head | Director | CX | CRM", False),                                                  # lista de palavras-chave
        ("Head of Customer Success | Customer Service | Customer Experience", True),
        ("Operations Manager | Customer Operations | Customer Experience", True),                    # ops que declara CX
        ("Gerente de Operações | Logística | Supply Chain", False),
        ("Operations & Service Delivery Executive | Professional Services | Customer Operations", False),  # lado vendor
        ("Customer Success Manager | Compliance | CPA-20 | Premium CX", False),                      # banco/corretora
    ]
    erros = [(h, esp) for h, esp in casos if avaliar(h, "", V)[0] != esp]
    for h, esp in erros: print("AUTOTESTE FALHOU:", h, "esperado", esp)
    if erros: sys.exit(1)


def main():
    ENT, OUT, total_engajados = sys.argv[1], sys.argv[2], int(sys.argv[3])
    raiz = Path(__file__).resolve().parents[2]
    V = carregar_vocab(sys.argv[4] if len(sys.argv) > 4 else raiz / "campaigns/cx/icp-vocab.json")
    demo(V)
    rows = list(csv.DictReader(open(ENT, encoding="utf-8-sig")))
    keep, motivo, revertidos = [], collections.Counter(), []
    for r in rows:
        ok, corte, d = avaliar(r["headline"], r.get("empresa", ""), V)
        if not ok: motivo[corte] += 1; continue
        if r["icp"] in ("Fornecedor", "BPO") or "banco" in r["motivo"] or "agencia" in r["motivo"]:
            revertidos.append((r["nome"], r["icp"] or r["motivo"]))
        p3, areas = d["p3"], d["areas"]
        keep.append({"nome": r["nome"], "slug": r["slug"], "headline": r["headline"], "cargo_avaliado": d["cargo_avaliado"],
            "is_gerente_ou_acima": "true", "is_diretor_ou_acima": str(p3).lower(),
            **{f: str(k in areas).lower() for k, f in [("PES-04","is_area_cx"),("PES-05","is_area_marketing"),("PES-06","is_area_martech"),("PES-07","is_area_marketplace"),("PES-17","is_area_operacoes_cx")]},
            "is_decisor_economico": str(p3 and ("PES-04" in areas or "PES-05" in areas)).lower(),
            "is_champion": str((not p3) and any(a in areas for a in ("PES-04","PES-05","PES-07","PES-17"))).lower(),
            "is_influenciador_tecnico": str("PES-06" in areas).lower(),
            "is_pessoa_elegivel": "true", "icp_triagem": r["icp"], "posts_tocados": r["posts_tocados"], "influenciadores": r["influenciadores"]})
    keep.sort(key=lambda k: (k["is_decisor_economico"] != "true", -int(k["posts_tocados"] or 0)))
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(keep[0])); w.writeheader(); w.writerows(keep)
    print("triados", len(rows), "| sobraram", len(keep), f"| {len(keep)/total_engajados:.1%} de {total_engajados}", f"| {len(keep)/len(rows):.1%} de {len(rows)}")
    for k, v in motivo.most_common(): print(" ", v, k)
    print("decisor econômico", sum(k["is_decisor_economico"]=="true" for k in keep), "| champion", sum(k["is_champion"]=="true" for k in keep), "| técnico", sum(k["is_influenciador_tecnico"]=="true" for k in keep))
    print("exclusão da triagem revertida (passado, atividade lateral ou contratante de BPO):", len(revertidos))
    for nome, m in revertidos: print("  -", nome, "|", m)


if __name__ == "__main__":
    main()
