# Fontes públicas do ICP: Sprinklr no Brasil

Base: `filtros.md` (EMP-01 a EMP-35, PES-01 a PES-17 e campos calculados). Para cada critério, as 5 melhores fontes públicas em ordem de prioridade: a primeira é a que mais resolve com menos esforço. Critérios com (!) não têm fonte pública que responda direto; as fontes listadas dão só indício e o valor final vem da conversa com a conta.

Esforço de extração:
- **Baixo:** dado aberto, CSV, API ou uma página única por empresa.
- **Médio:** busca manual por empresa ou raspagem simples.
- **Alto:** exige login, tem anti-raspagem ou depende de julgamento humano.

## 1. Cinco fontes por critério

### Empresa

| Critério | Campo | Fontes (1 = melhor) |
|---|---|---|
| EMP-01 · CNAE em setor-alvo | `is_cnae_setor_alvo` | 1. Receita Federal, Dados Abertos do CNPJ · 2. Casa dos Dados · 3. CNPJ.biz · 4. Econodata · 5. Página da empresa no LinkedIn (setor) |
| EMP-02 · Serviço financeiro ao consumidor | `has_servico_financeiro_consumidor` | 1. Banco Central, instituições autorizadas · 2. Site institucional (cartão, conta, crédito) · 3. CVM, Formulário de Referência · 4. App Store e Google Play (apps de banco e cartão) · 5. Google Notícias |
| EMP-03 · Sujeita ao Decreto do SAC | `is_sujeita_decreto_sac` | 1. Planalto, Decreto 11.034/2022 · 2. Receita Federal (CNAE para cruzar) · 3. Sites de Anatel, ANS, ANEEL e Banco Central (setor regulado) · 4. Consumidor.gov.br (empresa cadastrada) · 5. Site institucional (SAC 24h publicado) |
| EMP-04 · 1.000+ funcionários | `has_1000_funcionarios` | 1. Página da empresa no LinkedIn · 2. CVM, Formulário de Referência · 3. Glassdoor · 4. Econodata · 5. GPTW (ranking por porte) |
| EMP-05 · 10.000+ funcionários | `has_10000_funcionarios` | 1. Página da empresa no LinkedIn · 2. CVM, Formulário de Referência · 3. Relatório anual ou de sustentabilidade · 4. Glassdoor · 5. GPTW |
| EMP-06 · Receita ≥ R$ 5 bi | `has_receita_5bi` | 1. CVM, Dados Abertos (DFP) · 2. Valor 1000 · 3. Melhores e Maiores Exame · 4. Ranking SBVC (varejo) · 5. Banco Central, IF.data (bancos) |
| EMP-07 · 10 milhões+ de clientes | `has_10m_clientes` | 1. Banco Central, ranking de reclamações (traz nº de clientes) · 2. Releases de resultados (CVM e RI) · 3. Google Play (faixa de downloads) · 4. Site institucional · 5. Google Notícias |
| EMP-08 · CNPJ ativo com sede no Brasil | `is_cnpj_ativo_br` | 1. Receita Federal, Dados Abertos do CNPJ · 2. Consulta CNPJ da Receita (comprovante) · 3. Casa dos Dados · 4. CNPJ.biz · 5. Econodata |
| EMP-09 · Presente em 15+ estados | `has_15_ufs` | 1. Receita Federal (UF das filiais) · 2. Google Maps (lojas e agências) · 3. Site institucional (encontre uma loja) · 4. Banco Central (agências por UF) · 5. Releases de resultados |
| EMP-10 · Opera em outros países da América Latina | `has_operacao_latam` | 1. CVM, Formulário de Referência · 2. Página da empresa no LinkedIn (locais) · 3. Relatório anual · 4. Site institucional (seletor de país) · 5. Crunchbase |
| EMP-11 · Vende para consumidor final | `is_b2c_ou_b2b2c` | 1. Site institucional · 2. Receita Federal (CNAE) · 3. App Store e Google Play · 4. Reclame Aqui (empresa cadastrada com volume) · 5. Instagram oficial |
| EMP-12 · 3+ marcas comerciais | `has_3_marcas` | 1. INPI, busca por titular · 2. Relatório anual · 3. Site institucional (nossas marcas) · 4. Página da empresa no LinkedIn (páginas afiliadas) · 5. Reclame Aqui (várias páginas sob o mesmo grupo) |
| EMP-13 · Companhia aberta | `is_companhia_aberta` | 1. CVM, cadastro de companhias abertas · 2. B3, empresas listadas · 3. Site de RI · 4. Google Finance · 5. Valor Econômico |
| EMP-14 · 100+ pontos físicos | `has_100_pontos_fisicos` | 1. Receita Federal (nº de filiais por CNPJ raiz) · 2. Banco Central (agências por instituição) · 3. Releases de resultados · 4. Google Maps · 5. Ranking SBVC (nº de lojas) |
| EMP-15 · Marketplace ou ecossistema de parceiros | `has_marketplace` | 1. Site institucional (venda conosco) · 2. Releases de resultados (GMV 3P) · 3. LinkedIn Vagas (vagas de seller) · 4. Google Notícias · 5. Ranking SBVC |
| EMP-16 · App com atendimento | `has_app_atendimento` | 1. Google Play (descrição e reviews) · 2. App Store · 3. Página "Fale conosco" do site · 4. Reclame Aqui (canal da reclamação) · 5. YouTube (tutoriais do app) |
| EMP-17 · 10+ perfis sociais ativos | `has_10_perfis_sociais` | 1. Instagram · 2. Página da empresa no LinkedIn (páginas afiliadas) · 3. Facebook · 4. TikTok · 5. Site institucional (rodapé com links sociais) |
| EMP-18 · 1 milhão+ de seguidores | `has_1m_seguidores` | 1. Instagram · 2. Social Blade · 3. YouTube · 4. TikTok · 5. Facebook |
| EMP-19 · 1.000+ reclamações em 12 meses | `has_1000_reclamacoes_12m` | 1. Reclame Aqui · 2. Consumidor.gov.br, dados abertos · 3. Banco Central, ranking de reclamações · 4. Procon-SP, cadastro de reclamações · 5. Anatel e ANS (índices setoriais) |
| EMP-20 · Empresa privada | `is_empresa_privada` | 1. Receita Federal (natureza jurídica) · 2. CVM, Formulário de Referência (controle) · 3. Site de RI · 4. Casa dos Dados · 5. Wikipedia (estrutura acionária, só como pista) |
| EMP-21 · Fora de recuperação judicial | `is_sem_recuperacao_judicial` | 1. CVM, fatos relevantes · 2. Jusbrasil · 3. Escavador · 4. Consulta processual dos tribunais estaduais · 5. Google Notícias |
| EMP-22 · Não é cliente Sprinklr | `is_nao_cliente_sprinklr` | 1. Sprinklr Customer Stories · 2. LinkedIn Vagas (exigem Sprinklr) · 3. Google X-ray (`site:linkedin.com/in "Sprinklr" "<empresa>"`) · 4. Sprinklr 10-K e releases · 5. Gartner Peer Insights e G2 (reviews por empresa) |
| EMP-23 · Vaga em CX, social ou insights em 90 dias | `has_vaga_cx_90d` | 1. LinkedIn Vagas · 2. Gupy · 3. Site de carreiras · 4. Indeed · 5. Catho |
| EMP-24 · Novo líder em até 6 meses | `has_novo_lider_cx_6m` | 1. Perfis do LinkedIn (data de início) · 2. Atividade do LinkedIn (posts "novo desafio") · 3. Meio & Mensagem, movimentações · 4. Consumidor Moderno · 5. Google X-ray com filtro de data |
| EMP-25 · M&A ou nova marca em 12 meses | `has_ma_ou_marca_12m` | 1. CVM, fatos relevantes · 2. CADE, atos de concentração · 3. INPI, depósitos recentes · 4. Valor Econômico · 5. Crunchbase |
| EMP-26 · Reputação em queda | `is_reputacao_em_queda` | 1. Reclame Aqui (nota 6 meses contra 12 meses) · 2. Banco Central, ranking trimestral · 3. Consumidor.gov.br (série histórica) · 4. Google Trends (termo "<marca> reclamação") · 5. Reddit (r/brasil, r/investimentos, r/conselhodecarreira) |
| EMP-27 · IA generativa no atendimento em 12 meses | `has_ia_atendimento_12m` | 1. Releases e apresentações de resultados · 2. Google Notícias · 3. Consumidor Moderno · 4. Cases de fornecedores (seção Concorrentes) · 5. Posts de executivos no LinkedIn |
| EMP-28 (!) · Contrato vence em até 9 meses | `has_contrato_vencendo_9m` | Só indícios: 1. Data do case público do concorrente (contratos de 3 anos) · 2. PNCP (só estatais, fora do ICP) · 3. Vagas de "implantação" ou "migração" · 4. Posts de executivos sobre RFP · 5. Conversa com a conta |
| EMP-29 · Usa ferramenta concorrente | `has_ferramenta_concorrente` | 1. Páginas de clientes dos concorrentes (seção 3) · 2. LinkedIn Vagas (requisitos) · 3. Google X-ray em perfis (skills) · 4. Wappalyzer ou BuiltWith · 5. G2 e Gartner Peer Insights |
| EMP-30 · Stack fragmentado (2+ ferramentas) | `has_stack_fragmentado` | 1. LinkedIn Vagas (várias ferramentas no requisito) · 2. Wappalyzer ou BuiltWith · 3. Google X-ray em perfis · 4. Páginas de clientes dos concorrentes · 5. BuiltWith, histórico de tecnologias |
| EMP-31 · WhatsApp Business verificado | `has_whatsapp_verificado` | 1. WhatsApp (selo no número oficial) · 2. Site institucional (número publicado) · 3. Reclame Aqui (canais da empresa) · 4. Instagram (link na bio) · 5. Cases de Blip e Zenvia |
| EMP-32 · 4+ canais digitais de atendimento | `has_4_canais_digitais` | 1. Página "Fale conosco" · 2. App (menu de ajuda) · 3. Reclame Aqui (canais) · 4. Instagram e X (respondem DM e menção?) · 5. Wappalyzer (widget de chat) |
| EMP-33 · Contact center de voz | `has_contact_center_voz` | 1. Site (SAC telefônico) · 2. LinkedIn Vagas (operador, supervisor) · 3. Gupy · 4. Glassdoor (avaliações de operadores) · 5. Consumidor.gov.br |
| EMP-34 · Atendimento terceirizado em BPO | `has_bpo_atendimento` | 1. Cases e releases dos BPOs (Tahto, Atento, AeC, Teleperformance, Algar Tech) · 2. Consumidor Moderno · 3. Perfis do LinkedIn de BPOs ("operação <cliente>") · 4. LinkedIn Vagas dos BPOs · 5. Glassdoor dos BPOs |
| EMP-35 · Ferramenta pontual de WFM ou qualidade | `has_wfm_qa_pontual` | 1. LinkedIn Vagas (planejamento e qualidade) · 2. Google X-ray em perfis (Verint, NICE IEX, Calabrio) · 3. Gupy · 4. Cases de NICE e Genesys · 5. G2 |

### Pessoa

| Critério | Campo | Fontes (1 = melhor) |
|---|---|---|
| PES-01 · Título com palavra-chave-alvo | `is_titulo_alvo` | 1. Perfil público do LinkedIn · 2. Google X-ray · 3. Apollo · 4. RocketReach · 5. Agendas de eventos (cargo do palestrante) |
| PES-02 · Gerente ou acima | `is_gerente_ou_acima` | 1. Perfil público do LinkedIn · 2. Google X-ray · 3. Apollo · 4. RocketReach · 5. Site institucional (página de liderança) |
| PES-03 · Diretor ou acima | `is_diretor_ou_acima` | 1. Perfil público do LinkedIn · 2. CVM, Formulário de Referência (estatutários) · 3. Site de RI (diretoria) · 4. Apollo · 5. Google Notícias (porta-voz) |
| PES-04 · Área CX, SAC ou Ouvidoria | `is_area_cx` | 1. Perfil público do LinkedIn · 2. Banco Central, ouvidores cadastrados · 3. Google X-ray · 4. Consumidor Moderno (entrevistas) · 5. Agenda do CONAREC |
| PES-05 · Área Marketing, Social, Marca ou Insights | `is_area_marketing` | 1. Perfil público do LinkedIn · 2. Meio & Mensagem · 3. Propmark · 4. Effie e Cannes (fichas técnicas) · 5. Google X-ray |
| PES-06 · MarTech, dados ou TI de CX | `is_area_martech` | 1. Perfil público do LinkedIn · 2. Google X-ray · 3. Agenda da Febraban Tech · 4. GitHub e Medium (posts técnicos) · 5. Apollo |
| PES-07 · Marketplace ou Seller | `is_area_marketplace` | 1. Perfil público do LinkedIn · 2. Google X-ray · 3. Agenda do Latam Retail Show · 4. E-Commerce Brasil (entrevistas) · 5. Apollo |
| PES-17 · Operações, Planejamento ou Qualidade | `is_area_operacoes_cx` | 1. Perfil público do LinkedIn · 2. Google X-ray · 3. Agenda do CONAREC · 4. Comunidades de WFM no LinkedIn · 5. Apollo |
| PES-08 · Provável decisor econômico | `is_decisor_economico` | Derivado de PES-03, PES-04 e PES-05 (sem fonte própria) |
| PES-09 · Provável champion | `is_champion` | Derivado de PES-02, 03, 04, 05, 07 e 17 (sem fonte própria) |
| PES-10 · Influenciador técnico | `is_influenciador_tecnico` | Derivado de PES-06 (sem fonte própria) |
| PES-11 (!) · Tem alçada de orçamento | `has_alcada_orcamento` | Só indícios: 1. CVM, diretor estatutário · 2. Posts sobre "contratamos" ou "implantamos" · 3. Cases de fornecedores que citam a pessoa · 4. Cargo e tamanho do time no LinkedIn · 5. Conversa com a conta |
| PES-12 · Publicou sobre CX ou social em 90 dias | `has_post_cx_90d` | 1. Atividade pública no LinkedIn · 2. Google (`site:linkedin.com/posts "<nome>"`) · 3. X · 4. Medium e newsletters · 5. YouTube e podcasts |
| PES-13 · Palestrou em evento em 12 meses | `has_palestra_12m` | 1. Agenda do CONAREC · 2. Agenda da Febraban Tech · 3. Latam Retail Show e RD Summit · 4. Sympla (eventos menores) · 5. YouTube (gravações) |
| PES-14 · No cargo há até 12 meses | `is_novo_no_cargo_12m` | 1. Perfil público do LinkedIn · 2. Atividade do LinkedIn (post de novo cargo) · 3. Meio & Mensagem, movimentações · 4. Google Notícias · 5. Apollo (data de início) |
| PES-15 · Ex-Itaú, ex-Magalu ou ex-cliente Sprinklr | `has_ex_empresa_cliente_sprinklr` | 1. Histórico no LinkedIn · 2. Sprinklr Customer Stories (lista de clientes para cruzar) · 3. Google X-ray (`"ex-Itaú" OR "Itaú Unibanco"`) · 4. Apollo (empresas anteriores) · 5. RocketReach |
| PES-16 (!) · Avaliou fornecedor em 12 meses | `has_avaliacao_fornecedor_12m` | Só indícios: 1. Reviews no Gartner Peer Insights e G2 · 2. Posts sobre "estamos avaliando" · 3. Webinars de concorrentes com a pessoa · 4. Vagas de implantação na empresa · 5. Conversa com a conta |

### Campos calculados

| Campo | Origem |
|---|---|
| `is_empresa_elegivel` | EMP-01, 04, 08, 11, 21, 22 |
| `anchor_case` | EMP-01 (`itau` para financeiro, `magalu` para varejo e consumo) |
| `score_empresa` | Soma dos EMP que pontuam |
| `tier_conta` | `is_empresa_elegivel` + `score_empresa` |
| `is_pessoa_elegivel` | PES-01, PES-02 e (PES-04, 05, 06, 07 ou 17) |

## 2. Catálogo de fontes

| Fonte | O que entrega | Esforço |
|---|---|---|
| Receita Federal, Dados Abertos do CNPJ | CNAE, situação, natureza jurídica, filiais e UF de todo CNPJ | Baixo (CSV mensal, arquivo grande) |
| Consulta CNPJ da Receita | Comprovante de uma empresa | Médio (captcha) |
| Casa dos Dados · CNPJ.biz | Mesmos dados da Receita com busca por filtro | Baixo |
| Econodata | Porte estimado, funcionários, filiais | Médio (limite gratuito) |
| CVM, Dados Abertos (DFP, ITR, cadastro) | Receita, lista de abertas, controle | Baixo (CSV) |
| CVM, Formulário de Referência | Funcionários, países, diretores estatutários, marcas | Médio (PDF por empresa) |
| CVM, fatos relevantes | M&A, recuperação judicial, mudanças de diretoria | Baixo |
| B3 · Site de RI | Listagem, releases, apresentações de resultados | Médio |
| Banco Central, instituições autorizadas · IF.data | Quem é financeira, porte, agências | Baixo |
| Banco Central, ranking de reclamações | Reclamações e nº de clientes por instituição, trimestral | Baixo |
| Banco Central, ouvidores cadastrados | Nome do ouvidor de cada instituição | Baixo |
| Anatel · ANS · ANEEL | Índices de reclamação e regulação setorial | Baixo |
| Consumidor.gov.br, dados abertos | Reclamações por empresa, série histórica | Baixo (CSV) |
| Procon-SP | Cadastro de reclamações fundamentadas | Médio |
| Planalto | Texto do Decreto 11.034/2022 | Baixo |
| CADE | Atos de concentração | Médio |
| INPI | Marcas por titular e depósitos recentes | Médio (busca sem API) |
| PNCP | Contratos públicos (só estatais) | Baixo |
| Jusbrasil · Escavador · tribunais | Processos, recuperação judicial | Médio |
| Valor 1000 · Melhores e Maiores Exame · Ranking SBVC | Receita, ranking, nº de lojas | Médio (parte pago) |
| GPTW · Glassdoor | Porte, avaliações de funcionários (operação de voz) | Médio |
| Crunchbase | Aquisições, países, investimentos | Médio (limite gratuito) |
| Apollo · RocketReach | Cargo, área, data de início, histórico | Médio (créditos) |
| Página da empresa no LinkedIn | Funcionários, locais, páginas afiliadas | Médio |
| Perfil público do LinkedIn | Cargo, área, senioridade, tempo no cargo, histórico | Alto (login e anti-raspagem) |
| Atividade do LinkedIn | Posts recentes, temas, troca de emprego | Alto |
| LinkedIn Vagas | Vagas abertas e ferramentas exigidas | Médio |
| Google X-ray | Perfis e posts do LinkedIn sem login | Médio |
| Google Busca · Notícias · Trends | Notícias, movimentos, interesse por termo | Baixo |
| Google Maps | Lojas e agências por UF | Médio |
| Reddit | Reclamação espontânea e percepção de marca | Médio |
| Instagram · Facebook · TikTok · X · YouTube | Perfis, seguidores, se responde DM e menção | Médio (login parcial) |
| Social Blade | Seguidores e crescimento | Baixo |
| WhatsApp | Selo verificado do número oficial | Médio (manual, número a número) |
| Site institucional (Fale conosco, marcas, carreiras) | Canais, marcas, marketplace, SAC | Médio |
| Gupy · Indeed · Catho | Vagas de atendimento, planejamento e qualidade | Médio |
| Reclame Aqui | Volume, nota, reputação 6 e 12 meses, canais | Médio (anti-raspagem) |
| Meio & Mensagem · Propmark · Consumidor Moderno · Valor Econômico | Movimentações, cases, projetos de IA | Médio (paywall parcial) |
| Effie · Cannes | Fichas técnicas com nomes de marketing | Médio |
| Agendas de CONAREC, Febraban Tech, Latam Retail Show, RD Summit · Sympla | Palestrantes e cargos | Médio |
| App Store · Google Play | App, downloads, reviews citando atendimento | Baixo |
| Wappalyzer · BuiltWith | Widgets de chat e ferramentas no site | Baixo (extensão) |
| G2 · Capterra · Gartner Peer Insights | Reviews por empresa e ferramenta | Médio |
| Sprinklr Customer Stories · 10-K | Clientes Sprinklr para excluir e cruzar | Baixo |
| Páginas de clientes dos concorrentes | Quem usa qual ferramenta concorrente | Médio |

## 3. Concorrentes

Os três que você citou primeiro, mais sete que disputam as mesmas contas no Brasil. Uso principal: preencher EMP-29 e EMP-30 cruzando as páginas de clientes com a lista de contas.

| # | Concorrente | Disputa com a suíte | Página de clientes | Status do link |
|---|---|---|---|---|
| 1 | Genesys (Genesys Cloud) | Service: contact center, voz, WFM | https://www.genesys.com/customer-stories | Confirmado |
| 2 | NICE (CXone Mpower) | Service: contact center, WFM, qualidade | https://www.nice.com/customer-stories | Página global; confirmada a versão https://www.nice.com/es/customer-stories |
| 3 | Blip | Service: conversacional e WhatsApp; Insights (ex-Stilingue) | https://www.blip.ai/?p=39904 | Confirmado (página "Blip Cases") |
| 4 | Zenvia | Service e Marketing: mensageria e atendimento | https://zenvia.com/casos-de-sucesso/ | Página-mãe; cases individuais confirmados no mesmo caminho |
| 5 | Zendesk | Service: atendimento digital e ticketing | https://www.zendesk.com/customer/ | Confirmado em versões regionais |
| 6 | Salesforce (Service e Marketing Cloud) | Service e Marketing, onde o CRM já existe | https://www.salesforce.com/customer-stories/ | Confirmado em versões regionais |
| 7 | Buzzmonitor | Social e Insights | https://conteudo.buzzmonitor.com.br/compare-platforms | Sem página de clientes; esta tem o bloco de logos |
| 8 | Hootsuite (inclui Talkwalker) | Social e Insights | https://www.hootsuite.com/customers | Confirmado |
| 9 | Brandwatch | Insights e Social | https://www.casestudies.com/company/brandwatch | Página oficial não confirmada; agregador |
| 10 | Emplifi | Social, Insights e Service | https://www.casestudies.com/vendor/emplifi | Página oficial não confirmada; agregador |

### Post de maior engajamento

LinkedIn, Instagram e X não mostram ranking público de posts e exigem login para ver reações em volume, então nenhum "post de maior engajamento" pode ser afirmado só com busca aberta. O que achei:

| Concorrente | Post ou peça de maior alcance encontrada | Status |
|---|---|---|
| Blip | Campanha "Tudo em um Blip" com Fernanda Souza ([cobertura](https://marcaspelomundo.com.br/anunciantes/fernanda-souza-protagoniza-nova-campanha-tudo-em-um-blip/)) | (!) Maior peça de mídia identificada; engajamento não verificado |
| Genesys | Cobertura do Xperience, evento anual ([página](https://www.genesys.com/explore/xperience-live)) | (!) Candidato, não verificado |
| NICE, Zenvia, Zendesk, Salesforce, Buzzmonitor, Hootsuite, Brandwatch, Emplifi | Não encontrado em fonte aberta | (!) |

**Como confirmar (30 minutos por concorrente):**
1. **LinkedIn:** raspar os últimos 50 posts da página da empresa com um ator do Apify (`maxItems: 50`) e ordenar por reações + comentários. Custo por item; confirme comigo o volume antes de rodar.
2. **YouTube:** aba Vídeos do canal, filtro "Populares". Dado público e confiável.
3. **Instagram:** Social Blade ou HypeAuditor para os posts de maior engajamento.
4. Registre aqui o link, a data e o número de reações, e repita a cada trimestre.

O que observar no post vencedor: o ângulo (IA, custo, case de cliente brasileiro), o formato e quem comentou. Quem comenta em post de concorrente é sinal para EMP-29 e para PES-12.

## Cuidados

- Vivo e Telefônica não entram em nenhuma lista, nem como cliente de concorrente.
- Dados de pessoas raspados ficam em `signals/`, fora do git.
- Respeite os termos de uso de LinkedIn e Reclame Aqui: prefira consulta manual ou atores com limite de itens.
