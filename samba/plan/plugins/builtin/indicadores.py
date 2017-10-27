#Não tem o campo fonte que deveria ser definido

from samba.plan.plugins import Plugin


class IndicadoresdeEficiencia(Plugin):
    nome = 'Indicadores de Eficiência'
    descricao = '''
A análise de eficiência, os indicadores dão maior foco aos dispêndios
de recursos energéticos, humanos e financeiros.
    '''
    icone_loja = 'icons/256x256/Colorido/indicadores_de_eficiencia.svg'

    icone_sidebar = 'icons/16x16/Colorido/indicadores_de_eficiencia.svg'

    indicadores = [
        ('FC1', {
            'nome': 'Consumo total de energia elétrica em sistemas de abastecimento de água (Kw/h)',
            'definicao': 'Consumo de energia elétrica pelas maquinas e equipamentos do sistema de abastecimento de água e esgotamento sanitário.',
            'unidade' : 'Kw/h',
            'fonte' : 'SNIS',
        }),
        ('FV1', {
            'nome': 'Volume de água (Produzido + Tratado Importado) (m³)',
            'definicao': 'Volume de água disponível para consumo, compreendendo a água captada pelo prestador de serviços e a água importada bruta, ambas tratadas na(s) unidade(s) de tratamento do prestador de serviços, medido ou estimado na(s) saída(s) da(s) ETA(s) ou Unidade(s) de Tratamento Simplificado (UTS). Inclui também os volumes de água captada pelo prestador de serviços que sejam disponibilizados para consumo sem tratamento, medidos na(s) entrada(s) do sistema de distribuição.',
            'unidade' : 'm³',
            'fonte' : 'SNIS',
        }),
        ('FE1', {
            'nome': 'Quantidade de Economias Ativas (Água + Esgoto)',
            'definicao': 'Quantidade de economias residenciais ativas de água e esgoto que contribuíram para o faturamento no último mês do ano.',
            'unidade' : 'economias',
            'fonte' : 'SNIS',
        }),
        ('FE2', {
            'nome': 'Quantidade total de empregados próprios',
            'unidade' : 'empregados',
            'fonte' : 'SNIS',
        }),
        ('FE3', {
            'nome': 'Quantidade de empregados para funcionamento do SAA',
            'definicao': 'Quantidade de empregados, próprios ou terceirizados, necessários para o funcionamento do Sistema de Abatecimento de Água.',
            'unidade' : 'empregados',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FE4', {
            'nome': 'Quantidade de empregados para funcionamento do SES',
            'definicao': 'Quantidade de empregados, próprios ou terceirizados, necessários para o funcionamento do Sistema de Esgotamento Sanitário.',
            'unidade' : 'empregados',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FE5', {
            'nome': 'Quantidade de empregados para funcionamento do SDU',
            'definicao': 'Quantidade de empregados, próprios ou terceirizados, necessários para o funcionamento do Sistema de Drenagem Urbana.',
            'unidade' : 'empregados',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FE6', {
            'nome': 'Quantidade de empregados no manejo de RS',
            'definicao': 'Quantidade de empregados, próprios ou terceirizados, necessários para o manejo de Resíduos Sólidos do Sistema de Drenagem Urbana.',
            'unidade' : 'empregados',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FD1', {
            'nome': ' Despesas com Pessoal Próprio + Despesas com Serviços de Terceiros',
            'unidade' : 'R$/ano',
            'fonte' : 'SNIS',
        }),
        ('FD2', {
            'nome': 'Despesas totais com serviço',
            'definicao':'Valor anual total do conjunto de despesas realizadas para a prestação dos serviços. Inclui Despesas de Exploração (DEX); Juros e Encargos do Serviço da Dívida; Depreciação, Amortização e Provisão para Devedores Duvidosos; Despesas Capitalizáveis; Despesas Fiscais ou Tributárias Incidentes na DTS; além de outras Despesas com os Serviços.',
            'unidade' : 'R$/ano',
            'fonte' : 'SNIS',
        }),
        ('FV2', {
            'nome': 'Volume de Água Faturado (m³/ano)',
            'definicao': 'Volume de água debitado ao total de economias (medidas e não medidas), para fins de faturamento. Inclui o volume de água tratada exportado.',
            'unidade' : 'm³/ano',
            'fonte' : 'SNIS',
        }),
        ('FV3', {
            'nome': 'Volume de água (Produzido + Tratado Importado - de Serviço)',
            'definicao': 'Volume de água tratada disponibilizado para consumo.',
            'unidade' : 'm³',
            'fonte' : 'SNIS',
        }),
        ('FH1', {
            'nome': 'Residência com Hidrômetro Instalado',
            'definicao':'Quantidade de economias ativas de água, cujas respectivas ligações são providas de aparelho de medição. (hidrômetro) em funcionamento regular, que contribuíram para o faturamento no último mês do ano.',
            'unidade' : 'economias',
            'fonte' : 'SNIS',
        }),
        ('FR1', {
            'nome': 'Quantidade de Economias Residenciais Ativas de Água',
            'definicao': 'Quantidade de economias residenciais ativas de água que contribuíram para o faturamento no último mês do ano.',
            'unidade' : 'economias',
            'fonte' : 'SNIS',
        }),
        ('FV4', {
            'nome': 'Volume de Água Consumido (m³)',
            'definicao': 'Volume de água consumido por todos os usuários, compreendendo o volume micromedido, o volume estimado para as ligações desprovidas de aparelho de medição (hidrômetro) e o volume de água tratada exportado.',
            'unidade' : 'm³',
            'fonte' : 'SNIS',
        }),
        ('FV5', {
            'nome': 'Volume de Esgoto Coletado',
            'definicao':'Quantidade de esgoto direcionado ao sistema coletor de esgoto.',
            'unidade' : 'm³',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FV6', {
            'nome': 'Volume de Esgoto Coletado Tratado',
            'definicao': 'Quantidade de esgoto direcionado ao sistema coletor de esgoto e recebe tratamento.',
            'unidade' : 'm³',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FQ1', {
            'nome': 'Vazão de Água Tratada',
            'definicao': 'Vazão de água tratada em cada estação de tratamento disponibilizada para o consumo.',
            'unidade' : 'm³/s',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FQ2', {
            'nome': 'Vazão de Esgoto Tratado',
            'definicao': 'Vazão de esgoto tratado em cada estação ETE.',
            'unidade' : 'm³/s',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FQ3', {
            'nome': 'Vazão Nominal de Projeto da ETA',
            'definicao': 'Vazão, em condições normais de funcionamento, para a qual a ETA é projetada.',
            'unidade' : 'm³/ano',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FQ4', {
            'nome': 'Vazão Nominal de Projeto da ETE',
            'definicao': 'Vazão, em condições normais de funcionamento, para a qual a ETE é projetada.',
            'unidade' : 'm³/ano',
            'fonte' : 'Prestador de Serviço',
        }),
        ('FP1', {
            'nome': 'População Atingida',
            'definicao': 'População atingida por inundações,  deslizamento de solos, alagamentos, enxurradas, etc.',
            'unidade' : 'habitantes',
            'fonte' : 'Defesa Civil',
        }),
        ('FP2', {
            'nome': 'População Atingida nos Anos Anteriores',
            'definicao': 'População atingida por inundações,  deslizamento de solos, alagamentos e enxurradas em anos anterios.',
            'unidade' : 'habitantes',
            'fonte' : 'Defesa Civil',
        }),
        ('FM1', {
            'nome': 'Quantidade total de Resíduos Coletados',
            'definicao': 'Massa total de resíduos coletados, sendo eles de origem doméstico ou público.',
            'unidade' : 'toneladas',
            'fonte' : 'Prestador de Serviço/SNIS',
        }),
        ('FM2', {
            'nome': 'Quantidade de Materiais Recicláveis Recuperados',
            'definicao': 'Massa coletada de recicláveis recuperados, excetos os de origem doméstica e rejeitos.',
            'unidade' : 'toneladas',
            'fonte' : 'Prestador de Serviço/SNIS',
        }),
        ('FM3', {
            'nome': 'Quantidade de RCC coletado',
            'definicao': 'Massa coletada de resíduos da construção civil (RCC).',
            'unidade' : 'toneladas',
            'fonte' : 'Prestador de Serviço/SNIS',
        })
    ]
