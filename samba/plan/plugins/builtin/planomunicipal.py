from samba.plan.plugins import Plugin


class PlanoMunicipal(Plugin):
    nome = 'Implementação'
    descricao = '''
Conjunto de indicadores que permitem traçar um panorama da realização do PMSB de seu município.
    '''
    icone_loja = 'icons/256x256/Colorido/implementacao_do_plano_municipal.svg'
    icone_sidebar = 'icons/16x16/Colorido/implementacao_do_plano_municipal.svg'
    indicadores = [
        ('CA1', {
            'nome': 'Total de ações emergenciais de abastecimento de água',
            'unidade' : 'ações emergenciais',
            'definicao': 'Número de ações, para o serviço de abastecimento de água, previstas para serem realizadas emergencialmente.',
            'fonte' : 'PMSB',
        }),
        ('CA2', {
            'nome': 'Total de ações de curto prazo de abastecimento de água',
            'unidade' : 'ações de curto prazo',
            'definicao': 'Número de ações, para o serviço de abastecimento de água, previstas para serem realizadas em curto prazo.',
            'fonte' : 'PMSB',
        }),
        ('CA3', {
            'nome': 'Total de ações de médio prazo de abastecimento de água',
            'unidade' : 'ações de médio prazo',
            'definicao': 'Número de ações, para o serviço de abastecimento de água, previstas para serem realizadas em médio prazo.',
            'fonte' : 'PMSB',
        }),
        ('CA4', {
            'nome': 'Total de ações de longo prazo de abastecimento de água',
            'unidade' : 'ações de longo prazo',
            'definicao': 'Número de ações, para o serviço de abastecimento de água, previstas para serem realizadas em longo prazo.',
            'fonte' : 'PMSB',
        }),
        ('CA5', {
            'nome': 'Total de ações emergenciais de abastecimento de água implementadas',
            'unidade' : 'ações emergenciais implementadas',
            'definicao': 'Número de ações emergenciais, para o serviço de abastecimento de água, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CA6', {
            'nome': 'Total de ações de curto prazo de abastecimento de água implementadas',
            'unidade' : 'ações de curto prazo implementadas',
            'definicao': 'Número de ações de curto prazo, para o serviço de abastecimento de água, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CA7', {
            'nome': 'Total de ações de médio prazo de abastecimento de água implementadas',
            'unidade' : 'ações de médio prazo implementadas',
            'definicao': 'Número de ações de médio prazo, para o serviço de abastecimento de água, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CA8', {
            'nome': 'Total de ações de longo prazo de abastecimento de água implementadas',
            'unidade' : 'ações de longo prazo implementadas',
            'definicao': 'Número de ações de longo prazo, para abastecimento de água, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CE1', {
            'nome': 'Total de ações emergenciais de esgotamento sanitário',
            'unidade' : 'ações emergenciais',
            'definicao': 'Número de ações, para o serviço de esgotamento sanitário, previstas para serem realizadas emergencialmente.',
            'fonte' : 'PMSB',
        }),
        ('CE2', {
            'nome': 'Total de ações de curto prazo de esgotamento sanitário',
            'unidade' : 'ações de curto prazo',
            'definicao': 'Número de ações, para o serviço de esgotamento sanitário, previstas para serem realizadas em curto prazo.',
            'fonte' : 'PMSB',
        }),
        ('CE3', {
            'nome': 'Total de ações de médio prazo de esgotamento sanitário',
            'unidade' : 'ações de médio prazo',
            'definicao': 'Número de ações, para o serviço de esgotamento sanitário, previstas para serem realizadas em médio prazo.',
            'fonte' : 'PMSB',
        }),
        ('CE4', {
            'nome': 'Total de ações de longo prazo de esgotamento sanitário',
            'unidade' : 'ações de longo prazo',
            'definicao': 'Número de ações, para o serviço de esgotamento sanitário, previstas para serem realizadas em longo prazo.',
            'fonte' : 'PMSB',
        }),
        ('CE5', {
            'nome': 'Total de ações emergenciais de esgotamento sanitário implementadas',
            'unidade' : 'ações emergenciais implementadas',
            'definicao': 'Número de ações emergenciais, para o serviço de esgotamento sanitário, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CE6', {
            'nome': 'Total de ações de curto prazo de esgotamento sanitário implementadas',
            'unidade' : 'ações de curto prazo implementadas',
            'definicao': 'Número de ações de curto prazo, para o serviço de esgotamento sanitário, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CE7', {
            'nome': 'Total de ações de médio prazo de esgotamento sanitário implementadas',
            'unidade' : 'ações de médio prazo implementadas',
            'definicao': 'Número de ações de médio prazo, para o serviço de esgotamento sanitário, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CE8', {
            'nome': 'Total de ações de longo prazo de abastecimento de água implementadas',
            'unidade' : 'ações de longo prazo implementadas',
            'definicao': 'Número de ações de longo prazo, para o serviço de abastecimento de água, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CR1', {
            'nome': 'Total de ações emergenciais de resíduos sólidos',
            'unidade' : 'ações emergenciais',
            'definicao': 'Número de ações, para o manejo dos resíduos sólidos e limpeza urbana, previstas para serem realizadas emergencialmente.',
            'fonte' : 'PMSB',
        }),
        ('CR2', {
            'nome': 'Total de ações de curto prazo de resíduos sólidos',
            'unidade' : 'ações de curto prazo',
            'definicao': 'Número de ações, para o manejo dos resíduos sólidos e limpeza urbana, previstas para serem realizadas em curto prazo.',
            'fonte' : 'PMSB',
        }),
        ('CR3', {
            'nome': 'Total de ações de médio prazo de resíduos sólidos',
            'unidade' : 'ações de médio prazo',
            'definicao': 'Número de ações, para o manejo dos resíduos sólidos e limpeza urbana, previstas para serem realizadas em médio prazo.',
            'fonte' : 'PMSB',
        }),
        ('CR4', {
            'nome': 'Total de ações de longo prazo de resíduos sólidos',
            'unidade' : 'ações de longo prazo',
            'definicao': 'Número de ações, para o manejo dos resíduos sólidos e limpeza urbana, previstas para serem realizadas em longo prazo.',
            'fonte' : 'PMSB',
        }),
        ('CR5', {
            'nome': 'Total de ações emergenciais de resíduos sólidos implementadas',
            'unidade' : 'ações emergenciais implementadas',
            'definicao': 'Número de ações emergenciais,  para o manejo dos resíduos sólidos e limpeza urbana, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CR6', {
            'nome': 'Total de ações de curto prazo de resíduos sólidos implementadas',
            'unidade' : 'ações de curto prazo implementadas',
            'definicao': 'Número de ações de curto prazo,  para o manejo dos resíduos sólidos e limpeza urbana, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CR7', {
            'nome': 'Total de ações de médio prazo de resíduos sólidos implementadas',
            'unidade' : 'ações de médio prazo implementadas',
            'definicao': 'Número de ações de médio prazo,  para o manejo dos resíduos sólidos e limpeza urbana, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CR8', {
            'nome': 'Total de ações de longo prazo de resíduos sólidos implementadas',
            'unidade' : 'ações de longo prazo implementadas',
            'definicao': 'Número de ações de longo prazo,  para o manejo dos resíduos sólidos e limpeza urbana, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CD1', {
            'nome': 'Total de ações emergenciais de drenagem urbana e manejo das águas pluviais',
            'unidade' : 'ações emergenciais',
            'definicao': 'Número de ações, para o serviço de drenagem urbana e manejo das águas pluviais, previstas para serem realizadas emergencialmente.',
            'fonte' : 'PMSB',
        }),
        ('CD2', {
            'nome': 'Total de ações de curto prazo de drenagem urbana e manejo das águas pluviais',
            'unidade' : 'ações de curto prazo',
            'definicao': 'Número de ações, para o serviço de drenagem urbana e manejo das águas pluviais, previstas para serem realizadas em curto prazo.',
            'fonte' : 'PMSB',
        }),
        ('CD3', {
            'nome': 'Total de ações de médio prazo de drenagem urbana e manejo das águas pluviais',
            'unidade' : 'ações de médio prazo',
            'definicao': 'Número de ações, para o serviço de drenagem urbana e manejo das águas pluviais, previstas para serem realizadas em médio prazo.',
            'fonte' : 'PMSB',
        }),
        ('CD4', {
            'nome': 'Total de ações de longo prazo de drenagem urbana e manejo das águas pluviais',
            'unidade' : 'ações de longo prazo',
            'definicao': 'Número de ações, para o serviço de drenagem urbana e manejo das águas pluviais, previstas para serem realizadas em longo prazo.',
            'fonte' : 'PMSB',
        }),
        ('CD5', {
            'nome': 'Total de ações emergenciais de drenagem urbana e manejo das águas pluviais implementadas',
            'unidade' : 'ações emergenciais implementadas',
            'definicao': 'Número de ações emergenciais para o serviço de drenagem urbana e manejo das águas pluviais, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CD6', {
            'nome': 'Total de ações de curto prazo de drenagem urbana e manejo das águas pluviais implementadas',
            'unidade' : 'ações de curto prazo implementadas',
            'definicao': 'Número de ações de curto prazo, para  o serviço de drenagem urbana e manejo das águas pluviais, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CD7', {
            'nome': 'Total de ações de médio prazo de drenagem urbana e manejo das águas pluviais implementadas',
            'unidade' : 'ações de médio prazo implementadas',
            'definicao': 'Número de ações de médio prazo, para  o serviço de drenagem urbana e manejo das águas pluviais, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CD8', {
            'nome': 'Total de ações de longo prazo de drenagem urbana e manejo das águas pluviais implementadas',
            'unidade' : 'ações de longo prazo implementadas',
            'definicao': 'Número de ações de longo prazo, para o serviço de drenagem urbana e manejo das águas pluviais, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CG1', {
            'nome': 'Total de ações emergenciais de gestão dos serviços públicos',
            'unidade' : 'ações emergenciais',
            'definicao': 'Número de ações, para a gestão dos serviços públicos, previstas para serem realizadas emergencialmente.',
            'fonte' : 'PMSB',
        }),
        ('CG2', {
            'nome': 'Total de ações de curto prazo de gestão dos serviços públicos',
            'unidade' : 'ações de curto prazo',
            'definicao': 'Número de ações, para a gestão dos serviços públicos, previstas para serem realizadas em curto prazo.',
            'fonte' : 'PMSB',
        }),
        ('CG3', {
            'nome': 'Total de ações de médio prazo de gestão dos serviços públicos',
            'unidade' : 'ações de médio prazo',
            'definicao': 'Número de ações, para a gestão dos serviços públicos das águas pluviais , previstas para serem realizadas em médio prazo.',
            'fonte' : 'PMSB',
        }),
        ('CG4', {
            'nome': 'Total de ações de longo prazo de gestão dos serviços públicos',
            'unidade' : 'ações de longo prazo',
            'definicao': 'Número de ações, para a gestão dos serviços públicos, previstas para serem realizadas em longo prazo.',
            'fonte' : 'PMSB',
        }),
        ('CG5', {
            'nome': 'Total de ações emergenciais de gestão dos serviços públicos implementadas',
            'unidade' : 'ações emergenciais implementadas',
            'definicao': 'Número de ações emergenciais, para a gestão dos serviços públicos, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CG6', {
            'nome': 'Total de ações de curto prazo de gestão dos serviços públicos implementadas',
            'unidade' : 'ações de curto prazo implementadas',
            'definicao': 'Número de ações de curto prazo, para a gestão dos serviços públicos, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CG7', {
            'nome': 'Total de ações de médio prazo de gestão dos serviços públicos implementadas',
            'unidade' : 'ações de médio prazo implementadas',
            'definicao': 'Número de ações de médio prazo, para a gestão dos serviços públicos, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
        ('CG8', {
            'nome': 'Total de ações de longo prazo de gestão dos serviços públicos implementadas',
            'unidade' : 'ações de longo prazo implementadas',
            'definicao': 'Número de ações de longo prazo, para a gestão dos serviços públicos, que foram implementadas.',
            'fonte' : 'PMSB',
        }),
    ]
