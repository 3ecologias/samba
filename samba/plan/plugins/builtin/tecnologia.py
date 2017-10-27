from samba.plan.plugins import Plugin


class TecnologiaApropiada(Plugin):
    nome = 'Tecnologia Apropriada'
    descricao = '''
    Conjunto de indicadores que a permitem avaliar a
    solução tratada de acordo com a realidade local.
    '''
    icone_loja = '/static/icons/256x256/Colorido/tecnologia_apropriada.svg'
    icone_sidebar = '/static/icons/16x16/Colorido/tecnologia_apropriada.svg'
    indicadores = [
        ('TA1', {
            'nome': 'Tecnologia Adotada - Abastecimento de Água',
            'definicao': 'Verificar os tipos de tecnologia adotada no município: solução coletiva (sistema convencional) x solução individualizada (captação de água de chuva, cisternas, cacimbas, etc.).',
            'escolhas': ['', 'Solução Coletiva', 'Solução Individualizada'],
            'multipla_escolha': True,
            'exige_descricao' : True,
            'fonte' : 'Gestor do município',
        }),
        ('TE1', {
            'nome': 'Tecnologia Adotada - Esgotamento Sanitário',
            'definicao': 'Verificar os tipos de tecnologia adotada no município: solução coletiva (sistema convencional) x solução individualizada (fossa séptica, sumidouro, disposição a céu aberto, etc.).',
            'escolhas': ['', 'Solução Coletiva', 'Solução Individualizada'],
            'multipla_escolha': True,
            'fonte' : 'Gestor do município',
            'exige_descricao' : True,
        }),
        ('TR1', {
            'nome': 'Tecnologia Adotada - Resíduos Sólidos',
            'definicao': 'Verificar os tipos de tecnologia adotada no município: solução coletiva (coleta pública e periódica dos resíduos domésticos) x solução individualizada (enterrar, queimar ou dispor em terreno baldio os resíduos domésticos).',
            'escolhas': ['', 'Solução Coletiva', 'Solução Individualizada'],
            'multipla_escolha': True,
            'fonte' : 'Gestor do município',
            'exige_descricao' : True,
        }),
        ('TR2', {
            'nome': 'Tecnologia Adotada - Resíduos Sólidos - Coleta Seletiva',
            'definicao': 'Verificar a existência de coleta seletiva, bem como a proporção com relação á coleta convencional.',
            'escolhas': ['', 'Sim', 'Não'],
            'fonte' : 'Gestor do município',
            'exige_descricao' : True,
        }),
        ('TD1', {
            'nome': 'Tecnologia Adotada - Manejo de águas pluviais - Infraestrutura básica',
            'definicao': 'Verificar a existência de microdrenagem e macrodrenagem, por sistemas convencionais: sarjeta, bueiros, etc.',
            'escolhas': ['', 'Sistema de Microdrenagem', 'Sistema de Macrodrenagem'],
            'multipla_escolha': True,
            'fonte' : 'Gestor do município',
            'exige_descricao' : True,
        }),
        ('TD2', {
            'nome': 'Tecnologia Adotada - Manejo de Águas Pluviais - Soluções de Prevenção',
            'definicao': 'Verificar se há soluções sustentáveis de drenagem como: bacia de amortecimento, pavimentação permeável, coleta de água de chuva, preservação dos leitos naturais dos rios, manutenção da cobertura vegetal e ou outros.',
            'escolhas': [
                'Bacia de amortecimento',
                'Pavimentação permeável',
                'Coleta de água de chuva',
                'Preservação dos leitos naturais dos rios',
                'Manutenção da cobertura vegetal',
                'Outras'
            ],
            'multipla_escolha': True,
            'fonte' : 'Gestor do município',
            'exige_descricao' : True,
        })
    ]
