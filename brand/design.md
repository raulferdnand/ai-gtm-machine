# Design system

> Status: PROPOSTA (2026-10-11), aguardando OK do Raul. Identidade própria, propositalmente diferente da Sprinklr: tom editorial e quente (papel, grafite, terracota), serifa nos títulos. Não usar logo, cores ou fontes da Sprinklr.

> Spec de valores para qualquer visual (carrossel, post, slide, LP). Preencha antes de gerar o primeiro visual.

## Cores
| Token | Hex | Uso |
|---|---|---|
| Fundo | #F7F4EE (papel) | páginas e cards |
| Texto | #1C1F23 (grafite) | corpo e títulos |
| Destaque | #D9622B (terracota) | 1 elemento por peça, máx. 10% da área |
| Secundária | #23343B (petróleo escuro) | blocos escuros, rodapés |
| Neutra | #8C8A85 (cinza quente) | legendas, bordas |

## Tipografia
- Títulos: Fraunces SemiBold, 64-80 px no carrossel
- Corpo: Inter Regular, 28-32 px no carrossel
- Mono (dados/código): IBM Plex Mono (números de case em destaque: Fraunces Bold 120 px, cor Destaque)

## Formatos
- Post/carrossel: 1080×1350 px (4:5), margem de segurança 9%
- Capa de vídeo: não usada nesta fase

## Regras
- Sem gradientes. Um número grande por slide, sempre com o nome do case e a fonte ("case público Sprinklr") no rodapé
- Raio de borda: 8 px
- Assinatura fixa (foto + nome + slogan) sempre na mesma posição absoluta
- Miolo de carrossel: tudo em cards com ícone, nunca texto solto

## Ferramenta
HTML (Claude gera, exporta PDF/PNG). O Raul revisa cada peça antes de publicar.
