#ATENCAO : Condicoes logicas

from samba.plan.plugins import Plugin


class ParticipacaoEControleSocial(Plugin):
    nome = 'Participação e Controle Social'
    descricao = '''
Conjunto de indicadores que avalia se há estas instâncias de participação, como está a
representatividade destes fóruns, seu funcionamento regular, atividades realizadas
que garantam a participação e o controle social, dentre outros.
'''
    icone_loja = 'icons/256x256/Colorido/participacao_e_controle_social.svg'
    icone_sidebar = 'icons/16x16/Colorido/participacao_e_controle_social.svg'
    indicadores = [
        ('A10', {
            'nome': 'O Conselho Municipal de Saneamento Básico foi constituído?',
            'escolhas': ['','Sim', 'Não'],
        }),
        ('AA10', {
            'nome': 'Há paridade neste conselho?',
            'escolhas': ['','Sim', 'Não'],
        }),
        ('AAA10', {
            'nome': 'Há regularidade mínima das reuniões (a cada dois meses)?',
            'escolhas': ['','Sim', 'Não'],
        }),
        ('AAAA10', {
            'nome': 'Existe alguma outra instância que garanta a participação e o controle social para acompanhamento dos serviços públicos de saneamento básico?',
            'escolhas': ['','Sim', 'Não'],
            'exige_descricao' : True,
        }),
        ('B10', {
            'nome': 'Existem outras instâncias de cunho participativo que acompanhamento além do Conselho?',
            'escolhas': ['','Sim', 'Não'],
        }),
        ('BB10', {
            'nome': 'Tecnologia Adotada - Manejo de Águas Pluviais - Soluções de Prevenção',
            'definicao': 'Verificar se há soluções sustentáveis de drenagem como: bacia de amortecimento, pavimentação permeável, coleta de água de chuva, preservação dos leitos naturais dos rios, manutenção da cobertura vegetal e ou outros.',
            'escolhas': [
                'Comitê de Bacia Hidrográfica',
                'Conselho Gestor de Unidade de Conservação',
                'Conselho Municipal de Meio Ambiente',
                'Comissão interinstitucional de Educação Ambiental',
                'Outro tipo de conselho ou colegiado ambiental'
            ],
            'multipla_escolha': True
        }),
        ('C10', {
            'nome': 'Como se dá a participação destas outras instâncias para este acompanhamento?',
            'definicao': 'Descrever as atividades realizadas de participação e controle social que aconteceram ao longo de cada ano, com o objetivo de acompanhar a gestão em todas as suas atividades (prestação do serviço, regulação, fiscalização e planejamento), por meio de reuniões, seminários, audiências públicas, cursos, dentre outros.',
            'paragrafo': 'True',
        }),
        ('D10', {
            'nome': 'Estratégias de participação, controle social e acompanhamento',
            'definicao': 'Descrever quais são as estratégias utilizadas para a prática permanente da participação e controle social com o objetivo de acompanhar o PMSB em todas as suas etapas.',
            'paragrafo': 'True',
        })
    ]
