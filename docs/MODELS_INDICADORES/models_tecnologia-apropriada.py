"""
CÓDIGO,NOME,DEFINIÇÃO,UNIDADE,FONTE

TA1,Tecnologia Adotada - Abastecimento de Água,"Verificar os tipos de tecnologia adotada no município: solução coletiva (sistema convencional) x solução individualizada (captação de água de chuva, cisternas, cacimbas, etc.)",Dado qualitativo (Descrição dos sistemas),Gestor do município

TE1,Tecnologia Adotada - Esgotamento Sanitário,"Verificar os tipos de tecnologia adotada no município: solução coletiva (sistema convencional) x solução individualizada (fossa séptica, sumidouro, disposição a céu aberto, etc.)",Dado qualitativo (Descrição dos sistemas),Gestor do município

TR1,Tecnologia Adotada - Resíduos Sólidos,"Verificar os tipos de tecnologia adotada no município: solução coletiva (coleta pública e periódica dos resíduos domésticos) x solução individualizada (enterrar, queimar ou dispor em terreno baldio os resíduos domésticos).",Dado qualitativo (Descrição dos sistemas),Gestor do município

TR2,Tecnologia Adotada - Resíduos Sólidos,"Verificar a existência de coleta seletiva, bem como a proporção com relação á coleta convencional.",Dado qualitativo (Descrição dos sistemas),Gestor do município

TD1,Tecnologia Adotada - Manejo de águas pluviais,"Verificar a existência de microdrenagem e macrodrenagem, por sistemas convencionais: sarjeta, bueiros, etc.",Dado qualitativo (Descrição dos sistemas),Gestor do município

TD2,Tecnologia Adotada - Resíduos Sólidos,"Verificar se há soluções sustentáveis de drenagem como: bacia de amortecimento, pavimentação permeável, coleta de água de chuva, preservação dos leitos naturais dos rios, manutenção da cobertura vegetal e ou outros.",Dado qualitativo (Descrição dos sistemas),Gestor do município
"""

TA1 = models.CharField(
    "Tecnologia Adotada - Abastecimento de Água", max_length=20, blank=True)
TE1 = models.CharField(
    "Tecnologia Adotada - Esgotamento Sanitário", max_length=20, blank=True)
TR1 = models.CharField(
    "Tecnologia Adotada - Resíduos Sólidos", max_length=20, blank=True)
TR2 = models.CharField(
    "Tecnologia Adotada - Resíduos Sólidos", max_length=20, blank=True)
TD1 = models.CharField(
    "Tecnologia Adotada - Manejo de águas pluviais", max_length=20, blank=True)
TD2 = models.CharField(
    "Tecnologia Adotada - Resíduos Sólidos", max_length=20, blank=True)
