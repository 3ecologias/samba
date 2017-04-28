#ATENCAO : Condicoes logicas

from samba.plan.plugins import Plugin


class FiscalizacaoERegulacaoDosServicosDeSaneamentoBasico(Plugin):
    nome = 'Fiscalização e Regulação'
    descricao = '''
Esse conjunto de indicadores permite à entidade fiscalizadora realizar sua função que é a de observar
 se as normas e procedimentos estabelecidos pela regulação estão sendo realizados
 pelo prestador.
    '''
    indicadores = [
        ('FRS1', {
            'nome': 'Já foi instituído o ente regulador e fiscalizador dos serviços de saneamento básico?',
            'escolhas': ['Sim', 'Não'],
        }),
        ('FRS2', {
            'nome': 'Como a regulação e a fiscalização estão sendo executadas pelo titular?',
            'escolhas': ['Diretamente', 'Indiretamente'],
        }),
        ('FRS3', {
            'nome': 'Qual a natureza jurídica do ente regulador e fiscalizador?',
            'paragrafo': 'True',
        }),
        ('FRS4', {
            'nome': 'O ente regulador e fiscalizador possui independência decisória, incluindo autonomia administrativa, orçamentária e financeira?',
            'paragrafo': 'True',
        }),
        ('FRS5', {
            'nome': 'Foi fixada equipe técnica mínima?',
            'paragrafo': 'True',
        }),
        ('FRS6', {
            'nome': 'Equipe técnica atende à demanda pelos serviços de regulação e fiscalização?',
            'paragrafo': 'True',
        }),
        ('FRS7', {
            'nome': 'As atividades do ente regulador e fiscalizador já estão sendo desenvolvidas?',
            'escolhas': ['Sim', 'Não'],
        }),
        ('FRS8', {
            'nome': 'Descrever as atividades realizadas pelo ente regulador e fiscalizador em caso afirmativo.',
            'paragrafo': 'True',
        }),
        ('FRS9', {
            'nome': 'Está havendo a manutenção do convênio com a Agência Reguladora de Serviços de Abastecimento de Agua e de Esgotamento Sanitário do Estado para regulação e fiscalização não apenas dos serviços de água e esgotos, mas também dos componentes resíduos sólidos e drenagem urbana?',
            'paragrafo': 'True',
        }),
        ('FRS10', {
            'nome': 'Está sendo verificado o cumprimento dos planos de saneamento por parte dos prestadores de serviços?',
            'paragrafo': 'True',
        }),
        ('FRS11', {
            'nome': 'Como está sendo verificado o cumprimento dos planos de saneamento por parte dos prestadores de serviços?',
            'paragrafo': 'True',
        }),
        ('FRS12', {
            'nome': 'Está sendo realizada a fiscalização do cumprimento das normas editadas pelo ente regulador?',
            'paragrafo': 'True',
        }),
        ('FRS13', {
            'nome': 'Qual a periodicidade da fiscalização?',
            'paragrafo': 'True',
        }),
        ('FRS14', {
            'nome': 'São elaborados relatórios de fiscalização?',
            'paragrafo': 'True',
        }),
        ('FRS15', {
            'nome': 'Os relatórios estão disponíveis para acesso público? Como?',
            'paragrafo': 'True',
        }),
        ('FRS16', {
            'nome': 'Descrever quais são as estratégias utilizadas para a pratica das atividades realizadas pelo ente regulador para cada período (curto, médio e longo prazo).',
            'paragrafo': 'True',
        }),
        ('FRS17', {
            'nome': 'Já foram editadas normas relativas à qualidade e regularidade da prestação dos serviços?',
            'paragrafo': 'True',
        }),
        ('FRS18', {
            'nome': 'Já foram editados os requisitos operacionais e de manutenção dos sistemas?',
            'paragrafo': 'True',
        }),
        ('FRS19', {
            'nome': 'Já foram estabelecidas as metas progressivas de expansão e de qualidade dos serviços e os respectivos prazos?',
            'paragrafo': 'True',
        }),
        ('FRS20', {
            'nome': 'O ente regulador já estabeleceu regime, estrutura e níveis tarifários, bem como os procedimentos e prazos para a fixação, revisão e reajuste?',
            'paragrafo': 'True',
        }),
        ('FRS21', {
            'nome': 'Já foram editadas normas relativas à medição, faturamento e cobrança de serviço?',
            'paragrafo': 'True',
        }),
        ('FRS22', {
            'nome': 'Já foram editadas normas relativas ao monitoramento dos custos?',
            'paragrafo': 'True',
        }),
        ('FRS23', {
            'nome': 'Já foram editadas normas relativas à medição, faturamento e cobrança dos serviços?',
            'paragrafo': 'True',
        }),
        ('FRS24', {
            'nome': 'Já foram editadas normas relativas à avaliação da eficiência e eficácia dos serviços prestados?',
            'paragrafo': 'True',
        }),
        ('FRS25', {
            'nome': 'Já foram editadas normas relativas ao plano de contas e mecanismos de informação, auditoria e certificação?',
            'paragrafo': 'True',
        }),
        ('FRS26', {
            'nome': 'Já foram fixados critérios para a fiel execução dos contratos, dos serviços e para a correta administração de subsídios?',
            'paragrafo': 'True',
        }),
        ('FRS27', {
            'nome': 'Já foi estabelecido algum tipo de canal para o relacionamento com a sociedade, (seja por meio do atendimento telefônico gratuito, presencial, sítio eletrônico, consultas e audiências públicas) sob a coordenação da Ouvidoria e apoio da Assessoria de Comunicação Social do ente gestor?',
            'paragrafo': 'True',
        }),
        ('FRS28', {
            'nome': 'O ente regulador tem promovido programas de educação da população para o uso adequado do recurso hídrico, com o objetivo de desenvolvimento sustentável, inibindo o consumo supérfluo e seu desperdício?',
            'paragrafo': 'True',
        }),
        ('FRS29', {
            'nome': 'Já foram definidas medidas de contingência e emergência, inclusive racionamento?',
            'paragrafo': 'True',
        }),
        ('FRS30', {
            'nome': 'Será necessária se estruturar para a escolha do ente regulador e fiscalizador?',
            'paragrafo': 'True',
        }),
        ('FRS31', {
            'nome': 'A AGERSA está exercendo as atividades de regulação e fiscalização dos serviços públicos de saneamento básico no município?',
            'paragrafo': 'True',
        })
    ]
