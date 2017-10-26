from samba.plan.plugins import Plugin
from samba.plan.plugins.utils import porcentagem
from samba.plan.plugins.utils import pormil
from samba.plan.plugins.utils import divisao


class QualidadeServicosPrestados(Plugin):
    nome = 'Qualidade dos serviços prestados'
    descricao = '''
    Conjunto de indicadores dessa categoria que permitem analisar as condições de qualidade na prestação dos serviços de saneamento.
    '''
    icone_loja = 'icons/256x256/Colorido/qualidade_dos_servicos_prestados.svg'
    icone_sidebar = 'icons/16x16/Colorido/qualidade_dos_servicos_prestados.svg'
    indicadores = [
        ('SQ1', {
            'nome': 'Quantidade de amostras em conformidade - Cloro residual',
            'definicao': 'Quantidade total anual de amostras com Cloro Residual dentro do padrão de conformidade, coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes).',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SQ2', {
            'nome': 'Quantidade mínima de amostras - Cloro residual',
            'definicao': 'Quantidade mínima anual de amostras coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes), para aferição do teor de Cloro Residual.',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SQ3', {
            'nome': 'Quantidade de amostras fora do padrão - Cloro residual',
            'definicao': 'Quantidade de amostras com Cloro fora do padrão coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes).',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SQ4', {
            'nome': 'Quantidade de amostras em conformidade - Turbidez',
            'definicao' : 'Quantidade de amostras com Turbidez dentro do padrão de conformidade coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes).',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SQ5', {
            'nome': 'Quantidade mínima de amostras - Turbidez',
            'definicao': 'Quantidade mínima anual de amostras coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes), para aferição da Turbidez.',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SQ6', {
            'nome': 'Quantidade de amostras fora do padrão - Turbidez',
            'definicao': 'Quantidade de amostras com Turbidez fora do padrão coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes).',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SQ7', {
            'nome': 'Quantidade de amostras em conformidade - Coliformes Totais',
            'definicao': 'Quantidade de amostras com Coliformes Totais dentro do padrão de conformidade coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes).',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SQ8', {
            'nome': 'Quantidade mínima de amostras - Coliformes Totais',
            'definicao': 'Quantidade mínima anual de amostras coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes), para aferição do teor de Coliformes Totais.',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SQ9', {
            'nome': 'Quantidade de amostras fora do padrão – Coliformes Totais',
            'definicao': 'Quantidade de amostras com Coliformes Totais fora do padrão coletadas na(s) saída(s) da(s) unidade(s) de tratamento e no sistema de distribuição de água (reservatórios e redes).',
            'unidade' : 'amostras/ano',
            'fonte' : 'Coleta e análise da água',
        }),
        ('SC1', {
            'nome': 'Número de reclamações dos usuários dos serviços de abastecimento de água',
            'definicao': 'Registro de reclamações do serviço de abastecimento de água por mês.',
            'unidade' : 'reclamações/mês',
            'fonte' : 'Gestor/Prestador',
        }),
        ('SC2', {
            'nome': 'Número de ligações ativas de água',
            'definicao': 'Quantidade de ligações ativas de água.',
            'unidade' : 'ligações',
            'fonte' : 'Prestador do Serviço',
        }),
        ('SC3', {
            'nome': 'Número de reclamações dos usuários dos serviços de esgotamento sanitário',
            'definicao': 'Registro de reclamações do serviço de esgotamento sanitário por mês.',
            'unidade' : 'reclamações/mês',
            'fonte' : 'Gestor/Prestador',
        }),
        ('SC4', {
            'nome': 'Número de ligações ativas de esgoto',
            'definicao': 'Quantidade de ligações ativas de esgoto.',
            'unidade' : 'ligações',
            'fonte' : 'Prestador do Serviço',
        }),
        ('SC5', {
            'nome': 'Número de reclamações dos usuários do serviço coleta de RS',
            'definicao': 'Registro de reclamações do serviço de coleta de resíduos sólidos por mês.',
            'unidade' : 'reclamações/mês',
            'fonte' : 'Gestor/Prestador',
        }),
        ('SC6', {
            'nome': 'Quantidade de Logradouros que recebem coleta de RS',
            'definicao': 'Quantidades de logradouros que possuem coleta direta de resíduos sólidos por mês.',
            'unidade' : 'logradouros',
            'fonte' : 'Gestor/Prestador',
        }),
        ('SC7', {
            'nome': 'Número de reclamações dos usuários do serviço de drenagem urbana',
            'definicao': 'Registro de reclamações do serviço de drenagem urbana por mês.',
            'unidade' : 'reclamações/mês',
            'fonte' : 'Gestor/Prestador',
        }),
        ('SH1', {
            'nome': 'Horas de paralização do serviço',
            'definicao': 'Quantidade de horas por paralização do abastecimento de água.',
            'unidade' : 'horas',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN1', {
            'nome': 'Número de reclamações dos usuários dos serviços de saneamento',
            'definicao': 'Registro de reclamações dos serviços de saneamento por mês.',
            'unidade' : 'reclamações/mês',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN2', {
            'nome': 'Números de paralisações',
            'definicao': 'Quantidade de paralisações do abastecimento de água.',
            'unidade' : 'paralisações',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SH2', {
            'nome': 'Horas de intermitência do serviço',
            'definicao': 'Quantidade de horas de intermitência do abastecimento de água.',
            'unidade' : 'horas',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN3', {
            'nome': 'Números de interrupções',
            'definicao': 'Quantidade de interrupções do abastecimento de água.',
            'unidade' : 'interrupções',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SD1', {
            'nome': 'Duração dos reparos',
            'definicao': 'Quantidade de horas de cada reparo.',
            'unidade' : 'horas',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN4', {
            'nome': 'Números de extravasamentos de esgoto',
            'definicao': 'Quantidade de extravasamentos de esgoto.',
            'unidade' : 'estravasamento',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SX1', {
            'nome': 'Extensão da rede',
            'definicao': 'Comprimento em quilômetros da rede de esgotamento sanitário.',
            'unidade' : 'km',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SM1', {
            'nome': 'Número de mananciais com áreas de proteção de aquíferos',
            'definicao': 'Quantidade de mananciais com áreas de proteção de aquíferos.',
            'unidade' : 'mananciais protegidos',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SM2', {
            'nome': 'Número de mananciais utilizados para abastecimento',
            'definicao': 'Quantidade de mananciais utilizados para abastecimento.',
            'unidade' : 'mananciais utilizados',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN5', {
            'nome': 'Número ocorrências quanto á vandalismo, roubo/furto e depredações.',
            'definicao': 'Quantidade de ocorrências registradas na delegacia quanto á vandalismo, roubo/furto e depredações.',
            'unidade' : 'ocorrências',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN6', {
            'nome': 'Número de funcionários acidentados',
            'definicao': 'Quantidade de registros de funcionários do serviço público de saneamento básico acidentados ao longo do ano.',
            'unidade' : 'funcionários acidentados',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN7', {
            'nome': 'Número total de funcionários do serviço público de saneamento básico',
            'definicao': 'Número total de funcionários do serviço público de saneamento básico municipal.',
            'unidade' : 'funcionários',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN8', {
            'nome': 'Número de logradouros com cadastro da rede de abastecimento atualizado',
            'definicao': 'Logradouros com cadastro em arquivo físico ou digital da rede de abastecimento de água.',
            'unidade' : 'logradouros',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN9', {
            'nome': 'Número total de logradouros',
            'definicao': 'Quantidade total de logradouros.',
            'unidade' : 'logradouros',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN10', {
            'nome': 'Número de logradouros com cadastro da rede de esgotamento atualizado',
            'definicao': 'Logradouros com cadastro em arquivo físico ou digital da rede de esgotamento sanitário.',
            'unidade' : 'logradouros',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN11', {
            'nome': 'Número de logradouros com cadastro do sistema de drenagem',
            'definicao': 'Logradouros com cadastro em arquivo físico ou digital da rede de drenagem.',
            'unidade' : 'logradouros',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN12', {
            'nome': 'Número de logradouros cadastrados na rota de coleta de resíduo sólido',
            'definicao': 'Logradouros cadastrados em meio físico ou digital na coleta de resíduo solido.',
            'unidade' : 'logradouros',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN13', {
            'nome': 'Número de Funcionários Nível Superior relacionados a saneamento.',
            'unidade' : 'logradouros',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN14', {
            'nome': 'Número de Funcionários Nível Técnico relacionados a saneamento.',
            'unidade' : 'logradouros',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SN15', {
            'nome': 'Número de funcionários que receberam alguma qualificação em saneamento e ou meio ambiente.',
            'unidade' : 'logradouros',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SE1', {
            'nome': 'Quantidade de Economias Residenciais Ativas de Água',
            'definicao': 'Quantidade de residências com ligação de água ativa.',
            'unidade' : 'economias residenciais ativas',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SE2', {
            'nome': 'Quantidade de Economias Ativas de Água',
            'definicao': 'Quantidade de economias ativas de água que contribuíram para o faturamento no último mês do ano.',
            'unidade' : 'economias ativas de água',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SE3', {
            'nome': 'Quantidade de Economias Ativas de Água Atingidas por Paralisações',
            'definicao': 'Quantidade anual de economias ativas atingidas por paralisações no sistema de distribuição de água.',
            'unidade' : 'economias ativas atingidas por paralisações',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SE4', {
            'nome': 'Quantidade de Economias Ativas de Água Atingidas por Intermitências',
            'definicao': 'Quantidade anual de economias ativas atingidas por interrupções no sistema de distribuição de água.',
            'unidade' : 'economias ativas atingidas por interrupções',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('SV1', {
            'nome': 'Valor da tarifa social',
            'unidade' : 'Reais',
            'fonte' : 'Prestador do serviço/SNIS',
        }),

        ('SS1', {
            'nome': 'Média de renda das famílias assistidas por tarifa social',
            'unidade' : 'Reais',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('ST4', {
            'nome': 'Total de contas de taxa mínima com pagamento atrasado',
            'unidade' : 'contas em atraso',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('ST5', {
            'nome': 'Total de residências que pagam a taxa mínima',
            'unidade' : 'residências',
            'fonte' : 'Prestador do serviço/SNIS',
        }),
        ('QA1', {
            'nome': 'Índice de conformidade da quantidade de amostra - Cloro Residual',
            'unidade': '%',
            'calcular': porcentagem('SQ1', 'SQ2'),
        }),
        ('QA2', {
            'nome': 'Incidência das análises de Cloro Residual fora do padrão',
            'unidade': '%',
            'calcular': porcentagem('SQ3', 'SQ2'),
        }),
        ('QA3', {
            'nome': 'Índice de conformidade da quantidade de amostra - Turbidez',
            'unidade': '%',
            'calcular': porcentagem('SQ4', 'SQ5'),
        }),
        ('QA4', {
            'nome': 'Incidência das análises de Turbidez fora do padrão',
            'unidade': '%',
            'calcular': porcentagem('SQ6', 'SQ5'),
        }),
        ('QA5', {
            'nome': 'Índice de conformidade da quantidade de amostra - Coliformes Totais',
            'unidade': '%',
            'calcular': porcentagem('SQ7', 'SQ8'),
        }),
        ('QA6', {
            'nome': 'Incidência das análises de Coliformes Totais fora do padrão',
            'unidade': '%',
            'calcular': porcentagem('SQ9', 'SQ8'),
        }),
        ('QC1', {
            'nome': 'Índice de reclamações do serviço de abastecimento de água',
            'calcular': pormil('SC1', 'SC2'),
        }),
        ('QC2', {
            'nome': 'Índice de reclamações do serviço de esgotamento sanitário',
            'calcular': pormil('SC3', 'SC4'),
        }),
        ('QC3', {
            'nome': 'Índice de reclamações do serviço coleta de Resíduos',
            'calcular': divisao('SC5', 'SC6'),
        }),
        ('QC4', {
            'nome': 'Índice de reclamações do serviço de drenagem urbana',
            'calcular': divisao('SC7', 'LD1'),
        }),
        ('QR1', {
            'nome': 'Duração média das paralisações',
            'calcular': divisao('SH1', 'SN2'),
        }),
        ('QR2', {
            'nome': 'Duração média das intermitências',
            'calcular': divisao('SH2', 'SN3'),
        }),
        ('QR3', {
            'nome': 'Economias ativas atingidas por paralisações',
            'calcular': divisao('SE3', 'SN2'),
        }),
        ('QR4', {
            'nome': 'Economias ativas atingidas por intermitências',
            'calcular': divisao('SE4', 'SN3'),
        }),
        ('QR5', {
            'nome': 'Duração média dos reparos de extravasamentos de esgotos',
            'unidade': 'horas/reparo',
            'calcular': divisao('SD1', 'SN4'),
        }),
        ('QR6', {
            'nome': 'Extravasamentos de esgotos por economias residenciais ativas',
            'calcular': divisao('SN4', 'SE1'),
        }),
        ('QR7', {
            'nome': 'Regularidade na coleta de Resíduos Sólidos',
            'definicao': 'Com qual frequência ocorre a coleta de resíduos sólidos?',
            'escolhas': [
                'Diariamente',
                'Semanalmente',
                'Quinzenalmente',
                'Outro'
            ],
            'multipla_escolha': True
        }),
        ('QS1', {
            'nome': 'Nível de segurança contra contaminação dos mananciais aquíferos (superficial e subterrâneo)',
            'unidade': '%',
            'calcular': porcentagem('SM1', 'SM2'),
        }),
        ('QS2', {
            'nome': 'Ocorrências quanto á vandalismo, roubo/furto e depredações',
            'unidade': 'por mês',
            'calcular': porcentagem('SN5', 12),
        }),
        ('QS3', {
            'nome': 'Risco de acidente de trabalho',
            'unidade': '%',
            'calcular': porcentagem('SN6', 'SN7'),
        }),
        ('QT1', {
            'nome': 'Cadastro técnico atualizado da rede de abastecimento de água',
            'unidade': '%',
            'calcular': porcentagem('SN8', 'SN9'),
        }),
        ('QT2', {
            'nome': 'Cadastro técnico atualizado da rede de esgotamento sanitário',
            'unidade': '%',
            'calcular': porcentagem('SN10', 'SN9'),
        }),
        ('QT3', {
            'nome': 'Cadastro técnico atualizado do sistema de drenagem',
            'unidade': '%',
            'calcular': porcentagem('SN11', 'SN9'),
        }),
        ('QT4', {
            'nome': 'Cadastro da rota de coleta de resíduo sólido',
            'unidade': '%',
            'calcular': porcentagem('SN12', 'SN9'),
        }),
        ('QT5', {
            'nome': 'Grau de qualificação técnica dos profissionais  de nível superior',
            'unidade': '%',
            'calcular': porcentagem('SN13', 'SN7'),
        }),
        ('QT6', {
            'nome': 'Grau de qualificação técnica dos profissionais de nível técnico',
            'unidade': '%',
            'calcular': porcentagem('SN14', 'SN7'),
        }),
        ('QT7', {
            'nome': 'Grau de qualificação técnica dos profissionais qualificados',
            'calcular': divisao('SN15', 'SN15'),
        }),
        ('QT8', {
            'nome': 'São empregadas técnicas de monitorização das unidades de tratamento de água, quais?',
            'escolhas': ['', 'Sim', 'Não'],
            'exige_descricao' : True,
        }),
        ('QT9', {
            'nome': 'São empregadas técnicas de monitorização das unidades de tratamento de esgoto, quais?',
            'escolhas': ['', 'Sim', 'Não'],
            'exige_descricao' : True,
        }),
        ('QT10', {
            'nome': 'As unidades de tratamento possuem licenças ambientais e outorga de uso dos recursos hídricos em vigência?',
            'escolhas': ['', 'Outorga', 'Licença ambiental'],
        }),
        ('QT11', {
            'nome': 'Qual a regularidade na manutenção do sistema de abastecimento de água?',
            'unidade': 'por dia',
        }),
        ('QT12', {
            'nome': 'Qual a regularidade na manutenção do sistema de esgotamento sanitário?',
            'unidade': 'por dia',
        }),
        ('QT13', {
            'nome': 'Qual a regularidade na manutenção do sistema drenagem urbana?',
            'unidade': 'por dia',
        }),
        ('QT14', {
            'nome': 'Observação de normas técnicas para abastecimento de água',
            'definicao':'As atividades operacionais-técnicas dos serviços observam as normas, resoluções referentes às suas especificidades?',
            'escolhas': ['', 'Sim', 'Não', 'Parcialmente'],
        }),
        ('QT15', {
            'nome': 'Observação de normas técnicas para o tratamento e disposição final do esgoto ',
            'definicao':'As atividades operacionais-técnicas dos serviços observam as normas, resoluções referentes às suas especificidades?',
            'escolhas': ['', 'Sim', 'Não','Parcialmente'],
        }),
        ('QM1', {
            'nome': 'Participação das economias residenciais de água no total das economias de água',
            'unidade': '%',
            'calcular': porcentagem('SQ7', 'SQ8'),
        }),
        ('QM2', {
            'nome': 'Impacto da tarifa social na renda dos usuários',
            'unidade': '%',
            'calcular': porcentagem('SV1', 'SS1'),
        }),
        ('QM3', {
            'nome': 'Índice de inadimplências da conta de água',
            'unidade': '%',
            'calcular': porcentagem('ST4', 'ST5'),
        })
    ]
