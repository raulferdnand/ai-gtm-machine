"""Filtro de pessoa do ICP CX (campaigns/cx/icp/filtros.md).

is_pessoa_elegivel = PES-02 (gerente ou acima) E alguma área (PES-04, 05, 06, 07 ou 17).
Exclui quem a triagem marcou como Fornecedor/BPO e motivos banco/agência.
Uso: python3 filtro_pessoa.py <entrada_triada.csv> <saida.csv> <total_engajados>
"""
import csv, re, sys, unicodedata, collections
ENT, OUT = sys.argv[1], sys.argv[2]
def n(t): return unicodedata.normalize("NFKD", t or "").encode("ascii","ignore").decode().lower()
B = lambda p: re.compile(r"\b(" + p + r")\b")
PES02 = B(r"gerente|manager|head|superintendente|diretor\w*|director|vp|vice.?presiden\w*|chief|ceo|coo|cxo|cco|cmo|cdo|cio|cto|presidente|c-level")
AREA = {
 "PES-04": B(r"cx|customer experience|experiencia d[oe]s? (cliente|consumidor)|atendimento|sac|ouvidori\w*|ombudsman|customer (care|service|relations)|relacionamento com (o )?cliente|central de relacionamento|contact ?cent\w*|call ?cent\w*|voz do cliente|voc|cxo|cco|chief customer"),
 "PES-05": B(r"marketing|social|marca|brand\w*|comunicacao|communications?|insights?|conteudo|content|cmo"),
 "PES-06": B(r"martech|crm|ccaas|dados de cliente|customer data|ti de cx|cx tech\w*"),
 "PES-07": B(r"marketplace|seller|parceiros|partners?"),
 "PES-17": B(r"operacoes de atendimento|customer operations|planejamento|wfm|workforce|qualidade|quality|monitoria"),
}
FORA = {"Fornecedor", "BPO"}
rows = list(csv.DictReader(open(ENT, encoding="utf-8-sig")))
total_engajados = int(sys.argv[3])
keep, motivo = [], collections.Counter()
for r in rows:
    tit = n(" | ".join(re.split(r"\s*[|·•]\s*", r["headline"])[:2]))  # cargo = 2 primeiros trechos do headline
    seg1 = n(re.split(r"\s*[|·•]\s*", r["headline"])[0])
    nao_gestor = re.search(r"\b(analista|assistente|estagiari\w*|project manager|product manager|account manager)\b", seg1)
    p2 = bool(PES02.search(tit)) and not nao_gestor
    areas = [k for k, rx in AREA.items() if rx.search(tit)]
    if not p2: motivo["PES-02 (abaixo de gerente)"] += 1; continue
    if not areas: motivo["sem área PES-04/05/06/07/17"] += 1; continue
    if r["icp"] in FORA or r["motivo"].startswith(("banco", "agencia", "fora_de_lista")) or "banco" in r["motivo"] or "agencia" in r["motivo"]:
        motivo[f"empresa fora ({r['icp'] if r['icp'] in FORA else r['motivo']})"] += 1; continue
    p3 = bool(re.search(r"\b(diretor\w*|director|vp|vice.?presiden\w*|chief|ceo|coo|cxo|cco|cmo|cdo|presidente|superintendente executiv\w*)\b", tit))
    keep.append({"nome": r["nome"], "slug": r["slug"], "headline": r["headline"], "cargo_avaliado": tit,
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
c = collections.Counter
print("decisor econômico", sum(k["is_decisor_economico"]=="true" for k in keep), "| champion", sum(k["is_champion"]=="true" for k in keep), "| técnico", sum(k["is_influenciador_tecnico"]=="true" for k in keep))
print("icp_triagem", c(k["icp_triagem"] for k in keep))
for k in keep: print(" -", k["nome"], "|", k["cargo_avaliado"][:80])
