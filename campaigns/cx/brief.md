# Brief da campanha: CX (Sprinklr Service)

> Gerado com `campaign-plan` em 2026-10-11. Datas, geografia e orçamento confirmados pelo Raul. Sem orçamento de ads: plano 100% orgânico + outbound.

## 1. Visão geral
- **Nome sugerido:** Atendimento sem silos
- **Resumo:** mostrar a líderes de CX de grandes empresas brasileiras quanto custa operar canais separados, com números de casos públicos, e converter esse interesse em conversa 1:1.
- **Objetivo principal:** 20 reuniões com líderes de CX em 8 semanas (2,5 por semana).
- **Período:** 19/10/2026 a 11/12/2026. Termina antes das festas de fim de ano, quando agenda de C-Level some.
- **Geografia:** somente Brasil.
- **Objetivos secundários:** gerar uma lista de leads com sinal (comentaram, baixaram, responderam) para nutrir depois; validar qual pilar de conteúdo gera mais conversa.

## 2. Público
**Perfil:** Gerente, Head, Diretor ou C-Level de CX / Atendimento em empresa grande de varejo, banco/fintech, telecom, energia, mobilidade ou bens de consumo, que está pressionado por custo de atendimento alto, tempo de resposta ruim e canais (voz, WhatsApp, redes, chat) em ferramentas separadas, e busca fazer mais sem aumentar o time. Descobre soluções no LinkedIn, em eventos de CX (ex.: CONAREC) e por indicação de pares. Prioriza resultado mensurável e risco baixo.

- **Estágio de compra:** maioria em consciência do problema, não de solução. Por isso o conteúdo abre com dor + número, e o outbound faz pergunta, não pitch.
- **Gancho seu:** experiência de dentro com CRM e atendimento (Salesforce, Service Cloud) em empresas médias e grandes.

## 3. Mensagens
**Mensagem central:** Atendimento caro quase sempre é problema de canais apartados e descentralizados, não de gente; quem unificou reduziu tempo e custo sem contratar.

| Mensagem de apoio | Prova (de `brand/provas.md`) |
|---|---|
| Dá para responder mais rápido com o mesmo time | Santander Brasil: -20% na primeira resposta e -14% de carga dos agentes |
| Automação resolve o básico e libera o agente para o que importa | Telecom LATAM: 62% dos casos resolvidos só pelo bot e +13 pts de NPS |
| Unificar canais derruba custo operacional | Autopass: -14% de custo e resolução de 24h para 45 min |
| Agente com ferramenta boa fica na empresa | DTE Energy: -94% de rotatividade no contact center |

**Por canal:**
- **Post:** dor + número + caso público com link. Um CTA.
- **1:1:** gancho do perfil do lead + pergunta fechada. Número só se ele puxar o assunto. Sem reunião na 1ª mensagem.

## 4. Canais
| Canal | Papel | Formato | Esforço |
|---|---|---|---|
| Outbound LinkedIn (primário) | gera a maior parte das reuniões | convite com nota + 3 DMs | Alto |
| Conteúdo LinkedIn (orgânico) | ímã de autoridade e sinal | 3 posts/semana, 1 comment-gate por semana | Médio |
| Comment-gate | transforma comentário em DM e lead quente | material "Raio-X do atendimento" | Médio (setup único) |
| E-mail frio (paralelo) | alcança quem não aceita convite | 3 e-mails curtos | Médio |

**Matemática do funil [premissa, ajustar após semana 2]:**
600 convites (75/semana) → 35% de aceite = 210 conexões → 25% de resposta = ~52 conversas → 40% viram reunião = ~21 reuniões. Comment-gate e e-mail entram como folga para cobrir quedas.

## 5. Calendário
| Semana | Datas | Conteúdo | Outbound | Marcos / dependências |
|---|---|---|---|---|
| 0 (preparo) | 12-16/10 | Material "Raio-X do atendimento" (12 casos por setor) | Lista inicial de 150 leads + triagem de ICP | Material pronto antes do 1º comment-gate; `.env` com Nuvia/Apify |
| 1 | 19-23/10 | 3 posts P1 (custo); 1 comment-gate | 75 convites | Testar variáveis `empresa` e `primeiro nome` |
| 2 | 26-30/10 | 3 posts P2 (canais unificados) | 75 convites + DM 1 dos aceitos | **Checkpoint:** taxa de aceite e resposta; ajustar nota |
| 3 | 2-6/11 | 3 posts P1/P2; comment-gate | 75 convites + DMs 2 | Lista de mais 150 leads |
| 4 | 9-13/11 | 3 posts; post de caso brasileiro (Santander/Autopass) | 75 convites + e-mail 1 para não aceitos | **Meio da campanha:** meta parcial de 8-10 reuniões |
| 5 | 16-20/11 | 3 posts; comment-gate | 75 convites + DMs | Repostar o post campeão das semanas 1-4 |
| 6 | 23-27/11 | 3 posts | 75 convites + e-mail 2 | Lista final de 150 leads |
| 7 | 30/11-4/12 | 3 posts; comment-gate | 75 convites + DM 3 (último toque) | |
| 8 | 7-11/12 | 2 posts + post de retrospectiva | Só follow-ups e agendamento | Debrief e preenchimento da seção 8 do playbook |

20% dos slots de post ficam livres para reagir a notícia do setor.

## 6. Peças necessárias
| Peça | Tipo | Prioridade | Prazo |
|---|---|---|---|
| Raio-X do atendimento: 12 casos com números, por setor | PDF / carrossel (material do comment-gate) | Obrigatória | Semana 0 |
| Nota de conexão (2 variações para teste) | Outbound | Obrigatória | Semana 0 |
| DMs 1, 2 e 3 | Outbound | Obrigatória | Semana 0 |
| 3 e-mails frios | Outbound | Obrigatória | Semana 3 |
| Banco de 20 hooks por pilar | Conteúdo | Obrigatória | Semana 0 |
| ~24 posts LinkedIn | Conteúdo | Obrigatória | contínuo, 1 semana de antecedência |
| Mensagem do comment-gate (DM com o material) | Outbound | Obrigatória | Semana 0 |
| `brand/design.md` preenchido | Marca | Obrigatória antes de qualquer carrossel/PDF | Semana 0 |

## 7. Métricas
| KPI | Meta | Como medir |
|---|---|---|
| **Reuniões agendadas (principal)** | 20 em 8 semanas | Nuvia / agenda |
| Taxa de aceite de convite | ≥ 35% | LinkedIn / Nuvia |
| Taxa de resposta (conexões) | ≥ 25% | Nuvia |
| Resposta → reunião | ≥ 40% | Nuvia |
| Leads do comment-gate | ≥ 40 no total | `signals/` + Nuvia |

Cadência: revisão semanal às sextas (15 min); checkpoint formal nas semanas 2 e 4.

## 8. Orçamento
Sem orçamento de mídia nesta campanha. Custos apenas de ferramentas já existentes (Nuvia, Apify por uso). Se a meta parcial da semana 4 ficar abaixo de 8 reuniões, reavaliar ads como alavanca.

## 9. Riscos
| Risco | Mitigação |
|---|---|
| Aceite baixo de C-Level | Priorizar Gerentes/Heads (aceitam mais) e pedir indicação do decisor na conversa |
| Fim de ano reduz agenda nas semanas 7-8 | Concentrar convites nas semanas 1-5; nas finais, só follow-up |
| Conflito com política da Sprinklr (contas já trabalhadas por outro executivo, uso de marca) | Validar a lista de negativação e o uso dos cases com o gestor antes da semana 1 |
| Mensagem soar como pitch | Rodar `auditor-de-copy` e `humanize-pt-br` em toda mensagem antes do disparo |

## 10. Próximos passos
1. Lista de negativação: pedir ao gestor as contas que você não pode abordar.
2. Preencher `brand/design.md` (necessário para o material do comment-gate).
3. Produzir: material Raio-X, nota de conexão, DMs e banco de hooks.
4. Configurar `.env` (Nuvia, Apify) para lista, triagem de ICP e comment-gate.
