# Agente: clone de prospecção do Raul

`system.md` é o system prompt (identidade, missão, regras, tom, expressões e palavras proibidas). É genérico para campanhas do segmento de CX/Marketing que vendam Sprinklr. O que é de cada campanha (sinal do lead, cadência, ângulo por cargo) entra nos campos do contato ou nas etapas do agente, não no system.

Status: aguardando aprovação do Raul. Não gravar na Nuvia antes do OK (regra do `CLAUDE.md`).

## Fontes usadas

| Fonte | O que saiu dela |
|---|---|
| `brand/voice-outbound.md` (tom de voz 1:1) | registro, "Oi", "Obrigado", proibições, limites de caracteres e linhas, anatomia da 1ª mensagem |
| `brand/voice.md` | arquétipo, registro executivo, palavras proibidas de conteúdo |
| `brand/background.md` | trajetória e pontos em comum |
| `brand/provas.md` | tabela de casos (sem Telefónica e Vivo) |
| `campaigns/cx/playbook.md` | ICP, dor comum, ângulo por cargo, cadência ascendente, CTA, Gartner |
| `campaigns/cx/outbound/mensagens-base.md` (mensagens revisadas) | sinais de conexão, DMs, respostas, expressões |
| 4 conversas reais enviadas no chat (WhatsApp e LinkedIn, jul. a set. 2026) | expressões, apresentação da Sprinklr, convites de almoço/Swag/evento, quebra em mensagens curtas, emojis |

Não encontrados: `mensagens.csv` e `tom-de-voz.md`. O tom de voz veio de `brand/voice-outbound.md`.

## Registro do humanize-pt-br

O rascunho v0 tinha: "desempenha um papel fundamental", "plataforma robusta que potencializa a jornada do cliente" (vocabulário de IA e ênfase inflada); "não só apresentando a Sprinklr, mas entendendo profundamente" (paralelismo negativo); "garantindo que a conversa evolua" (gerúndio de muleta); "empatia, clareza e objetividade" (regra de três); travessão no tom. Na versão final: frases afirmativas com sujeito e verbo, sem gerúndio de ligação, sem trio de adjetivos, sem travessão e com negrito só onde a estrutura precisa.

Das conversas reais, ficaram de fora por conflito com as regras: "Te add no Linkedin" (abreviação, virou "Te adicionei no LinkedIn"), "Olá" (a regra é "Oi"), "jornada do cliente" e "revolucionando" (lista de proibidas), e os dois convites na mesma mensagem (regra de um pedido por mensagem).

## Pendente (perguntas para o Raul)

1. Enviar `mensagens.csv` para calibrar as expressões com mais mensagens revisadas.
2. "Olá" ou "Oi"? As conversas reais usam "Olá"; a voz revisada manda "Oi". O prompt está com "Oi".
3. Emoji: o prompt libera só 🇧🇷 e 🥩🍷. Confirmar.
4. Número "cliente do segmento financeiro: 45% menos casos na fila e 83% menos tempo médio de atendimento": qual o caso público e o link? Até lá, fica fora.
5. Almoço, Swag Brinde e convite de evento: em que toque podem entrar (a cadência proíbe pedido na 1ª mensagem) e qual evento vale agora?
6. Passagem para o Raul: só atribuir a conversa ou mandar um link de agenda?
7. Se o lead perguntar se é robô: o prompt manda assumir que é um assistente do Raul. Confirmar.
8. Indicação interna ("{pessoa} participou do nosso evento"): de onde vem esse dado na Nuvia?
