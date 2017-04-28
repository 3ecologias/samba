from samba.plan.plugins import Plugin
from samba.plan.plugins.utils import porcentagem


class UniversalizacaoDoAcesso(Plugin):
    nome = 'Universalização do Acesso'
    descricao = '''
    Conjunto de indicadores que permitem traçar um
    panorama da cobertura dos serviços de saneamento.
    '''
    indicadores = [
        ('PT1', {
            'nome': 'População Total do município',
            'definicao':'Número total de habitantes no município incluindo zona urbana e rural, tanto a população servida quanto a que não é servida pelos serviços.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PU1', {
            'nome': 'População Urbana do Município (Sede Municipal)',
            'definicao':'Número de habitantes no município que residem na zona urbana, tanto a população servida quanto a que não é servida pelos serviços.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PU2', {
            'nome': 'População Rural do Município',
            'definicao':'Número de habitantes no município que residem na zona rural, tanto a população servida quanto a que não é servida pelos serviços.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PA1', {
            'nome': 'População atendida com abastecimento de água',
            'definicao':'Número total de habitantes a que o prestador fornece serviços de abastecimento de água, seja na sede municipal ou localidades.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PA2', {
            'nome': 'População urbana atendida com abastecimento de água',
            'definicao':'Número total de habitantes da zona urbana a que o prestador fornece serviços de abastecimento de água.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PA3', {
            'nome': 'População rural atendida com abastecimento de água',
            'definicao':'Número total de habitantes da zona rural a que o prestador fornece serviços de abastecimento de água.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PA4', {
            'nome': 'População atendida com abastecimento de água por soluções individualizadas',
            'definicao':'Número total de habitantes que adota uma solução individualizada como aproveitamento da água de chuvas, cisternas, etc.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PE1', {
            'nome': 'População atendida por rede de esgotamento sanitário',
            'definicao':'Número total de habitantes com acesso ao serviço de coleta de esgotos, seguida de tratamento, realizado pelo prestador de serviços, seja na sede municipal ou localidades.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PE2', {
            'nome': 'População urbana atendida por rede de esgotamento sanitário',
            'definicao':'Número total de habitantes da zona urbana com acesso ao serviço de coleta de esgotos, seguida de tratamento, realizado pelo prestador de serviços, seja na sede municipal ou localidades.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PE3', {
            'nome': 'População rural atendida por rede de esgotamento sanitário',
            'definicao':'Número total de habitantes da zona rural com acesso ao serviço de coleta de esgotos, seguida de tratamento, realizado pelo prestador de serviços.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PE4', {
            'nome': 'População atendida por soluções individuais de esgotamento sanitário',
            'definicao':'População atendida por algum tipo de solução individualizada para a destinação do esgoto doméstico: fossa séptica, dentre outros (conforme Relatório Técnico Participativo).',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PE5', {
            'nome': 'População urbana atendida por soluções individuais de esgotamento sanitário',
            'definicao':'População urbana atendida por algum tipo de solução individualizada para a destinação do esgoto doméstico: fossa séptica, dentre outros (conforme Relatório Técnico Participativo).',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PR1', {
            'nome': 'População com acesso à coleta de Resíduo Sólido',
            'definicao':'População atendida pela coleta pública de resíduos sólidos.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PR2', {
            'nome': 'População urbana com acesso à coleta de Resíduo Sólido',
            'definicao':'População urbana atendida pela coleta pública de resíduos sólidos.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('PR3', {
            'nome': 'População rural com acesso à coleta de Resíduo Sólido',
            'definicao':'População rural atendida pela coleta pública de resíduos sólidos.',
            'unidade': 'habitantes',
            'fonte' : 'IBGE',
        }),
        ('LD1', {
            'nome': 'Quantidade de Logradouros com algum tipo de solução de drenagem (para todo o município)',
            'definicao':'Quantidade de logradouros atendidos por sistema de drenagem urbana, tais como: micro drenagem e macro drenagem (condutos e dispositivos projetados em função do plano de arruamento).',
            'unidade': 'logradouros',
            'fonte' : 'Gestor',
        }),
        ('LT1', {
            'nome': 'Quantidade total logradouros (para todo o município)',
            'definicao':'Quantidade total de logradouros do município.',
            'unidade': 'logradouros',
            'fonte' : 'Gestor',
        }),
        ('DT1', {
            'nome': 'Domicílio Total do município',
            'definicao':'Número total de domicílios no município incluindo zona urbana e rural.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DU1', {
            'nome': 'Domicílios urbanos do município',
            'definicao':'Número total de domicílios no município que residem na zona urbana.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DU2', {
            'nome': 'Domicílio rurais do município',
            'definicao':'Número total de domicílios no município que residem na zona rural.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DA1', {
            'nome': 'Domicílios atentidos com abastecimento de água pelo prestador de serviços',
            'definicao':'Número total de domicpilios a que o prestador fornece serviços de abastecimento de água, seja na sede municipal ou localidades.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DA2', {
            'nome': 'Domicilios urbanos atendidos com abastecimento de água pelo prestador de serviços',
            'definicao':'Número total de domicílios da zona urbana a que o prestador fornece serviços de abastecimento de água.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DA3', {
            'nome': 'Domicílios rurais atendidos com abastecimento de água pelo prestador de serviços',
            'definicao':'Número total de domicílios da zona rural a que o prestador fornece serviços de abastecimento de água.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DE1', {
            'nome': 'Domicílios atentidos por rede de esgotamento sanitário',
            'definicao':'Número total de domicílios servidos por rede coletora ou fossa séptica.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DE2', {
            'nome': 'Domicílios urbanos atendidos por rede de esgotamento sanitário',
            'definicao':'Número total de domicílios urbano servidos por rede coletora ou fossa séptica.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DE3', {
            'nome': 'Domicílios rurais atendidos por rede de esgotamento sanitário',
            'definicao':'Número total de domicílios rurais servidos por rede coletora ou fossa séptica.',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DE4', {
            'nome': 'Domicilios que possuem banheiros',
            'definicao':'Número de domícilos que possuem banheiros (chuveiro ou banheira e vaso sanitário).',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DR1', {
            'nome': 'Domicílios atendidos por coleta direta',
            'definicao':'Domicílios urbanos e rurais atendidos por coleta direta (porta-a-porta).',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DR2', {
            'nome': 'Domicílios urbanos atendidos por coleta direta',
            'definicao':'Domicílios urbanos atendidos por coleta direta (porta-a-porta).',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('DR3', {
            'nome': 'Domicílios rurais atendidos por coleta direta',
            'definicao':'Domicílios rurais atendidos por coleta direta (porta-a-porta).',
            'unidade': 'domicílios',
            'fonte' : 'IBGE',
        }),
        ('UA1', {
            'nome': 'Índice de Atendimento de Água ',
            'unidade': '%',
            'calcular': porcentagem('PA1', 'PT1'),
        }),
        ('UA2', {
            'nome': 'Índice de Atendimento de Água aos Domicílios',
            'unidade': '%',
            'calcular': porcentagem('DA1', 'DT1'),
        }),
        ('UA3', {
            'nome': 'Índice de Atendimento de Água à População Urbana',
            'unidade': '%',
            'calcular': porcentagem('PA2', 'PU1'),
        }),
        ('UA4', {
            'nome': 'Índice de Atendimento de Água aos Domicílios Urbanos',
            'unidade': '%',
            'calcular': porcentagem('DA2', 'DT1'),
        }),
        ('UA5', {
            'nome': 'Índice de Atendimento de Água à População Rural',
            'unidade': '%',
            'calcular': porcentagem('PA3', 'PR1'),
        }),
        ('UA6', {
            'nome': 'Índice de Atendimento de Água aos Domicílios Rurais',
            'unidade': '%',
            'calcular': porcentagem('DA3', 'DT1'),
        }),
        ('UA7', {
            'nome': 'Índice de Atendimento de Água (Soluções Individualizadas)',
            'unidade': '%',
            'calcular': porcentagem('PA4', 'PT1'),
        }),
        ('UE1', {
            'nome': 'Índice de atendimento de esgoto (rede de esgotamento sanitário)',
            'unidade': '%',
            'calcular': porcentagem('PE1', 'PT1'),
        }),
        ('UE2', {
            'nome': 'Índice de atendimento de esgoto (rede de esgotamento sanitário) aos domicílios',
            'unidade': '%',
            'calcular': porcentagem('DE1', 'PT1'),
        }),
        ('UE3', {
            'nome': 'Índice de atendimento de esgoto à População Urbana (rede de esgotamento sanitário)',
            'unidade': '%',
            'calcular': porcentagem('PE2', 'PU1'),
        }),
        ('UE4', {
            'nome': 'Índice de atendimento de esgoto aos Domicílios  Urbanos (rede de esgotamento sanitário)',
            'unidade': '%',
            'calcular': porcentagem('DE2', 'PT1'),
        }),
        ('UE5', {
            'nome': 'Índice de atendimento de esgoto à População Rural (rede de esgotamento sanitário)',
            'unidade': '%',
            'calcular': porcentagem('PE3', 'PU2'),
        }),
        ('UE6', {
            'nome': 'Índice de atendimento de esgoto aos Domicílios  Rurais (rede de esgotamento sanitário)',
            'unidade': '%',
            'calcular': porcentagem('DE3', 'PT1'),
        }),
        ('UE7', {
            'nome': 'Índice de atendimento de esgoto (solução individualizada)',
            'unidade': '%',
            'calcular': porcentagem('PE4', 'PT1'),
        }),
        ('UE8', {
            'nome': 'Índice de atendimento de esgoto à População Urbana (solução individualizada)',
            'unidade': '%',
            'calcular': porcentagem('PE5', 'PU1'),
        }),
        ('UE9', {
            'nome': 'Índice de domicílios que possuem unidades hidrossanitárias',
            'unidade': '%',
            'calcular': porcentagem('DE4', 'DT1'),
        }),
        ('UR1', {
            'nome': 'Índice de cobertura do serviço de coleta de RDO',
            'unidade': '%',
            'calcular': porcentagem('PR1', 'PT1'),
        }),
        ('UR2', {
            'nome': 'Índice de Cobertura do Serviço de Coleta de RDO aos Domicílios',
            'unidade': '%',
            'calcular': porcentagem('DR1', 'DT1'),
        }),
        ('UR3', {
            'nome': 'Índice de Cobertura Urbana do Serviço de Coleta de RDO',
            'unidade': '%',
            'calcular': porcentagem('PR2', 'PU1'),
        }),
        ('UR4', {
            'nome': 'Índice de Cobertura do Serviço de Coleta de RDO aos Domicílios Urbanos',
            'unidade': '%',
            'calcular': porcentagem('DR2', 'DT1'),
        }),
        ('UR5', {
            'nome': 'Índice de Cobertura Rural do serviço de coleta de RDO',
            'unidade': '%',
            'calcular': porcentagem('PR3', 'PR1'),
        }),
        ('UR6', {
            'nome': 'Índice de Cobertura do Serviço de Coleta de RDO aos Domicílios Rurais',
            'unidade': '%',
            'calcular': porcentagem('DR3', 'DT1'),
        }),
        ('UD1', {
            'nome': 'Índice de atendimento de drenagem urbana',
            'unidade': '%',
            'calcular': porcentagem('LD1', 'LT1'),
        })
    ]
