"""
Código,Nome,Definição,Unidade,FONTE

AE1,Quantidade de casos notificados de esquistossomose,Quantidade total anual de casos de esquistossomos notificados no Sistema de Informação de Agravos de Notificação(SINAN),Número de casos/ano,SINAN/ DATASUS

AD1,Quantidade de casos notificados de dengue,Quantidade total anual de casos de dengue notificados no Sistema de Informação de Agravos de Notificação(SINAN),Número de casos/ano,SINAN/ DATASUS

AH1,Quantidade de casos notificados de hepatite A,Quantidade total anual de casos de hepatite A notificados no Sistema de Informação de Agravos de Notificação(SINAN),Número de casos/ano,SINAN/ DATASUS

AL1,Quantidade de casos notificados de leptospirose,Quantidade total anual de casos de leptospirose notificados no Sistema de Informação de Agravos de Notificação(SINAN),Número de casos/ano,SINAN/ DATASUS
"""

AE1 = models.CharField(
    "Quantidade de casos notificados de esquistossomose", max_length=20, blank=True)
AD1 = models.CharField(
    "Quantidade de casos notificados de dengue", max_length=20, blank=True)
AH1 = models.CharField(
    "Quantidade de casos notificados de hepatite A", max_length=20, blank=True)
AL1 = models.CharField(
    "Quantidade de casos notificados de leptospirose", max_length=20, blank=True)
