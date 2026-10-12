# Triagem de ICP — padrão para TODOS os leads

`triagem_icp.py` é a classificação oficial de lead deste projeto. **Todo lead que entra, de qualquer post ou campanha, passa por aqui antes de virar campanha de outbound.** O ICP não é julgamento improvisado por post: é este vocabulário, calibrado com o seu mercado e revisado à mão. Ajuste as regex de `triagem_icp.py` ao SEU ICP.

## O que ele faz

Cruza o `processed.csv` do post com o export de conexões do LinkedIn e devolve, por lead: se é conexão, desde quando, empresa, cargo, headline, **nível hierárquico**, **ICP** e o **engagement_score** vindo do ledger.

```bash
python3 "automations/leads/triagem_icp.py" \
  --pasta "campaigns/<publico>/conteudo/AAAA-MM/<post>/signals" --prefixo <xxx>
```

Saída: `<prefixo>_conectados.csv` e `<prefixo>_nao_conectados.csv` na pasta do post, ordenados por nível e depois por score.

- `--conexoes` é opcional: sem ele, usa o **export mais recente** de `Connections*.csv` na raiz do projeto. A base envelhece rápido (186 conexões novas entre 16/08 e 17/08), então exportar de novo do LinkedIn antes de campanha grande.
- `--prefixo` default vem do nome da pasta do post.

- Sem `Connections*.csv` na raiz, o script avisa e segue: todo mundo sai como "não conectado". Sem `~/gtm-automation/engagement_ledger.json`, o score fica vazio.

## Etapa 0 (lista por engajamento de posts de terceiros): consolidar por pessoa

Quando o `engajamento.csv` vem do Apify (comentários + curtidas de vários posts), a mesma pessoa aparece com dois formatos de URL: o ator de curtidas devolve o ID interno (`/in/ACoAA...`), o de comentários devolve o slug. Sem unificar, a contagem por pessoa sai errada. Rode antes da triagem:

```bash
python3 automations/leads/consolidar_engajamento.py --entrada campaigns/<publico>/signals/engajamento.csv
```

Unifica por slug igual; ID interno vira slug quando nome + headline batem, ou quando o nome é único dos dois lados. Nunca só por nome solto. Reescreve a contagem no `engajamento.csv` e grava `processed.csv` na mesma pasta.

## Vocabulário por campanha (`--vocab`)

O vocabulário embutido no script é de Growth/Marketing. Campanha com outro ICP passa um JSON próprio (conteúdo é dado, não código):

```bash
python3 automations/leads/triagem_icp.py --pasta campaigns/cx/signals --prefixo cx-infl --vocab campaigns/cx/icp-vocab.json
```

Chaves do JSON (exemplo em `campaigns/cx/icp-vocab.json`): `excluir_empresa` (some do CSV), `fora_de_lista` (banco, agência), `fornecedor` (consultor, palestrante, vendor), `bpo`, `icp` e `nivel` (listas ordenadas), `nao_decisor` (cargo atual que derruba o decisor, ex. marketing manager, customer success, coordenador) e `decisor` (quais ICPs e níveis contam). Saem as colunas `decisor` e `motivo`, e a ordenação põe decisores primeiro.

Ao mudar o vocab, apague os `<prefixo>_*.csv` antes de rodar de novo, senão o `icp_manual()` congela o resultado antigo.

## Etapa 1b: filtro de pessoa do ICP (`filtro_pessoa.py`)

Aplica `campaigns/cx/icp/filtros.md` sobre o CSV triado: `is_pessoa_elegivel` = PES-02 (gerente ou acima) e alguma área (PES-04, 05, 06, 07 ou 17). A PES-01 (palavra-chave no título) foi retirada do ICP. Grava os campos `is_*` e imprime o % que sobrou e o motivo de cada corte.

```bash
python3 automations/leads/filtro_pessoa.py campaigns/cx/signals/cx-infl_nao_conectados.csv <saida.csv> <total_engajados> [vocab.json]
```

Não grave a saída por cima de `lista-influenciador.csv` depois que ele já tiver as colunas de empresa (Etapa 1c): elas se perdem.

Como lê o headline (revisado em 12/10/2026, depois que o loop de ICP recuperou 11 pessoas que o filtro tinha cortado):

- **Headline inteiro**, quebrado por `|`, `·`, `•` e ` l `. Trechos de passado (`ex-`, `Formerly`, `Previously`, `anteriormente`, `passagem por`) são ignorados: empregador antigo não derruba ninguém ("Formerly ... Banco X" não é banco).
- **Cargo** = todo trecho atual com palavra de gestão (gerente, head, diretor, executive, gestor...). Cargo de vendas e operação de mídia no 1º trecho (account executive, gestor de tráfego, analista) não conta.
- **Área** tem que estar no trecho do cargo, senão é lista de competências. Duas exceções: gestor de Customer Success e gestor de Operações contam como CX/Operações quando o headline declara CX, atendimento ou customer operations.
- **Sinônimos** de área: gestão de clientes, jornada do cliente, serviço ao cliente, pós-venda (CX); mkt, corporate affairs (Marketing); canais digitais, omnichannel (MarTech); e-commerce (Marketplace).
- **Exclusões reconferidas** no texto atual (vocab da triagem): palestrante, mentor, advisor e afins só derrubam quando são o cargo principal; marca de vendor derruba sempre; dono de firma própria que vende palestra/consultoria e quem atua em Professional Services/Service Delivery são fornecedor; "Gestão de Fornecedores (BPO)" é quem contrata BPO e fica.
- Imprime quem a triagem tinha excluído e o filtro reverteu, para revisão humana.
- `demo()` trava os casos que já deram errado e aborta a execução se algum regredir.

Resultado na campanha CX: 37 pessoas elegíveis (antes 23). Todas as 23 anteriores mais as 11 do loop; os 3 extras (HR Tech, incorporadora, resort) são decididos no filtro de empresa.

Tamanho da empresa não vem do LinkedIn: confirme os decisores na Nuvia (`search_brazil_companies` por domínio, grátis) antes de montar a lista.

## Etapa 1c: raspagem de perfil + filtro de empresa

O headline não diz onde a pessoa trabalha hoje. Para aplicar os eliminatórios de empresa (EMP-01, 04, 08, 11, 21, 22), raspe o perfil de quem passou na 1b:

1. **Apify `harvestapi/linkedin-profile-scraper`**, input `{"profileScraperMode":"Profile details no email ($4 per 1k)","queries":[<urls>]}`. Custa US$ 0,004 por perfil. No plano free o limite é 10 itens por run: rode em lotes de até 10. Confirme o custo com o aluno antes.
2. **Empresa atual** = `currentPosition`. Se vier vazio, use `experience[0]` e veja a data de fim: com fim preenchido a pessoa está sem empresa (sai da lista, mas vale acompanhar o próximo emprego).
3. **Nuvia `search_brazil_companies`** (grátis): busque por `dominio`, não por nome (a busca por nome é difusa e traz ruído). Resultado grande: salve e filtre em python. Porte da Receita só diz ME/EPP/Demais, então 1000+ funcionários vem do LinkedIn da empresa ou de conhecimento público.
4. **Regras fixas de exclusão:** banco, agência, BPO, vendor (martech, CPaaS), consultoria, autônomo, Vivo/Telefônica.
5. Grave em `signals/perfis-empresa.csv` (slug, empresa, cargo, status, cnpj, cnae, porte, fonte) e as colunas EMP + `is_empresa_elegivel` (`true`, `false` ou `verificar`), `anchor_case` (`itau` financeiro, `magalu` varejo e consumo), `tier_conta` (A elegível, B verificar, fora) e `motivo_empresa` no `lista-influenciador.csv`.
6. Excel bruto em `signals/lista-influenciador-bruto.xlsx`: abas resumo (fórmulas de %), bruto, pessoa elegível e lista final.

Primeira rodada (CX, 10/2026): 229 engajados, 23 pessoas elegíveis (10,0%), 4 empresas tier A e 2 a verificar (2,6% dos engajados). As 2 a verificar (Nissan, Align) foram confirmadas pelo aluno e subiram para tier A: lista final com 6 contas tier A. Tier B só se resolve com confirmação humana (quem vende conhece a base de clientes).

## Etapa 2 obrigatória: gravar os campos na Nuvia

A triagem só produz CSV. **Os campos não chegam na Nuvia sozinhos** — `POST /contacts` não
persiste `job_title`, só grava por PUT depois de criado. Então, logo depois da triagem:

```bash
python3 "automations/leads/preencher_campos.py" \
  --csv "<pasta>/<prefixo>_conectados.csv" --csv "<pasta>/<prefixo>_nao_conectados.csv"
```

De-para gravado (fonte: `Automations/comment-to-dm/runbook-segmentacao.md`):

| CSV | Nuvia | Tipo |
|---|---|---|
| `nome` | `name` | nativo |
| `slug` | `linkedin_identifier` | nativo |
| `headline` | `job_title` | nativo |
| `cargo` | `cargo-do-lead` | custom de contato |
| `icp` | `icp` | custom de contato |
| `score` | `engagement-score` | mantido pelo `score_engagement.py`, **não tocar** |
| — | `post-interacao` | acumula, **nunca sobrescrever** |

Escrita de campo custom é por **slug**, leitura volta por **título** (grava `icp`, lê `ICP`;
grava `cargo-do-lead`, lê `Cargo do lead`). O script limpa as duas grafias antes do PUT e
preserva `post-interacao` e `engagement-score`. É idempotente: quem já está correto volta como `ok`.

Exemplo de saída de uma rodada: 95 gravados, 10 já corretos.

## Vocabulário de ICP

Ordem importa, a primeira que casar vence:

| ICP | Pega |
|---|---|
| **Growth** | growth, demand gen, revops, aquisição, gtm, go-to-market |
| **Produto** | product manager/owner/lead, CPO, PO, gestão de produtos (PMM **não** entra: é Marketing) |
| **Dados** | data science, analytics, BI, engenheiro de dados, ML, estatística |
| **Tech** | dev, software engineer, devops, CTO, tech lead, IA, automação |
| **Vendas** | SDR, BDR, inside sales, AE, comercial, closer, new business, customer success |
| **Marketing** | marketing, mídia paga, tráfego, social media, conteúdo, branding, SEO, ads |
| **Fora** | nada acima |

Nível: C-level, Diretoria, Gerência, Consultor, Outro.

## Por que a separação conectado / não conectado importa

Muda a campanha inteira, não só a lista. Conectado recebe DM direta; não conectado precisa de connection request, e a conversa só começa depois do aceite, o que pode levar dias. As duas sequências são diferentes — a M3 da sequência de não conectados deve ser personalizada por ICP (Vendas, Marketing, Growth).

## Exclusões fixas

`{{seu-slug}}` e outros slugs seus, amigos e testes. Testes e amigos nunca entram em campanha. Editar a constante `EXCLUIR` no script.

## Revisão manual: como funciona e onde escorrega

`icp_manual()` lê os CSVs já gerados e **preserva** o que estiver na coluna `icp`, para que rodar de novo não apague correção humana. Efeito colateral: na **primeira** rodada de um post novo, o resultado do regex vira "manual" na rodada seguinte, mesmo sem ninguém ter revisado. Então a revisão do lote novo tem que acontecer logo depois da primeira execução, olhando a lista que o script imprime como `leads NOVOS (icp por regex, precisa revisao manual)`.

## Autoteste

`demo()` roda antes do main e trava os casos que já deram errado: PMM classificado como Produto, "growth product manager" caindo em Produto em vez de Growth, "sócio consultor" como C-level.

## Histórico

Nasceu como `triagem.py` dentro de `signals/` do post McKinsey Storytelling. Movido para cá em 24/08/2026 e parametrizado por `--pasta`, quando virou padrão de todos os posts.
