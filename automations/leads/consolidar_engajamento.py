"""Consolida o engajamento bruto (uma linha por interação) em uma linha por PESSOA.

Gatilho : depois de raspar comentários + curtidas de posts (Apify harvestapi).
Ação    : unifica a mesma pessoa que veio com dois formatos de URL e conta interações.
Destino : <pasta>/processed.csv, entrada do triagem_icp.py.

Por que existe: o ator de curtidas devolve o perfil como ID interno
(/in/ACoAA...) e o de comentários devolve o slug (/in/fulano). Sem unificar,
a mesma pessoa vira duas e a contagem de "posts tocados" sai errada.

Regra de unificação (nunca só por nome solto):
  1. slug igual;
  2. ID interno -> slug quando nome + headline são idênticos;
  3. ID interno -> slug quando o nome é único entre os slugs e só há 1 ID com esse nome.
Quem só curtiu e não tem slug conhecido fica com o ID interno (a URL abre normal).

Uso:
  python3 consolidar_engajamento.py --entrada campaigns/<publico>/signals/engajamento.csv
  (grava processed.csv na mesma pasta e reescreve as colunas de contagem do engajamento.csv)
"""

import argparse
import csv
import os
import re
import unicodedata
import urllib.parse
from collections import defaultdict


def ident(url):
    m = re.search(r"/in/([^/?#]+)", url or "")
    return urllib.parse.unquote(m.group(1)).lower() if m else ""


def eh_id_interno(s):
    return s.startswith("acoa")


def norm(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", t).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--saida", help="default: processed.csv na mesma pasta")
    a = ap.parse_args()
    saida = a.saida or os.path.join(os.path.dirname(os.path.abspath(a.entrada)), "processed.csv")

    rows = list(csv.DictReader(open(a.entrada, encoding="utf-8")))
    campos = list(rows[0].keys())

    # mapas a partir das linhas que têm slug real
    por_nome_head, por_nome = {}, defaultdict(set)
    for r in rows:
        s = ident(r["profile_url"])
        if s and not eh_id_interno(s):
            por_nome_head[(norm(r["nome"]), norm(r["headline"]))] = s
            por_nome[norm(r["nome"])].add(s)
    ids_por_nome = defaultdict(set)
    for r in rows:
        s = ident(r["profile_url"])
        if eh_id_interno(s):
            ids_por_nome[norm(r["nome"])].add(s)

    unificados = set()

    def chave(r):
        s = ident(r["profile_url"])
        if not eh_id_interno(s):
            return s
        n, h = norm(r["nome"]), norm(r["headline"])
        if (n, h) in por_nome_head:
            unificados.add(s)
            return por_nome_head[(n, h)]
        if len(por_nome.get(n, ())) == 1 and len(ids_por_nome[n]) == 1:
            unificados.add(s)
            return next(iter(por_nome[n]))
        return s

    pessoas = {}
    for r in rows:
        k = chave(r)
        r["slug"] = k
        p = pessoas.setdefault(k, {"name": r["nome"], "linkedin_identifier": k, "headline": r["headline"],
                                   "profile_url": f"https://www.linkedin.com/in/{k}",
                                   "posts": set(), "influenciadores": set(),
                                   "comentarios": 0, "reacoes": 0})
        if r["headline"] and len(r["headline"]) > len(p["headline"]):
            p["headline"] = r["headline"]
        p["posts"].add(r["post_url"])
        p["influenciadores"].add(r["influenciador"])
        p["comentarios" if r["tipo"] == "comentario" else "reacoes"] += 1

    for r in rows:
        p = pessoas[r["slug"]]
        r["interacoes_pessoa"] = p["comentarios"] + p["reacoes"]
        r["posts_distintos"] = len(p["posts"])
    if "slug" not in campos:
        campos.insert(campos.index("profile_url") + 1, "slug")
    with open(a.entrada, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (-r["posts_distintos"], r["nome"])))

    out_cols = ["name", "linkedin_identifier", "profile_url", "headline", "posts_tocados",
                "influenciadores", "comentarios", "reacoes", "contact_id", "status"]
    with open(saida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader()
        for p in sorted(pessoas.values(), key=lambda p: (-len(p["posts"]), -p["comentarios"])):
            w.writerow({**{k: p[k] for k in ("name", "linkedin_identifier", "profile_url", "headline",
                                             "comentarios", "reacoes")},
                        "posts_tocados": len(p["posts"]),
                        "influenciadores": "; ".join(sorted(p["influenciadores"])),
                        "contact_id": "", "status": "novo"})

    multi = sum(1 for p in pessoas.values() if len(p["posts"]) >= 2)
    print(f"interações: {len(rows)} | pessoas: {len(pessoas)} | IDs internos unificados: {len(unificados)}"
          f" | em 2+ posts: {multi} | saída: {saida}")


if __name__ == "__main__":
    main()
