# Playbook: CX

Documento mestre da campanha. Conteúdo, ads e outbound são uma máquina só: nenhuma subpasta (`conteudo/`, `ads/creative/`, `outbound/`, `signals/`, `scripts/`) pode divergir do que está aqui. Preencha de cima pra baixo; o que ainda não sabe, escreva "A definir" (não apague a linha).

Plano completo, calendário e riscos: `brief.md`.

## 1. ICP

| Campo | Definição |
|---|---|
| **Empresa** | Grandes empresas (enterprise) com alto volume de atendimento e de conversa em redes sociais. Setores: varejo, bens de consumo (CPG), serviços financeiros, telecom, tecnologia, viagens e hotelaria, governo. Geografia: somente Brasil |
| **Sinal técnico/comportamental de fit** | A definir. Hipóteses: vagas abertas para contact center ou social media; operação omnichannel (WhatsApp, chat, redes); marca com crise ou alto volume de menções; troca recente de liderança de CX/Marketing |
| **Pessoa (decisor)** | Gerente, Head, Diretor e C-Level de CX / Atendimento (CCO, CXO). Marketing/Social tem campanha própria em `campaigns/marketing-social/` |
| **Dor comum** | Times, ferramentas e canais isolados que impedem uma visão única do cliente: atendimento lento, caro e sem visão única do cliente entre canais |
| **Quem fica de fora** | A definir. Sugestão: PMEs sem volume de atendimento/social que justifique plataforma enterprise |
| **Lista de negativação** | A definir (clientes atuais Sprinklr, concorrentes, parceiros) |

Fonte de verdade da base: `signals/` e `outbound/` ({{nome do arquivo}}).

## 2. Estratégia

- **Oferta:** Sprinklr Service, da plataforma Unified-CXM da Sprinklr (contact center omnichannel, agentes de IA). Provas: Leader no Gartner MQ de Social Media Management and Listening e de Voice of Customer Platforms (2026); 3M reduziu 90% do tempo de resposta a casos
- **Ímã (material rico):** Raio-X do atendimento: 12 casos com números, por setor (comment-gate). Vive em `conteudo/`
- **Ideia da campanha:** "Atendimento sem silos". Atendimento caro quase sempre é problema de canais apartados e descentralizados, não de gente; quem unificou reduziu tempo e custo sem contratar
- **Objetivo:** 20 reuniões com líderes de CX em 8 semanas
- **Métrica norte:** reuniões agendadas por semana (meta 2,5)

## 3. Canais

| Canal | Papel | Pasta | Status |
|---|---|---|---|
| Conteúdo (orgânico) | ímã, gera sinal | `conteudo/` | Planejado: 3 posts/semana |
| Ads | amplifica o mesmo ângulo pro mesmo público | `ads/creative/` | Fora desta campanha (sem orçamento) |
| Outbound LinkedIn | canal primário | `outbound/` | Planejado: 75 convites/semana |
| Outbound e-mail | paralelo, para quem não aceita convite | `outbound/` | Planejado: 3 e-mails a partir da semana 4 |
| Comment-gate | sinal de post vira DM | `signals/` | Sim, 1 por semana com o Raio-X |

## 4. Sequência (cadência)

Máximo de toques: 4 LinkedIn (convite + 3 DMs) + 3 e-mails.

| Toque | Canal | Ação / mensagem | Arquivo |
|---|---|---|---|
| D0 | LinkedIn | conexão com nota personalizada | `outbound/` |
| D+2 | LinkedIn / e-mail | msg 1 | `outbound/` |
| D+4 | LinkedIn / e-mail | msg 2 | `outbound/` |
| D+7 | LinkedIn / e-mail | msg 3 (último toque) | `outbound/` |
| Ao responder | | aprofundar a dor com pergunta; oferecer o caso do setor; propor reunião de 20 min | |
| Sem resposta | | segue impactado pelo conteúdo orgânico | |

Voz: `brand/voice-outbound.md` (1:1, registro de WhatsApp, curto).

## 5. Dados, filtros e enriquecimento

Log rastreável de como a base bruta virou a lista final. Um passo por linha, com o número antes e depois.

| Passo | O que foi feito | Antes → depois | Arquivo |
|---|---|---|---|
| 1 | {{priorização / remoção}} | {{N → N}} | {{...}} |
| 2 | {{filtro geográfico, ICP}} | | |
| 3 | {{enriquecimento (Apify, Nuvia)}} | | |

Triagem de ICP: `automations/leads/triagem_icp.py`. Campos de ICP e cargo gravados no contato da Nuvia antes de ativar a campanha.

## 6. Leads de exemplo e mensagens

3 a 5 leads reais da base, com a mensagem que cada um receberia. Serve de teste antes do disparo: se a mensagem não soa certa pra esses, não sai pra lista toda.

| Lead | Cargo / empresa | Gancho (atividade ou fato do perfil) | Mensagem enviada |
|---|---|---|---|
| {{nome}} | {{cargo, empresa}} | {{o que você viu}} | {{texto da DM}} |
| {{nome}} | | | |
| {{nome}} | | | |

Checar antes do disparo: variáveis `empresa` e `primeiro nome` carregando em todos os canais.

## 7. Ficha operacional

| Campo | Definição |
|---|---|
| **Data de início** | 2026-10-19 |
| **Duração do ciclo** | 8 semanas |
| **Data de fim** | 2026-12-11 |
| **Ferramenta / bot** | Nuvia, LinkedIn, e-mail |
| **Campaign ID (Nuvia)** | {{...}} |
| **Responsável** | Raul Pereira |

## 8. Resultados e debriefing

Preencher ao fim do primeiro ciclo.

| Métrica | Meta | Resultado |
|---|---|---|
| Leads abordados | | |
| Taxa de aceite de conexão | ≥ 35% | |
| Taxa de resposta | ≥ 25% | |
| Reuniões agendadas | 20 | |
| Custo / tempo por reunião | | |

**O que funcionou:** {{...}}
**O que não funcionou:** {{...}}
**Próximo experimento:** {{link para `playbook/experimentos/`}}

## 9. Pendente

- [ ] Definir geografia, sinal de fit e lista de negativação
- [ ] Validar lista de negativação e uso dos cases com o gestor
- [ ] Preencher `brand/design.md` e produzir o Raio-X
- [ ] Configurar `.env` (Nuvia, Apify)
