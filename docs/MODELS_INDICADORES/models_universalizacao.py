"""
CÓDIGO,NOME,DEFINIÇÃO,UNIDADE,FONTE

PT1,População Total do município,"Número total de habitantes no município incluindo zona urbana e rural, tanto a população servida quanto a que não é servida pelos serviços.",Habitantes,IBGE

PU1,População Urbana do Município (Sede Municipal),"Número de habitantes no município que residem na zona urbana, tanto a população servida quanto a que não é servida pelos serviços.",Habitantes,IBGE

PU2,População Rural do Município ,"Número de habitantes no município que residem na zona rural, tanto a população servida quanto a que não é servida pelos serviços.",Habitantes,IBGE

PA1,População atendida com abastecimento de água,"Número total de habitantes a que o prestador fornece serviços de abastecimento de água, seja na sede municipal ou localidades.",Habitantes,IBGE

PA2,População urbana atendida com abastecimento de água,Número total de habitantes da zona urbana a que o prestador fornece serviços de abastecimento de água.,Habitantes,IBGE

PA3,População rural atendida com abastecimento de água,Número total de habitantes da zona rural a que o prestador fornece serviços de abastecimento de água.,Habitantes,IBGE

PA4,População atendida com abastecimento de água por soluções individualizadas,"Número total de habitantes que adota uma solução individualizada como aproveitamento da água de chuvas, cisternas, etc.",Habitantes,IBGE

PE1,População atendida por rede de esgotamento sanitário,"Número total de habitantes com acesso ao serviço de coleta de esgotos, seguida de tratamento, realizado pelo prestador de serviços, seja na sede municipal ou localidades.",Habitantes,IBGE

PE2,População urbana atendida por rede de esgotamento sanitário,"Número total de habitantes da zona urbana com acesso ao serviço de coleta de esgotos, seguida de tratamento, realizado pelo prestador de serviços, seja na sede municipal ou localidades.",Habitantes,IBGE

PE3,População rural atendida por rede de esgotamento sanitário,"Número total de habitantes da zona rural com acesso ao serviço de coleta de esgotos, seguida de tratamento, realizado pelo prestador de serviços.",Habitantes,IBGE

PE4,População atendida por soluções individuais de esgotamento sanitário,"População atendida por algum tipo de solução individualizada para a destinação do esgoto doméstico: fossa séptica, dentre outros (conforme Relatório Técnico Participativo).",Habitantes,IBGE

PE5,População urbana atendida por soluções individuais de esgotamento sanitário,"População urbana atendida por algum tipo de solução individualizada para a destinação do esgoto doméstico: fossa séptica, dentre outros (conforme Relatório Técnico Participativo).",Habitantes,IBGE

PR1,População com acesso à coleta de Resíduo Sólido,População atendida pela coleta pública de resíduos sólidos.,Habitantes,IBGE

PR2,População urbana com acesso à coleta de Resíduo Sólido,População urbana atendida pela coleta pública de resíduos sólidos.,Habitantes,IBGE

PR3,População rural com acesso à coleta de Resíduo Sólido,População urural atendida pela coleta pública de resíduos sólidos,Habitantes,IBGE

LD1,Quantidade de Logradouros com algum tipo de solução de drenagem (para todo o município).,"Quantidade de logradouros atendidos por sistema de drenagem urbana, tais como: micro drenagem e macro drenagem (condutos e dispositivos projetados em função do plano de arruamento).","Quantidade de Logradouros",Gestor 

LT1,Quantidade total logradouros (para todo o município).,Quantidade total de logradouros do município,"Quantidade de Logradouros",Gestor

DT1,Domicílio Total do município,Número total de domicílios  no município incluindo zona urbana e rural,Domicílios,IBGE

DU1,Domicílios urbanos do município,Número total de domicílios  no município que residem na zona urbana.,Domicílios,IBGE

DU2,Domicílio rurais do município,Número total de domicílios  no município que residem na zona rural.,Domicílios,IBGE

DA1,Domicílios atentidos com abastecimento de água pelo prestador de serviços,"Número total de domicpilios a que o prestador fornece serviços de abastecimento de água, seja na sede municipal ou localidades.",Domicílios,IBGE

DA2,Domicilios urbanos atendidos com abastecimento de água pelo prestador de serviços,Número total de domicílios da zona urbana a que o prestador fornece serviços de abastecimento de água.,Domicílios,IBGE

DA3,Domicílios rural atendidos com abastecimento de água pelo prestador de serviços ,Número total de domicílios da zona rural a que o prestador fornece serviços de abastecimento de água.,Domicílios,IBGE

DE1,Domicílios atentidos por rede de esgotamento sanitário,Número total de domicílios servidos por rede coletora ou fossa séptica.,Domicílios ,IBGE

DE2,Domicílios urbanos atendidos por rede de esgotamento sanitário,Número total de domicílios urbano servidos por rede coletora ou fossa séptica.,Domicílios,IBGE

DE3,Domicílios rurais atendidos por rede de esgotamento sanitário,Número total de domicílios rurais servidos por rede coletora ou fossa séptica.,Domicílios,IBGE

DE4,Domicilios que possuem banheiros  ,Número de domícilos que possuem banheiros (chuveiro ou banheira e vaso sanitário) ,Domicílios ,IBGE

DR1,Domicílios atendidos por coleta direta,Domicílios urbanos  e rurais atendidos por coleta direta (porta-a-porta),Domicílios,IBGE

DR2,Domicílios urbanos atendidos por coleta direta,Domicílios urbanos atendidos por coleta direta (porta-a-porta),Domicílios,IBGE

DR3,Domicílios rurais atendidos por coleta direta,Domicílios rurais atendidos por coleta direta (porta-a-porta),Domicílios,IBGE
"""

PT1 = models.CharField("População Total do município",
                       max_length=20, blank=True)
PU1 = models.CharField(
    "População Urbana do Município (Sede Municipal)", max_length=20, blank=True)
PU2 = models.CharField("População Rural do Município ",
                       max_length=20, blank=True)
PA1 = models.CharField(
    "População atendida com abastecimento de água", max_length=20, blank=True)
PA2 = models.CharField(
    "População urbana atendida com abastecimento de água", max_length=20, blank=True)
PA3 = models.CharField(
    "População rural atendida com abastecimento de água", max_length=20, blank=True)
PA4 = models.CharField(
    "População atendida com abastecimento de água por soluções individualizadas", max_length=20, blank=True)
PE1 = models.CharField(
    "População atendida por rede de esgotamento sanitário", max_length=20, blank=True)
PE2 = models.CharField(
    "População urbana atendida por rede de esgotamento sanitário", max_length=20, blank=True)
PE3 = models.CharField(
    "População rural atendida por rede de esgotamento sanitário", max_length=20, blank=True)
PE4 = models.CharField(
    "População atendida por soluções individuais de esgotamento sanitário", max_length=20, blank=True)
PE5 = models.CharField(
    "População urbana atendida por soluções individuais de esgotamento sanitário", max_length=20, blank=True)
PR1 = models.CharField(
    "População com acesso à coleta de Resíduo Sólido", max_length=20, blank=True)
PR2 = models.CharField(
    "População urbana com acesso à coleta de Resíduo Sólido", max_length=20, blank=True)
PR3 = models.CharField(
    "População rural com acesso à coleta de Resíduo Sólido", max_length=20, blank=True)
LD1 = models.CharField(
    "Quantidade de Logradouros com algum tipo de solução de drenagem (para todo o município).", max_length=20, blank=True)
LT1 = models.CharField(
    "Quantidade total logradouros (para todo o município).", max_length=20, blank=True)
DT1 = models.CharField("Domicílio Total do município",
                       max_length=20, blank=True)
DU1 = models.CharField("Domicílios urbanos do município",
                       max_length=20, blank=True)
DU2 = models.CharField("Domicílio rurais do município",
                       max_length=20, blank=True)
DA1 = models.CharField(
    "Domicílios atentidos com abastecimento de água pelo prestador de serviços", max_length=20, blank=True)
DA2 = models.CharField(
    "Domicilios urbanos atendidos com abastecimento de água pelo prestador de serviços", max_length=20, blank=True)
DA3 = models.CharField(
    "Domicílios rural atendidos com abastecimento de água pelo prestador de serviços ", max_length=20, blank=True)
DE1 = models.CharField(
    "Domicílios atentidos por rede de esgotamento sanitário", max_length=20, blank=True)
DE2 = models.CharField(
    "Domicílios urbanos atendidos por rede de esgotamento sanitário", max_length=20, blank=True)
DE3 = models.CharField(
    "Domicílios rurais atendidos por rede de esgotamento sanitário", max_length=20, blank=True)
DE4 = models.CharField(
    "Domicilios que possuem banheiros  ", max_length=20, blank=True)
DR1 = models.CharField(
    "Domicílios atendidos por coleta direta", max_length=20, blank=True)
DR2 = models.CharField(
    "Domicílios urbanos atendidos por coleta direta", max_length=20, blank=True)
DR3 = models.CharField(
    "Domicílios rurais atendidos por coleta direta", max_length=20, blank=True)
