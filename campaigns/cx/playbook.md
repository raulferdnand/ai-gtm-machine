# Playbook: CX

Documento mestre da campanha. Conteúdo, ads e outbound são uma máquina só: nenhuma subpasta (`conteudo/`, `ads/creative/`, `outbound/`, `signals/`, `scripts/`) pode divergir do que está aqui. Preencha de cima pra baixo; o que ainda não sabe, escreva "A definir" (não apague a linha).

Plano completo, calendário e riscos: `brief.md`. Personas e provas por persona: `icp/personas.md`. Banco de provas: `brand/provas.md`.

## 1. ICP

| Campo | Definição |
|---|---|
| **Empresa** | Grandes empresas (enterprise) com alto volume de atendimento e de conversa em redes sociais. Setores: varejo, bens de consumo (CPG), serviços financeiros, telecom, tecnologia, viagens e hotelaria, governo. Geografia: somente Brasil. Contas tier A da 1ª lista: Amazon, Nissan, VR, UOL, Pluxee Brasil, Align Technology |
| **Sinal técnico/comportamental de fit** | Engajou (comentou ou curtiu) post de um dos 5 influenciadores de CX monitorados: Jacques Meir, Ricardo Pena, Bruno Gobbato, Roberto Madruga, Sérgio Frías. Hipóteses ainda não usadas: vagas de contact center ou social media, operação omnichannel, crise ou alto volume de menções, troca de liderança de CX |
| **Pessoa (decisor)** | Gerente, Head, Diretor e C-Level de CX / Atendimento (CCO, CXO), regra PES-02 (gerente para cima) em área-alvo (PES-03/04/05/06/07/17). Marketing/Social tem campanha própria em `campaigns/marketing-social/` |
| **Dor comum** | Times, ferramentas e canais isolados que impedem uma visão única do cliente: atendimento lento, caro e sem visão única do cliente entre canais |
| **Quem fica de fora** | Abaixo de gerente (PES-02); fornecedores, consultores, palestrantes e vendors; BPO e terceirizadas de atendimento (exclusão fixa nesta campanha; BPO é persona 7, canal); bancos como conta-alvo; empresas pequenas, médias ou B2B sem volume que justifique plataforma enterprise; pessoas sem cargo atual |
| **Lista de negativação** | A definir (clientes atuais Sprinklr, concorrentes, parceiros) |

Fonte de verdade da base: `signals/` e `outbound/` (`lista-cx-final.xlsx`, fora do git por conter dados de leads).

## 2. Estratégia e canais

- **Oferta:** Sprinklr Service, da plataforma Unified-CXM da Sprinklr (contact center omnichannel, agentes de IA). Provas: Leader no Gartner MQ de Social Media Management and Listening e de Voice of Customer Platforms (2026); 3M reduziu 90% do tempo de resposta a casos
- **Prova ou artefato:** casos públicos de `brand/provas.md`, escolhidos pelo segmento da conta (§4, "Prova por segmento")
- **Escopo da entrega:** A definir
- **CTA único:** conversa curta, só depois que a pessoa reconhece a dor ("Faz sentido aprofundar o tema?")
- **Champion interno:** persona 4 (Operações, Planejamento e Qualidade) na mesma conta do decisor. Como checar: A definir
- **Ímã (material rico):** Raio-X do atendimento: casos públicos com números, por setor (comment-gate). Vive em `conteudo/`
- **Ideia da campanha:** "Atendimento sem silos". Atendimento caro quase sempre é problema de canais apartados e descentralizados, não de gente; quem unificou reduziu tempo e custo sem contratar. No outbound, o quebra-gelo é o post do influenciador que a pessoa acabou de engajar
- **Objetivo (60-90 dias):** 20 reuniões com líderes de CX em 8 semanas
- **Métrica norte:** reuniões agendadas por semana (meta 2,5)

**Canais:**

| Canal | Papel | Pasta | Status |
|---|---|---|---|
| Conteúdo (orgânico) | ímã, gera sinal | `conteudo/` | Planejado: 3 posts/semana |
| Ads | amplifica o mesmo ângulo pro mesmo público | `ads/creative/` | Fora desta campanha (sem orçamento) |
| Outbound LinkedIn | canal primário | `outbound/` | Planejado: 75 convites/semana. Notas dos 6 tier A escritas, aguardando aprovação do Raul |
| Outbound e-mail | paralelo, para quem não aceita convite | `outbound/` | Planejado: 3 e-mails a partir da semana 4 (sequência a desenhar) |
| Comment-gate | sinal de post vira DM | `signals/` | Sim, 1 por semana com o Raio-X |

## 3. Dados, filtros e sinais

Log rastreável de como a base bruta virou a lista final. Um passo por linha, com o número antes e depois.

| Passo | O que foi feito | Antes → depois | Arquivo |
|---|---|---|---|
| 1 | Coleta de quem engajou em posts dos 5 influenciadores (Jacques Meir 67, Ricardo Pena 50, Sérgio Frías 39, Roberto Madruga 33, Bruno Gobbato 31, 8 em mais de um) + dedup | 228 | `lista-cx-final.xlsx` › Base completa |
| 2 | Triagem de ICP por regra fixa. Saíram: 102 abaixo de gerente, 60 fornecedor/consultoria, 38 sem área-alvo, 15 empresa fora do perfil, 4 banco, 3 BPO | 228 → 6 | idem (Motivo inicial) |
| 3 | Revisão em loop dos excluídos (rodadas 1 e 2): 11 reaceitos por erro de regra (ex.: banco era empregador passado; gerente de BPO do lado contratante) | 6 → 17 | `lista-cx-final.xlsx` › Aprovados (17) |
| 4 | Corte por conta: só empresa confirmada tier A segue para disparo; 11 ficam "a verificar (sem raspagem)" | 17 → 6 | `lista-cx-final.xlsx` › Tier A + notas |

### Sinais e priorização

| Sinal | Peso | Fonte | Como medir |
|---|---|---|---|
| S1. Conta tier A | alto | lista de contas | Situação da conta = "tier A" |
| S2. Nível de decisão | alto | headline LinkedIn | Nível = C-level ou Diretoria (Gerência entra como champion) |
| S3. Perfil ICP (categoria_cargo) | alto | headline + triagem | Persona 1 a 7 de `icp/personas.md` |
| S4. Tipo de engajamento | médio | post do influenciador | Comentou (com texto citável) > curtiu |
| S5. Tema do post engajado | médio | post do influenciador | Assunto do post (ex.: painel CONAREC, ROI de CX, estudo do consumidor) |
| S6. Posts tocados | médio | coleta | Nº de posts engajados (1, 2 ou 3+) |
| S7. Palavras de área no headline | baixo | headline LinkedIn | Termos como Qualidade, BPO, Canais Digitais, E-commerce, NPS, Cost to Serve, Customer Journey |

Critério de corte da lista qualificada: S1 = tier A e S3 dentro do ICP. Arquivo: `signals/lista-cx-final.xlsx`.

**Enriquecimento antes do disparo** (campos por lead; todo sinal com fonte e data):

| Campo | Fonte | Para que serve |
|---|---|---|
| Nome, cargo, headline e sobre do decisor | LinkedIn (coleta dos posts) | personalizar o gancho |
| Sinal de champion interno | persona 4 na mesma empresa | decidir se avança para a reunião |
| Post engajado + trecho do comentário | post do influenciador | gancho da nota de conexão (S4, S5) |
| Empresa atual confirmada | raspagem do perfil | tirar os 11 "a verificar" da fila |

O que **não** entra no enriquecimento pré-disparo: A definir.

Triagem de ICP: `automations/leads/triagem_icp.py`. Campos de ICP e cargo gravados no contato da Nuvia antes de ativar a campanha.

### Dores do ICP (top 5)

Hipóteses tiradas dos sinais acima e de `icp/personas.md`, não de entrevista.

| # | Dor (fato do negócio) | Evidência na base |
|---|---|---|
| D1 | Atender rápido deixou de diferenciar e virou o mínimo esperado; a operação trava quando tenta acelerar sem cair a qualidade | S4/S5: decisora tier A (Amazon) comentou o painel de CEOs do CONAREC com essa leitura; único tier A com 2 posts tocados (S6) |
| D2 | CX é cobrado a provar retorno financeiro e, sem esse número, é das primeiras áreas cortadas | S4/S5: gerente tier A (Align) comentou "colocou em palavras o que sinto" no post do Gobbato sobre o tema; 18 dos 36 engajadores do Gobbato são de CX, a maior proporção entre os 5 influenciadores |
| D3 | O consumidor está com o orçamento apertado (juros, bets) e troca de marca com menos tolerância a erro; cada falha de atendimento custa cliente | S5: 3 dos 6 tier A (VR, UOL, Pluxee) curtiram o estudo "O brasileiro entre o corre e o refúgio" |
| D4 | O volume cresce e a operação precisa escalar (IA, BPO) sem subir o custo de servir nem derrubar NPS e qualidade | S7: headlines com "AI-Driven Service, NPS & Cost to Serve", "Gestão de Fornecedores (BPO)… Qualidade e Performance", "Quality/Contact Center/Ombudsman" |
| D5 | A experiência é decidida em canais e áreas que CX não controla (digital, e-commerce, outros mercados) | S7: "Canais Digitais", "E-commerce" (2 leads), "Digital Transformation" e "LATAM" em 4 decisores |

## 4. Matriz de ângulos (dor × cargo)

Uma linha por cargo da lista qualificada. O ângulo só pode usar sinal que existe na seção 3. Provas só de `brand/provas.md` e `icp/personas.md` (Telefónica e Vivo fora, a pedido do Raul). Não há lead das personas 3 e 7 na lista atual.

| Cargo (categoria_cargo) | Dor específica | Ângulo da mensagem (como ele descreve a dor / a quem atribui a causa) | Sinal que usa | Prova |
|---|---|---|---|---|
| **1 Decisor CX/Atendimento** (7 leads) | D2 + D1 | "Entrego a experiência, mas na mesa do CEO a área ainda aparece como custo." Atribui a causa à falta de um número que ligue CX a receita e retenção, e ao orçamento decidido fora da área | S1 + S2 (C-level/Diretoria) + S3 = 1 + S4/S5 | Telecom LATAM: 110 mil vendas no WhatsApp em 6 meses. Fintech LATAM: NPS de 47 para 71. Autopass: -14% de custo operacional |
| **2 Decisor Marketing/Marca** (2 leads) | D3 | "Uma reclamação mal resolvida vira problema de marca e de venda." Atribui a causa ao atendimento e às áreas operacionais | S2 + S3 = 2 + S7 (MKT/Comunicação) + S5. Sem S1: só após confirmar empresa | Fintech LATAM: US$ 1,5 mi em mídia espontânea. Mover estes leads para `campaigns/marketing-social/` |
| **4 Champion Operações/Qualidade** (6 leads) | D4 | "O volume sobe, o time e o fornecedor não acompanham, e a meta de qualidade cai na minha conta." Atribui a causa ao BPO, à falta de ferramenta e ao headcount congelado | S3 = 4 + S7 (Qualidade, BPO, CS, Contact Center) + S4 | Santander Brasil: pico de demanda com equipe igual; -14% de carga dos agentes, -20% na primeira resposta, +35% de NPS com agente. DTE Energy: -94% de rotatividade |
| **5 Influenciador técnico** (1 lead) | D5 | "Cada canal digital tem regra, fila e dado próprio, e a sustentação vive apagando incêndio." Atribui a causa à integração entre canais e sistemas | S3 = 5 + S7 ("Canais Digitais") + S5 | Autopass: dois times e duas ferramentas viraram um; resolução de 24h para 45 min, 99,5% no SLA. Banco LATAM: 100% dos casos classificados e distribuídos automaticamente |
| **6 Seller/Marketplace** (1 lead) | D3 + D5 | "No e-commerce, problema de atendimento vira avaliação ruim e venda perdida." Atribui a causa à operação e ao marketplace | S2 + S3 = 6 + S7 ("E-commerce") | Sam's Club: 92% das mensagens respondidas em menos de 1h (era 8h). Sem case público de seller (`icp/personas.md`) |

### Prova por segmento de atuação

| Segmento | Contas da lista | Case | Resultado |
|---|---|---|---|
| Benefícios / financeiro | VR, Pluxee | Fintech LATAM | -70% a -75% na primeira resposta; NPS 47 → 71 |
| | | Santander Brasil | -20% na primeira resposta; -14% de carga; +35% de NPS com agente |
| | | Banco LATAM | Primeira resposta de 66,5 para 30 min; NPS 81,29 |
| Mídia, internet e tecnologia | UOL | Big tech global | -33% de contatos improdutivos no 1º mês |
| | | Telecom LATAM | 62% dos casos só no bot; +13 pts de NPS |
| Automotivo / mobilidade | Nissan | Autopass | Resolução de 24h para 45 min (-97%); -14% de custo operacional |
| Varejo / e-commerce | Amazon, Casas Bahia | Sam's Club | 92% respondido em menos de 1h; 600+ clubes monitorados 24/7 |
| Saúde / odontologia | Align Technology | Operadora de saúde brasileira (`icp/personas.md`) | -92% no SLA de primeira resposta; 48% dos casos resolvidos pelo bot. Confirmar se pode citar fora |
| Indústria global | Align Technology (apoio) | 3M | -90% no tempo de resposta a casos; 21 idiomas |

Bancos servem como prova para benefícios e fintech, mas não são conta-alvo (ver §1).

## 5. Sequência (cadência)

Máximo de toques no LinkedIn: 3 (nota de conexão + 2 FUPs). E-mail segue o plano do canal (§2) e terá sequência própria. Cada toque parte de um ângulo da seção 4. Dias contados a partir do aceite da conexão.

**Tipo: ascendente.** Cada toque pede um pouco mais que o anterior: a nota só retoma o post, o FUP 1 nomeia a dor e pergunta, e o FUP 2 traz o case e o único pedido de conversa. O motivo é o sinal da §3: engajar com post de terceiro (S4/S5) mostra interesse no tema, não intenção de compra. Com diretoria e C-level de contas tier A, pedir reunião no primeiro toque queima a conta. A prova só convence depois que a dor foi reconhecida.

| Toque | Canal | Dia | Ideia central | Sinal que usa | Regra de saída |
|---|---|---|---|---|---|
| 1. Nota de conexão | LinkedIn | D0 (envio) | Retomar o que a pessoa disse ou curtiu no post do influenciador, sem falar de produto | S4 (comentou/curtiu) + S5 (tema do post) + S6 | Não aceitou em 14 dias: sai do LinkedIn e vai para e-mail/conteúdo. Aceitou e respondeu: sai da cadência e segue 1:1 |
| 2. FUP 1 | LinkedIn (DM) | D+2 após o aceite | Nomear a dor do cargo dela (§4) como algo que outros líderes da mesma função relatam, e perguntar se é assim na operação dela | S3 (categoria_cargo → dor e ângulo da §4) + S7 + S2 | Respondeu: sai da cadência e segue 1:1. "Não é o momento" ou "sem interesse": encerra e marca na Nuvia. Sem resposta: vai para o FUP 2 |
| 3. FUP 2 (último) | LinkedIn (DM) | D+7 após o aceite | Mostrar como uma empresa do mesmo segmento resolveu essa dor, com o número do case (§4, "Prova por segmento"), e convidar para uma conversa curta | S1 (conta tier A → segmento) + S3 (dor do cargo) | Respondeu: segue para o CTA. Sem resposta em 7 dias: encerra o outbound e o lead fica no conteúdo orgânico, sem novos toques |
| Ao responder | LinkedIn | assim que responder | Aprofundar a dor com pergunta; oferecer o caso do setor; convidar com "Faz sentido aprofundar o tema?" | o que a pessoa disse | A cadência para; não ganha toques extras |
| Sem resposta | Conteúdo orgânico | após o FUP 2 | Segue impactado pelo conteúdo com o mesmo ângulo da §4 | S3 | Volta ao outbound só se surgir sinal novo (S4/S5 em outro post) |

Regra de saída: qualquer resposta (positiva ou negativa), descadastro, ou aceite sem resposta até 7 dias após o FUP 2. Se a resposta muda o fluxo (ex: dispara um build), a cadência não ganha toques extras.

Voz: `brand/voice-outbound.md` (1:1, registro de WhatsApp, curto).

## 6. Leads de exemplo e mensagens

3 a 5 leads reais da base, com a mensagem que cada um receberia. Nomes e textos completos ficam em `signals/lista-cx-final.xlsx` › Tier A + notas (fora do git, dados de leads).

| Lead | Cargo / empresa | Gancho (atividade ou fato do perfil) | Mensagem enviada |
|---|---|---|---|
| Lead A | Head CX & Operações LATAM, e-commerce (tier A) | Comentou o post do Jacques Meir sobre o painel de CEOs do CONAREC | Nota A: retoma o comentário e a ideia de acelerar sem perder humanidade |
| Lead B | Sr Manager CX LATAM, saúde/odonto (tier A) | Comentou o post do Bruno Gobbato sobre ROI de CX | Nota A: cobrança para CX provar ROI em época de layoff |
| Lead C | Diretor CX, automotivo (tier A) | Comentou o post do Ricardo Pena sobre o trabalho com a marca | Nota A: fazer CX funcionar em dois mercados ao mesmo tempo |
| Lead D | Diretor de Relacionamento, mídia/internet (tier A) | Curtiu o estudo do Jacques Meir "O brasileiro entre o corre e o refúgio" | Nota A: consumidor espremido tem menos espaço para erro |
| Lead E | Gerente de CX, benefícios (tier A) | Curtiu o mesmo estudo | Nota A: benefício como alívio no fim do mês |

**Modelos de nota de conexão**: os padrões que funcionaram nas 6 contas tier A, todos ancorados no engajamento do lead.

| Tipo de sinal | Modelo da nota (≤ 300 caracteres) |
|---|---|
| Comentou o post do influenciador | Oi [NOME], tudo bem? Li seu comentário sobre [TEMA] no post do [INFLUENCIADOR]. [Uma frase sobre a dor que o comentário toca]. Vamos conectar? |
| Comentário com frase marcante | Oi [NOME], tudo bem? "[FRASE DO COMENTÁRIO]" Sua frase no post do [INFLUENCIADOR] resumiu [TEMA] melhor que o próprio post. Vamos conectar? |
| Só reagiu / acompanha o influenciador | Oi [NOME], tudo bem? Vi que você acompanha o [INFLUENCIADOR]. [Uma frase ligando o post ao negócio do lead]. Vamos conectar? |

Regras: "Oi" sempre, sem abreviação, sem travessão, sem "Trabalho com" nem "Vi que você cuida", uma pergunta leve no fim. Leads A, B e C têm versão B alternativa; nada enviado.

Status: aguardando aprovação do Raul.

Checar antes do disparo: variáveis `empresa` e `primeiro nome` carregando em todos os canais, testando cada canal separadamente (o bug costuma carregar no e-mail e falhar no LinkedIn).

**Pontos de atenção da campanha:**
- Toda nota cita o post que a pessoa engajou; não existe versão genérica.
- Comentário (S4 alto) rende gancho mais forte que curtida: nas curtidas, a nota fala do tema do post, não da opinião da pessoa.
- Os 11 aprovados "a verificar" só entram depois de confirmar empresa atual.
- Personas 2, 5 e 6 têm 1 a 2 leads cada: o ângulo é hipótese até a primeira resposta.

## 7. Ficha operacional

| Campo | Definição |
|---|---|
| **Data de início** | 2026-10-13 |
| **Duração do ciclo** | 8 semanas |
| **Data de fim** | 2026-12-04 |
| **Ferramenta / bot** | Nuvia, LinkedIn, e-mail |
| **List ID (Nuvia)** | A definir |
| **Campaign ID (Nuvia)** | A definir |
| **Agent ID (Nuvia)** | A definir |
| **Responsável** | Raul Pereira |

## 8. Metas, resultados e debriefing

Metas preenchidas antes do disparo; resultados ao fim do primeiro ciclo. A métrica norte vem da seção 2.

| Métrica | Meta | Resultado |
|---|---|---|
| Leads abordados | 6 tier A no 1º lote (17 após verificação); 75 convites/semana no ritmo cheio | |
| Taxa de aceite de conexão | ≥ 35% | |
| Taxa de resposta | ≥ 25% | |
| Tempo entre resposta e próxima ação (SLA) | A definir | |
| % de respondentes com champion identificado | A definir | |
| Reuniões agendadas | 20 | |
| Custo / tempo por reunião | A definir | |

**O que funcionou:** A definir
**O que não funcionou:** A definir
**Próximo experimento:** A definir

## 9. Pendente

- [ ] Definir lista de negativação
- [ ] Validar uso dos cases com o gestor (inclui operadora de saúde brasileira de `icp/personas.md`)
- [ ] Mover os 2 leads de Marketing/Marca para `campaigns/marketing-social/`
- [ ] Confirmar empresa atual dos 11 aprovados "a verificar"
- [ ] Desenhar a sequência de e-mail (3 toques, a partir da semana 4)
- [ ] Aprovar o design proposto e produzir o Raio-X (semana 1)
- [ ] Revisar mensagens-base (`outbound/mensagens-base.md`) e escolher hooks (`conteudo/banco-de-hooks.md`)
- [ ] Configurar `.env` (Nuvia, Apify)
