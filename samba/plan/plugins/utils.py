def porcentagem(margem, total):
    """
    Retorna uma função que calcula a porcentagem de
    dois indicadores em um plano.
    """
    def calcular(indicador):
        valor_margem = indicador(margem)
        valor_total = indicador(total)

        if valor_margem is None or valor_total is None:
            return None

        if valor_margem > 0 and valor_total > 0:

            return (valor_margem * 100) / valor_total
        else:
            return None

    return calcular

def pormil(margem, total):
    """
    Retorna uma função que calcula a por mil de
    dois indicadores em um plano.
    """
    def calcular(indicador):
        valor_margem = indicador(margem)
        valor_total = indicador(total)

        if valor_margem is None or valor_total is None:
            return None

        return (valor_margem * 1000) / valor_total

    return calcular

def divisao(numerator, denominator):
    """
    Retorna uma função que calcula a divisão
    dois indicadores em um plano.
    """
    def calcular(indicador):
        valor_numerator = indicador(numerator)
        valor_denominator = indicador(denominator)

        if valor_numerator is None or valor_denominator is None:
            return None

        return (valor_numerator * 1000) / valor_denominator

    return calcular
