import time
from datetime import datetime

def time_exec(func):
    def interno(*args, **kargs):
        inicio = time.time()
        result = func(*args, **kargs)
        fim = itme.time()
        print(func.__name__ + ' Executado em ' + str((fim-inicio)*1000 ) + 'milisegundos' )
    return interno()

@time_exec(cal_quadrato)
def cal_quadrado(numeros):
    resultado = []
    for numero in numeros:
        resultado.append(numero*numero)
    return resultado

@time_exec(cal_cubo)
def cal_cubo(numeros):
    resultado = []
    for numero in numeros:
        resultado.append(numero*numero*numero)
    return resultado

if __name__ == "__main__":
    lista_numeros = range(1,10000)
    print(datetiame.now())
    saida_quadrados = cal_quadrado(lista_numeros)
    saida_cubos = calc_cubo(lista_numeros)
    print(datetime.now())
