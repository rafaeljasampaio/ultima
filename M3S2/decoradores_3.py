def somador(x):
    def soma(y):
        return x+y

    return soma

resultado = somador(15)

print(resultado(10))


