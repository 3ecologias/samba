from samba.plan.plugins import Plugin


class SustentabilidadeFinanceira(Plugin):
    nome = 'Sustentabilidade Financeira'
    descricao = '''
    A sustentabilidade econômico-financeira dos serviços públicos de saneamento básico
    deve ser assegurada, sempre que possível, mediante remuneração
    pela cobrança dos serviços.
    '''
    icone_loja = 'icons/256x256/Colorido/sustentabilidade_financeira.svg'

    icone_sidebar = 'icons/16x16/Colorido/sustentabilidade_financeira.svg'

    indicadores = [
        ('NR1', {
            'nome': 'Receita Operacional Direta',
            'definicao': 'Valor da receita anual decorrente das atividades-fim do prestador de serviços, ou seja, produção e distribuição de água e coleta, tratamento e disposição de esgotos.',
            'unidade' : 'R$',
            'fonte' : 'SNIS',
        }),
        ('NT1', {
            'nome': 'Despesas totais com serviço',
            'definicao': 'Valor anual total do conjunto de despesas realizadas para a prestação dos serviços. Inclui Despesas de Exploração (DEX); Juros e Encargos do Serviço da Dívida; Depreciação, Amortização e Provisão para Devedores Duvidosos; Despesas Capitalizáveis; Despesas Fiscais ou Tributárias Incidentes na DTS; além de outras Despesas com os Serviços.',
            'unidade' : 'R$',
            'fonte' : 'SNIS',
        }),
        ('NR2', {
            'nome': 'Receita Operacional Total',
            'definicao': 'Valor faturado anual decorrente das atividades-fim do prestador de serviços, resultante da exclusiva aplicação das tarifas. Resultado da soma da Receita Operacional Direta-Água, Receita Operacional Direta-Esgoto e Receita Operacional Direta - Água Exportada.',
            'unidade' : 'R$',
            'fonte' : 'SNIS',
        }),
        ('NA1', {
            'nome': 'Arrecadação Total',
            'definicao': 'Valor anual efetivamente arrecadado das Receitas Operacionais (Disponível em Caixa ou em Bancos - Conta Movimento).',
            'unidade' : 'R$',
            'fonte' : 'SNIS',
        }),
        ('NR3', {
            'nome': 'Receita Operacional Direta de Água',
            'definicao': 'Valor faturado anual decorrente da prestação do serviço de abastecimento de água, resultante exclusivamente da aplicação de tarifas, excluídos os valores decorrentes da venda de água por atacado (bruta ou tratada).',
            'unidade' : 'R$',
            'fonte' : 'SNIS',
        }),
        ('NR4', {
            'nome': 'Receita Operacional Direta de Esgoto',
            'definicao': 'Valor faturado anual decorrente da prestação do serviço de esgotamento sanitário, resultante exclusivamente da aplicação de tarifas.',
            'unidade' : 'R$',
            'fonte' : 'SNIS',
        })
    ]
