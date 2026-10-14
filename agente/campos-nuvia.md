# Campos da Nuvia para o clone de prospecção

Conta: "Nuvia - Partners (Yuri)". Lista de campos consultada em 2026-10-14.

## Criar (não existem)

Criação pela interface da Nuvia (Configurações → Campos personalizados). Depois de criar, rodar `builder_list_custom_fields` para pegar os IDs e preencher a coluna ID e a tabela de configuração de `agente/etapas.md`.

| Título | Tipo | Contexto | Valores | Quem grava | Para que serve | ID |
|---|---|---|---|---|---|---|
| empresa | texto | contato | nome da empresa atual do lead | lista/triagem antes da campanha | `{empresa}` nas mensagens e na pergunta de dor | `[vazio]` |
| categoria_cargo | seleção | contato | 1 Decisor CX/Atendimento · 2 Decisor Marketing/Marca · 3 Champion Social/Insights · 4 Champion Operações/Qualidade · 5 Influenciador técnico · 6 Seller/Marketplace · 7 Executivo de BPO | triagem de ICP (`automations/leads/`) | escolher a pergunta de dor da Identificação | `[vazio]` |
| dor_principal | texto | conversa | a dor nas palavras do lead | agente (Identificação, Passo 3) | descrição do evento no calendário; escolha do caso no Modo consultivo | `[vazio]` |
| interesse | seleção | conversa | sim · não agora | agente | rota entre Agendar reunião e Modo consultivo | `[vazio]` |
| disponibilidade | texto | conversa | dia e horário exatamente como o lead escreveu | agente (Agendar reunião, Passo 2) | o Raul marcar o horário | `[vazio]` |

## Reaproveitar (já existem)

| Título | ID | Uso no agente |
|---|---|---|
| ICP | `6a82ffc3edb23472bc0bada0` | resultado da triagem de ICP |
| Cargo do lead | `6a31f8a38104cb0689286428` | cargo escrito (headline) |
| post-interacao | `6a58e4540add8161d61db3b8` | sinal do lead (post engajado, ponto em comum) |
| Segmento/setor da empresa | `6a31f8a45267ec2c73b99be6` | escolher o caso do setor |
| data_reuniao | `6a6350215d75994a17ce448a` | data da reunião confirmada |
| Motivo perdido | `6a633961056646004b1dab6c` | motivo_perda |

Nome do lead: campo nativo `contact.name`.

## Observações

- A persona 3 (Social/Insights) e a 7 (BPO) não têm pergunta de dor em `agente/etapas.md`, porque o playbook (§4) não tem ângulo para elas. Na campanha CX, BPO é exclusão fixa.
- A triagem (`automations/leads/preencher_campos.py`) hoje grava só ICP e Cargo do lead. Para preencher `empresa` e `categoria_cargo`, o script precisa gravar esses dois campos também.
