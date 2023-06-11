







def decorador_imprimir(func):

    def imprime(capital,taxa,tempo):
        func = print(f'Capital:{capital}\n',
                     f'Taxa:{taxa}\n',
                     f'Tempo:{tempo}\n',
                     f'Resultado: {capital*(taxa/100)*tempo}'
                     )
    return imprime

@decorador_imprimir
def juros_simples(capital,taxa,tempo):
    return capital*(taxa/100)*tempo

print(juros_simples(70,40,90))
