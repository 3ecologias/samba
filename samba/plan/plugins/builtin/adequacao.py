from samba.plan.plugins import Plugin

class Adequacao(Plugin):
    nome = 'Adequação'
    descricao = '''
    Conjunto de indicadores que a permitem avaliar
    a adequação à saúde pública e ao ambiente.
    '''
    icone_loja = 'icons/256x256/Colorido/adequacao.svg'
    icone_sidebar = 'icons/16x16/Colorido/adequacao.svg'
    indicadores = [
        ('AE1', {
            'nome': 'Quantidade de casos registrados de esquistossomose',
            'definicao' : 'Quantidade total anual de casos de esquistossomose notificados no Sistema de Informação de Agravos de Notificação(SINAN).',
            'unidade' : 'casos/ano',
            'fonte' : 'SINAN/DATASUS',
        }),
        ('AD1', {
            'nome': 'Quantidade de casos registrados de dengue',
            'definicao': 'Quantidade total anual de casos de dengue notificados no Sistema de Informação de Agravos de Notificação(SINAN).',
            'unidade' : 'casos/ano',
            'fonte' : 'SINAN/DATASUS',
        }),
        #indicador que não existe no MODELS_INDICADORES/models_adequcao.py
        ('AV1', {
            'nome': 'Quantidade de casos registrados de verminose',
            'definicao': 'Quantidade total anual de casos de verminose notificados no Sistema de Informação de Agravos de Notificação(SINAN).',
            'unidade' : 'casos/ano',
            'fonte' : 'SINAN/DATASUS',
        }),
        ('AL1', {
            'nome': 'Quantidade de casos registrados de leptospirose',
            'definicao': 'Quantidade total anual de casos de leptospirose notificados no Sistema de Informação de Agravos de Notificação(SINAN).',
            'unidade' : 'casos/ano',
            'fonte' : 'SINAN/DATASUS',
        }),
        ('AH1', {
            'nome': 'Quantidade de casos hepatite A',
            'definicao': 'Quantidade total anual de casos de hepatite A notificados no Sistema de Informação de Agravos de Notificação(SINAN).',
            'unidade' : 'casos/ano',
            'fonte' : 'SINAN/DATASUS',
        })
    ]
