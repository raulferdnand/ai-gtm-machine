# Fontes públicas do ICP: Sprinklr no Brasil

Complementa `filtros.md`.

> **Atenção:** a parte 1 usa a numeração de critérios da versão anterior do ICP (antes das âncoras Itaú e Magalu). Os IDs não batem com o `filtros.md` atual; as fontes continuam válidas, mas a tabela precisa ser renumerada.
 A parte 1 lista as 5 melhores fontes por critério, em ordem de prioridade. A parte 2 é o catálogo de fontes, com o que cada uma entrega e o esforço de extração. A parte 3 traz os 10 concorrentes.

**Escala de esforço**

- **Baixo:** dado aberto, CSV, API ou página única com o número visível.
- **Médio:** busca manual por empresa ou scraping simples de página pública.
- **Alto:** exige login, tem bloqueio contra scraping ou precisa de leitura e julgamento humano.

---

## 1. Cinco fontes por critério

### Empresa

| Critério | Campo | Fonte 1 | Fonte 2 | Fonte 3 | Fonte 4 | Fonte 5 |
|---|---|---|---|---|---|---|
| EMP-01 · CNAE em setor-alvo | `is_cnae_setor_alvo` | Receita Federal (Dados Abertos CNPJ) | Casa dos Dados | Econodata | LinkedIn (setor da página) | Google ("nome" + CNPJ) |
| EMP-02 · Telecom ou financeiro | `is_telecom_ou_financeiro` | Receita Federal (Dados Abertos CNPJ) | Banco Central (IF.data) | Anatel (prestadoras) | SUSEP (seguradoras autorizadas) | LinkedIn (setor da página) |
| EMP-03 · Sujeita ao Decreto do SAC | `is_sujeita_decreto_sac` | Planalto (texto do Decreto 11.034/2022) | Receita Federal (CNAE) | Banco Central (IF.data) | Anatel (prestadoras) | ANS (operadoras ativas) |
| EMP-04 · 1.000+ funcionários | `has_1000_funcionarios` | LinkedIn (página da empresa) | CVM (Formulário de Referência) | Econodata (faixa de funcionários) | Relatório anual ou de sustentabilidade | Glassdoor (porte) |
| EMP-05 · 10.000+ funcionários | `has_10000_funcionarios` | LinkedIn (página da empresa) | CVM (Formulário de Referência) | Relatório anual ou de sustentabilidade | Econodata | Glassdoor (porte) |
| EMP-06 · Receita ≥ R$ 1 bi | `has_receita_1bi` | CVM (RAD, DFP e ITR) | Valor 1000 | Melhores e Maiores Exame | Diário Oficial (balanço de S.A. fechada) | Econodata (estimativa) |
| EMP-07 · CNPJ ativo no Brasil | `is_cnpj_ativo_br` | Receita Federal (Dados Abertos CNPJ) | Receita Federal (consulta CNPJ online) | Casa dos Dados | CNPJ.biz | Econodata |
| EMP-08 · Multinacional ou 2+ países | `is_multinacional` | LinkedIn (aba Locais) | Site institucional (seletor de país) | Relatório anual | Crunchbase | Google ("nome" + subsidiária) |
| EMP-09 · Vende para consumidor final | `is_b2c_ou_b2b2c` | Site institucional | Reclame Aqui (empresa tem página ativa) | Instagram (perfil de marca) | Google Maps (lojas) | Receita Federal (CNAE) |
| EMP-10 · 3+ marcas | `has_3_marcas` | INPI (busca por titular) | Site ("nossas marcas") | CVM (Formulário de Referência) | LinkedIn (páginas vitrine) | Wikipedia |
| EMP-11 · 10+ perfis sociais | `has_10_perfis_sociais` | Busca nativa em Instagram, TikTok, X, YouTube e Facebook | Rodapé do site (links oficiais) | Meta Ad Library (páginas anunciantes) | Social Blade | Google ("nome" site:instagram.com) |
| EMP-12 · 1 milhão+ de seguidores | `has_1m_seguidores` | Perfis oficiais (contador público) | Social Blade | HypeAuditor (versão gratuita) | Relatório anual ou release | Google |
| EMP-13 · 1.000+ reclamações em 12 meses | `has_1000_reclamacoes_12m` | Reclame Aqui | Consumidor.gov.br (dados abertos) | Banco Central (ranking de reclamações) | Anatel (dados de reclamações) | Procon-SP (cadastro de reclamações fundamentadas) |
| EMP-14 · 100+ pontos de venda | `has_100_pontos_venda` | Receita Federal (nº de filiais por CNPJ raiz) | Localizador de lojas do site | Google Maps | Ranking SBVC (maiores varejistas) | Release de resultados (CVM) |
| EMP-15 · 2+ agências | `has_2_agencias` | Meio & Mensagem | Propmark | LinkedIn (posts de agências anunciando contas) | Effie Brasil e Cannes (ficha técnica dos cases) | Google Notícias |
| EMP-16 · Fora de recuperação judicial | `is_sem_recuperacao_judicial` | Jusbrasil | Escavador | Tribunais estaduais (consulta processual) | CVM (fatos relevantes) | Valor Econômico |
| EMP-17 · Não é cliente Sprinklr | `is_nao_cliente_sprinklr` | Sprinklr Customer Stories | Sprinklr 10-K (SEC) | LinkedIn (funcionários com skill "Sprinklr") | Vagas citando Sprinklr | G2 e Gartner Peer Insights (empresa do revisor) |
| EMP-18 · Vaga em CX, social ou MarTech em 90 dias | `has_vaga_cx_90d` | LinkedIn Vagas | Gupy | Site de carreiras | Indeed | Catho |
| EMP-19 · Novo líder em 6 meses | `has_novo_lider_cx_6m` | LinkedIn (data de início do cargo) | LinkedIn (posts "novo cargo") | Meio & Mensagem e Propmark (movimentações) | CVM (diretoria estatutária) | Google Notícias |
| EMP-20 · M&A ou nova marca em 12 meses | `has_ma_ou_marca_12m` | CVM (fatos relevantes) | CADE (atos de concentração) | INPI (pedidos novos) | Valor Econômico e Google Notícias | LinkedIn (posts da empresa) |
| EMP-21 · Reputação em queda | `is_reputacao_em_queda` | Reclame Aqui (nota 6 meses vs. 12 meses) | Consumidor.gov.br | Google Trends ("marca" + problema) | X (busca avançada) | Reddit |
| EMP-22 · Grande campanha em 6 meses | `has_grande_campanha_6m` | Meta Ad Library | Google Ads Transparency Center | Meio & Mensagem | Propmark | Releases no site da empresa |
| EMP-23 (!) · Contrato vence em até 9 meses | `has_contrato_vencendo_9m` | Sem fonte pública | Proxy: PNCP (contratos de estatais) | Proxy: vagas de implantação de ferramenta | Proxy: reviews recentes no G2 | Proxy: conversa com a conta |
| EMP-24 · Usa ferramenta concorrente | `has_ferramenta_concorrente` | Vagas (requisitos citam a ferramenta) | Cases públicos dos concorrentes (seção 3) | LinkedIn (skills de funcionários) | G2, Capterra e Gartner Peer Insights | Wappalyzer e BuiltWith (widgets de chat) |
| EMP-25 · Stack fragmentado | `has_stack_fragmentado` | Vagas (2+ ferramentas citadas) | LinkedIn (skills de funcionários) | Wappalyzer e BuiltWith | Cases públicos dos concorrentes | G2 e Gartner Peer Insights |
| EMP-26 · WhatsApp verificado | `has_whatsapp_verificado` | Site (Fale conosco) | App WhatsApp (selo no perfil) | Bio do Instagram | Reclame Aqui (canais da empresa) | Google ("nome" WhatsApp oficial) |
| EMP-27 · 4+ canais digitais | `has_4_canais_digitais` | Site (Fale conosco) | App Store e Google Play (app com atendimento) | Reclame Aqui (canais da empresa) | Perfis sociais (DM aberta) | Wappalyzer (widget de chat) |
| EMP-28 · Programa de advocacy | `has_programa_advocacy` | Site de carreiras | LinkedIn (hashtag do programa em posts de funcionários) | Glassdoor | GPTW (perfil da empresa) | Cases públicos de ferramentas de advocacy |

### Pessoa

| Critério | Campo | Fonte 1 | Fonte 2 | Fonte 3 | Fonte 4 | Fonte 5 |
|---|---|---|---|---|---|---|
| PES-01 · Título com palavra-chave | `is_titulo_alvo` | LinkedIn (perfil) | Google X-ray (site:linkedin.com/in) | Site institucional (liderança) | Apollo ou RocketReach (versão gratuita) | Agendas de eventos |
| PES-02 · Gerente ou acima | `is_gerente_ou_acima` | LinkedIn (perfil) | Google X-ray | Apollo ou RocketReach | Site institucional | Imprensa de mercado |
| PES-03 · Diretor ou acima | `is_diretor_ou_acima` | LinkedIn (perfil) | CVM (Formulário de Referência, diretores estatutários) | Site institucional (liderança) | Google X-ray | Imprensa de mercado |
| PES-04 · Área CX | `is_area_cx` | LinkedIn (perfil) | Google X-ray | Agenda do CONAREC e eventos de CX | Apollo ou RocketReach | Imprensa de CX (Consumidor Moderno) |
| PES-05 · Área Marketing | `is_area_marketing` | LinkedIn (perfil) | Google X-ray | Agenda do RD Summit e eventos de marketing | Meio & Mensagem | Apollo ou RocketReach |
| PES-06 · MarTech ou TI de CX | `is_area_martech` | LinkedIn (perfil) | Google X-ray | Vagas do time (descrevem o stack) | Apollo ou RocketReach | GitHub e comunidades técnicas |
| PES-07 · RH ou Comunicação Interna | `is_area_rh_comunicacao_interna` | LinkedIn (perfil) | Google X-ray | Agendas de eventos de RH | Apollo ou RocketReach | GPTW (porta-vozes) |
| PES-08 · Decisor econômico | `is_decisor_economico` | Derivado das fontes de PES-03 a PES-05 | | | | |
| PES-09 · Champion | `is_champion` | Derivado das fontes de PES-02 a PES-07 | | | | |
| PES-10 · Influenciador técnico | `is_influenciador_tecnico` | Derivado das fontes de PES-06 | | | | |
| PES-11 (!) · Alçada de orçamento | `has_alcada_orcamento` | Sem fonte pública | Proxy: CVM (estatutário) | Proxy: senioridade (PES-03) | Proxy: conversa | |
| PES-12 · Post sobre CX em 90 dias | `has_post_cx_90d` | LinkedIn (aba Atividade) | Google (site:linkedin.com/posts + nome) | X | YouTube e podcasts | Medium ou blog pessoal |
| PES-13 · Palestra em 12 meses | `has_palestra_12m` | Sites de eventos (CONAREC, RD Summit) | Sympla | YouTube (gravações) | LinkedIn (posts sobre a palestra) | Google |
| PES-14 · No cargo há até 12 meses | `is_novo_no_cargo_12m` | LinkedIn (data de início) | Google X-ray | Meio & Mensagem e Propmark (movimentações) | Apollo ou RocketReach | Site institucional |
| PES-15 · Ex-cliente Sprinklr | `has_ex_empresa_cliente_sprinklr` | LinkedIn (histórico profissional) | Sprinklr Customer Stories | LinkedIn (skill "Sprinklr") | Google X-ray ("Sprinklr" site:linkedin.com/in) | G2 (reviews da Sprinklr) |
| PES-16 (!) · Avaliou fornecedor em 12 meses | `has_avaliacao_fornecedor_12m` | Sem fonte pública | Proxy: reviews recentes no G2 e Gartner Peer Insights | Proxy: webinars de concorrentes | Proxy: conversa | |

---

## 2. Catálogo de fontes

### Dados abertos e governo

| Fonte | O que entrega | Esforço de extração |
|---|---|---|
| Receita Federal (Dados Abertos CNPJ) | CNAE, situação cadastral, UF, porte, filiais e quadro societário de todas as empresas | Baixo: download mensal em CSV; arquivos grandes, pedem processamento em lote |
| Receita Federal (consulta online) | Comprovante de um CNPJ por vez | Médio: tem captcha, serve só para checagem pontual |
| CVM (RAD, DFP, ITR, Formulário de Referência) | Receita, nº de empregados, marcas, diretoria estatutária e fatos relevantes de companhias abertas | Baixo: dados abertos em CSV; só cobre empresas abertas |
| Banco Central (IF.data e ranking de reclamações) | Lista de instituições autorizadas e reclamações por banco | Baixo: planilhas trimestrais |
| SUSEP | Seguradoras autorizadas | Baixo: lista pública |
| ANS | Operadoras de saúde ativas | Baixo: dados abertos |
| Anatel | Prestadoras e reclamações de telecom | Baixo: dados abertos |
| Consumidor.gov.br | Reclamações por empresa, com prazo e resolução | Baixo: dados abertos em CSV |
| Procon-SP | Cadastro anual de reclamações fundamentadas | Médio: relatório em PDF |
| CADE | Atos de concentração (fusões e aquisições) | Médio: busca por empresa no SEI |
| INPI | Marcas registradas por titular | Médio: busca manual, sem API pública |
| PNCP | Contratos de empresas públicas, inclusive software | Médio: busca por órgão e objeto |
| Planalto | Texto de leis e decretos | Baixo: leitura única |
| Diário Oficial e tribunais estaduais | Balanços de S.A. fechadas e processos de recuperação judicial | Alto: busca dispersa por estado |

### Diretórios e bases de empresas

| Fonte | O que entrega | Esforço de extração |
|---|---|---|
| Casa dos Dados | Busca de CNPJ por CNAE, UF e situação, com exportação | Baixo: filtros prontos |
| CNPJ.biz | Ficha resumida por CNPJ | Baixo: página única por empresa |
| Econodata | Faixa de funcionários e receita estimada | Médio: parte é paga; estimativas |
| Crunchbase | Matriz, subsidiárias e aquisições | Médio: limite de buscas na versão gratuita |
| Valor 1000 | Receita das maiores empresas por setor | Médio: parte atrás de paywall |
| Melhores e Maiores Exame | Receita e ranking setorial | Médio: parte atrás de paywall |
| Ranking SBVC | Maiores varejistas, com faturamento e nº de lojas | Médio: relatório anual |
| GPTW | Perfil de empresas certificadas | Baixo: página pública |
| Glassdoor | Porte, avaliações de funcionários e benefícios | Médio: pede login após algumas páginas |
| Jusbrasil e Escavador | Processos judiciais, incluindo recuperação judicial | Médio: busca por nome; resultados completos são pagos |
| Apollo e RocketReach | Cargo, área e senioridade de pessoas | Médio: versão gratuita limitada |

### LinkedIn

| Fonte | O que entrega | Esforço de extração |
|---|---|---|
| Página da empresa | Nº de funcionários, setor, locais e páginas vitrine | Médio: leitura manual por conta |
| Perfis de pessoas | Cargo, área, data de início e histórico | Alto: exige login; scraping viola os termos de uso |
| Atividade e posts | Publicações e comentários recentes | Alto: leitura manual |
| LinkedIn Vagas | Vagas abertas com requisitos e ferramentas citadas | Médio: busca por empresa e palavra-chave |
| Google X-ray (site:linkedin.com/in) | Perfis públicos indexados, sem login | Médio: consultas booleanas, resultados incompletos |

### Google

| Fonte | O que entrega | Esforço de extração |
|---|---|---|
| Google Busca e Notícias | Movimentações, aquisições e campanhas | Médio: leitura e checagem |
| Google Maps | Lojas físicas e perfis de unidade | Médio: contagem por região |
| Google Trends | Picos de interesse por termo, como sinal de crise | Baixo: gráfico pronto |
| Google Ads Transparency Center | Anúncios ativos por anunciante | Baixo: busca por nome |

### Redes sociais e comunidades

| Fonte | O que entrega | Esforço de extração |
|---|---|---|
| Instagram, TikTok, Facebook, X e YouTube | Perfis oficiais, seguidores, canais de DM e conteúdo | Médio: verificação manual por marca |
| Meta Ad Library | Páginas anunciantes e campanhas ativas | Baixo: busca pública, sem login |
| Social Blade | Histórico de seguidores | Baixo: página por perfil |
| HypeAuditor | Seguidores e engajamento | Médio: versão gratuita limitada |
| Reddit | Reclamações espontâneas e relatos de uso de ferramentas | Médio: busca por marca ou ferramenta, leitura manual |
| WhatsApp | Selo de conta oficial | Médio: checagem manual pelo app |

### Sites, mídia e software

| Fonte | O que entrega | Esforço de extração |
|---|---|---|
| Site institucional | Marcas, canais de atendimento, países e liderança | Médio: leitura por empresa |
| Site de carreiras e Gupy | Vagas, programas de embaixadores e stack citado | Médio: busca por palavra-chave |
| Indeed e Catho | Vagas complementares | Médio: busca por empresa |
| Reclame Aqui | Nº de reclamações, nota por período e canais da empresa | Médio: página pública por empresa |
| Meio & Mensagem e Propmark | Contas de agências, movimentações e campanhas | Médio: parte atrás de paywall |
| Valor Econômico | M&A, resultados e recuperação judicial | Médio: paywall |
| Consumidor Moderno | Notícias e porta-vozes de CX | Baixo: página pública |
| Effie Brasil e Cannes Lions | Fichas técnicas de campanhas com agências | Médio: busca por anunciante |
| Sympla e sites de eventos (CONAREC, RD Summit) | Palestrantes por evento | Médio: leitura de agendas |
| App Store e Google Play | Apps com atendimento embutido | Baixo: busca pública |
| Wappalyzer e BuiltWith | Widgets de chat e tecnologias no site | Baixo: extensão ou consulta gratuita |
| G2, Capterra e Gartner Peer Insights | Reviews de ferramentas, com cargo e porte do revisor | Médio: empresa do revisor nem sempre aparece |
| Sprinklr Customer Stories e 10-K | Clientes atuais da Sprinklr | Baixo: páginas públicas |
| Cases dos concorrentes (seção 3) | Contas que usam ferramenta concorrente | Médio: leitura por fornecedor |

---

## 3. Concorrentes

Os três que você citou (Genesys, NICE e Buzzmonitor) cobrem contact center e social no Brasil. Os outros sete foram escolhidos por disputarem as mesmas suítes da Sprinklr (Service, Social, Insights ou Marketing) em contas enterprise e por terem presença relevante no Brasil.

| # | Concorrente | Disputa com | Por que entra | Página de clientes | Status do link |
|---|---|---|---|---|---|
| 1 | Genesys | Service (contact center e voz) | Citado por você | https://www.genesys.com/customer-stories | Confirmado |
| 2 | NICE (CXone Mpower) | Service (contact center e voz) | Citado por você | https://www.nice.com/es/customer-stories | Confirmado na versão em espanhol |
| 3 | Buzzmonitor | Social e Insights | Citado por você | https://conteudo.buzzmonitor.com.br/compare-platforms | Sem página de clientes dedicada; esta página tem o bloco de logos de clientes |
| 4 | Blip | Service (conversacional e WhatsApp) | Maior plataforma conversacional brasileira, forte em bancos, varejo e telecom | https://www.blip.ai/?p=39904 | Confirmado (página "Blip Cases") |
| 5 | Zenvia | Service e Marketing (mensageria) | Plataforma brasileira de CX com base enterprise local | https://zenvia.com/casos-de-sucesso/ | Página-mãe deduzida a partir de um case confirmado |
| 6 | Zendesk | Service (atendimento digital) | Muito presente em varejo e tecnologia | https://www.zendesk.com/customer/ | Confirmado em versões regionais (/au/ e /sg/) |
| 7 | Salesforce (Service e Marketing Cloud) | Service e Marketing | Concorre na consolidação de CX em contas que já usam o CRM | https://www.salesforce.com/customer-stories/ | Confirmado em versões regionais (/ca/, /au/, /it/) |
| 8 | Hootsuite (inclui Talkwalker) | Social e Insights | Social e listening enterprise, com advocacy | https://www.hootsuite.com/customers | Confirmado |
| 9 | Brandwatch | Insights e Social | Concorrente direto em listening | https://www.casestudies.com/company/brandwatch | Página oficial não confirmada; link de agregador |
| 10 | Emplifi | Social, Insights e Service | Suíte unificada mais parecida com a Sprinklr; tem case no Brasil | https://www.casestudies.com/vendor/emplifi | Página oficial não confirmada; link de agregador |

### Post de maior engajamento (!)

Não consegui obter o post de maior engajamento de nenhum dos 10. LinkedIn, Instagram e X exigem login para listar posts e nenhum deles ordena publicamente por engajamento, então qualquer post que eu indicasse aqui seria palpite. Para preencher:

1. **YouTube:** no canal de cada concorrente, a aba Vídeos tem o filtro "Populares". É o único ordenamento público por engajamento.
2. **LinkedIn:** role a página da empresa até 6 meses atrás e anote reações e comentários dos posts. Leva cerca de 15 minutos por concorrente.
3. **Instagram e TikTok:** HypeAuditor ou Social Blade mostram os posts com mais interação.

### Como usar os cases dos concorrentes

Cada empresa listada nas páginas acima com operação no Brasil é uma conta com EMP-24 = sim. Cruze essas listas com os critérios eliminatórios do ICP: o resultado é uma lista de deslocamento (displacement) já qualificada. Priorize contas que aparecem em 2 ou mais concorrentes ao mesmo tempo (por exemplo, Genesys no contact center e Buzzmonitor no social), porque isso também torna EMP-25 (stack fragmentado) = sim, que é o argumento central da plataforma unificada.
