# Filtros do ICP: Sprinklr no Brasil

Âncoras: Itaú Unibanco e Magazine Luiza. Cada campo guarda `true` ou `false`. Critérios sem fonte pública estão marcados com (!) e só são preenchidos depois de conversa com a conta.

## Empresa

| Critério | Campo | Fonte pública |
|---|---|---|
| EMP-01 · CNAE em setor-alvo | `is_cnae_setor_alvo` | Receita Federal, Dados Abertos do CNPJ (CNAE principal) |
| EMP-02 · Serviço financeiro ao consumidor | `has_servico_financeiro_consumidor` | Banco Central (instituições autorizadas, inclusive financeiras de varejistas); site da empresa |
| EMP-03 · Sujeita ao Decreto do SAC | `is_sujeita_decreto_sac` | Texto do Decreto 11.034/2022 (planalto.gov.br) cruzado com o CNAE |
| EMP-04 · 1.000+ funcionários | `has_1000_funcionarios` | Página da empresa no LinkedIn; CVM, Formulário de Referência |
| EMP-05 · 10.000+ funcionários | `has_10000_funcionarios` | Página da empresa no LinkedIn; CVM, Formulário de Referência |
| EMP-06 · Receita ≥ R$ 5 bi | `has_receita_5bi` | CVM, Dados Abertos (DFP) para abertas; rankings Valor 1000 e Melhores e Maiores Exame |
| EMP-07 · 10 milhões+ de clientes ou usuários | `has_10m_clientes` | Banco Central (ranking de reclamações, que traz nº de clientes); releases de resultados (CVM) |
| EMP-08 · CNPJ ativo com sede no Brasil | `is_cnpj_ativo_br` | Receita Federal, Dados Abertos do CNPJ (situação cadastral) |
| EMP-09 · Presente em 15+ estados | `has_15_ufs` | Receita Federal, Dados Abertos do CNPJ (UF das filiais) |
| EMP-10 · Opera em outros países da América Latina | `has_operacao_latam` | Relatório anual e Formulário de Referência (CVM); página do LinkedIn (locais) |
| EMP-11 · Vende para consumidor final | `is_b2c_ou_b2b2c` | Site institucional; CNAE |
| EMP-12 · 3+ marcas comerciais | `has_3_marcas` | INPI, busca de marcas por titular; relatório anual; site |
| EMP-13 · Companhia aberta | `is_companhia_aberta` | CVM (cadastro de companhias abertas); B3 |
| EMP-14 · 100+ pontos físicos | `has_100_pontos_fisicos` | Receita Federal (nº de filiais por CNPJ raiz); Banco Central (agências por instituição); releases de resultados |
| EMP-15 · Marketplace ou ecossistema de parceiros | `has_marketplace` | Site da empresa (página "venda conosco" ou de parceiros); releases de resultados |
| EMP-16 · App com atendimento | `has_app_atendimento` | App Store e Google Play |
| EMP-17 · 10+ perfis sociais ativos | `has_10_perfis_sociais` | Perfis públicos em Instagram, Facebook, X, TikTok, LinkedIn e YouTube |
| EMP-18 · 1 milhão+ de seguidores | `has_1m_seguidores` | Contadores públicos dos perfis oficiais |
| EMP-19 · 1.000+ reclamações em 12 meses | `has_1000_reclamacoes_12m` | Reclame Aqui; Consumidor.gov.br (dados abertos); Banco Central (ranking de reclamações) |
| EMP-20 · Empresa privada | `is_empresa_privada` | Receita Federal (natureza jurídica) |
| EMP-21 · Fora de recuperação judicial | `is_sem_recuperacao_judicial` | Consulta processual dos tribunais estaduais; CVM (fatos relevantes); imprensa |
| EMP-22 · Não é cliente Sprinklr | `is_nao_cliente_sprinklr` | Sprinklr Customer Stories; vagas e perfis do LinkedIn que citam Sprinklr |
| EMP-23 · Vaga em CX, social ou insights em 90 dias | `has_vaga_cx_90d` | LinkedIn Vagas; Gupy; site de carreiras |
| EMP-24 · Novo líder em até 6 meses | `has_novo_lider_cx_6m` | Perfis do LinkedIn (data de início); Meio & Mensagem (movimentações) |
| EMP-25 · M&A ou nova marca em 12 meses | `has_ma_ou_marca_12m` | CVM (fatos relevantes); CADE (atos de concentração); INPI |
| EMP-26 · Reputação em queda | `is_reputacao_em_queda` | Reclame Aqui (nota de 6 meses contra nota de 12 meses) |
| EMP-27 · IA generativa no atendimento em 12 meses | `has_ia_atendimento_12m` | Releases e relatórios de resultados (CVM); imprensa |
| EMP-28 (!) · Contrato atual vence em até 9 meses | `has_contrato_vencendo_9m` | Sem fonte pública |
| EMP-29 · Usa ferramenta concorrente | `has_ferramenta_concorrente` | Requisitos de vagas; skills em perfis do LinkedIn; cases públicos dos concorrentes |
| EMP-30 · Stack fragmentado (2+ ferramentas) | `has_stack_fragmentado` | Mesmas fontes de EMP-29; Wappalyzer ou BuiltWith para widgets no site |
| EMP-31 · WhatsApp Business verificado | `has_whatsapp_verificado` | Número oficial do site, com selo visível no WhatsApp |
| EMP-32 · 4+ canais digitais de atendimento | `has_4_canais_digitais` | Página "Fale conosco" do site e do app |
| EMP-33 · Contact center de voz | `has_contact_center_voz` | Site (SAC telefônico); LinkedIn Vagas e Gupy (vagas de operador, supervisor e planejamento) |
| EMP-34 · Atendimento terceirizado em BPO | `has_bpo_atendimento` | Cases e releases dos BPOs (Tahto, Atento, AeC, Teleperformance, Algar Tech); imprensa setorial (Consumidor Moderno) |
| EMP-35 · Ferramenta pontual de WFM ou qualidade | `has_wfm_qa_pontual` | Requisitos de vagas de planejamento e qualidade; skills em perfis do LinkedIn |

## Pessoa

| Critério | Campo | Fonte pública |
|---|---|---|
| PES-02 · Gerente ou acima | `is_gerente_ou_acima` | Perfil público do LinkedIn |
| PES-03 · Diretor ou acima | `is_diretor_ou_acima` | Perfil público do LinkedIn; CVM, Formulário de Referência (diretores estatutários) |
| PES-04 · Área CX, Atendimento, SAC ou Ouvidoria | `is_area_cx` | Perfil público do LinkedIn; Banco Central (ouvidores cadastrados) |
| PES-05 · Área Marketing, Social, Marca ou Insights | `is_area_marketing` | Perfil público do LinkedIn |
| PES-06 · MarTech, dados ou TI de CX | `is_area_martech` | Perfil público do LinkedIn |
| PES-07 · Marketplace ou Experiência do Seller | `is_area_marketplace` | Perfil público do LinkedIn |
| PES-17 · Operações de Atendimento, Planejamento ou Qualidade | `is_area_operacoes_cx` | Perfil público do LinkedIn |
| PES-08 · Provável decisor econômico | `is_decisor_economico` | Derivado de PES-03, PES-04 e PES-05 |
| PES-09 · Provável champion | `is_champion` | Derivado de PES-02, PES-03, PES-04, PES-05, PES-07 e PES-17 |
| PES-10 · Influenciador técnico | `is_influenciador_tecnico` | Derivado de PES-06 |
| PES-11 (!) · Tem alçada de orçamento | `has_alcada_orcamento` | Sem fonte pública |
| PES-12 · Publicou sobre CX ou social em 90 dias | `has_post_cx_90d` | Atividade pública no LinkedIn |
| PES-13 · Palestrou em evento em 12 meses | `has_palestra_12m` | Agendas públicas de CONAREC, Febraban Tech, Latam Retail Show e RD Summit |
| PES-14 · No cargo há até 12 meses | `is_novo_no_cargo_12m` | Perfil público do LinkedIn |
| PES-15 · Ex-Itaú, ex-Magalu ou ex-cliente Sprinklr | `has_ex_empresa_cliente_sprinklr` | Histórico no LinkedIn cruzado com a base de clientes Sprinklr |
| PES-16 (!) · Avaliou fornecedor de CX em 12 meses | `has_avaliacao_fornecedor_12m` | Sem fonte pública |

## Campos calculados

| Critério | Campo | Fonte pública |
|---|---|---|
| Todos os eliminatórios da empresa = sim | `is_empresa_elegivel` | Derivado de EMP-01, 04, 08, 11, 21, 22 |
| Âncora de referência (case a usar) | `anchor_case` | Derivado de EMP-01: `itau` para financeiro, `magalu` para varejo e consumo |
| Soma dos critérios que pontuam | `score_empresa` | Derivado dos campos EMP que pontuam |
| Tier da conta (A, B, C ou fora) | `tier_conta` | Derivado de `is_empresa_elegivel` e `score_empresa` |
| Pessoa elegível | `is_pessoa_elegivel` | Derivado de PES-02 e (PES-04, 05, 06, 07 ou 17) |
