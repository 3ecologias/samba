#ATENCAO : Normalmente AA7 e AAA7 aparecem so se a pessoa responde Sim em A7

from samba.plan.plugins import Plugin


class RevisaoDoPlanoMunicipalDeSaneamento(Plugin):
    nome = 'Revisão'
    descricao = '''
Conjunto de indicadores que verifica se o gestor está cumprindo
o preconizado na Política Pública de Saneamento Básico, atualizando assim,
quando da revisão do plano, as estratégias de condução da gestão do serviço no município,
e avaliando a eficiência, eficácia e eficiência das ações propostas nas versões anteriores do plano.

    '''
    icone_loja = 'static/icons/256x256/Colorido/revisao_do_plano_municipal.svg'
    icone_sidebar = 'static/icons/16x16/Colorido/revisao_do_plano_municipal.svg'
    indicadores = [
        ('RP1', {
            'nome': 'Quando foi elaborada a primeira versão do PMSB?',
            'paragrafo': 'True',
        }),
        ('RP2', {
            'nome': 'Caso tenha 4 anos ou mais de elaborado, informar se já foi realizada alguma revisão?',
            'paragrafo': 'True',
        }),
        ('RP3', {
            'nome': 'Quantas revisões foram realizadas?',
            'paragrafo': 'True',
        })
    ]
