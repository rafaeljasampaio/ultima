def decorator_imprimir(ca, ta, te):
    def registra(ca,ta, te):
        print(str(a) + " + " + str(b) + " é ", end="")
        return func(a,b)
    
    return registra
    

@logging_soma
def soma_ab(a,b):
    soma = a + b
    return soma


if __name__ == "__main__":
    a = int(5)
    b = int(3)
    valor = soma_ab(a,b)
    quardrado = valor ** 2


    print(valor)
    print(quardrado)
