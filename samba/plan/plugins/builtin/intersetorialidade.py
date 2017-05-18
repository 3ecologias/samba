#ATENCAO : Normalmente AA7 e AAA7 aparecem so se a pessoa responde Sim em A7

from samba.plan.plugins import Plugin


class Intersetorialidade(Plugin):
    nome = 'Intersetorialidade'
    descricao = '''
Conjunto de indicadores que permitem refletir a respeito do grau de
articulação das políticas de saneamento com as outras políticas desenvolvidas,
através da articulação existente entre os setores da administração pública do
município e sua evolução ao longo do desenvolvimento do PMSB.
    '''
    icone_loja = 'icons/256x256/Colorido/intersetorialidade.svg'
    icone_sidebar = 'icons/16x16/Colorido/intersetorialidade.svg'
    indicadores = [
        ('A7', {
            'nome': 'Existem planos, programas, e/ou projetos desenvolvidos por outros setores administrativos no campo do saneamento básico?',
            'escolhas': ['Sim', 'Não'],
        }),
        ('AA7', {
            'nome': 'Citar quais planos, programas e/ou projetos e a que setores administrativos estão vinculados (saúde, meio ambiente, recursos hídricos, desenvolvimento urbano, habitação e educação)',
            'paragrafo': 'True',
        }),
        ('AAA7', {
            'nome': 'Estes planos, programas, projetos e/ou atividades de controle se articulam com o setor administrativo responsável pelo saneamento?',
            'paragrafo': 'True',
        }),
        ('B7', {
            'nome': 'Existem mecanismos de integração e de articulação entre as diversas áreas administrativas que possuem interface com o saneamento (saúde, meio ambiente, recursos hídricos, desenvolvimento urbano, habitação e educação)(Se a resposta for SIM, descrever como se a resposta for NÃO, descrever porque)?',
            'paragrafo': 'True',
        })
    ]
