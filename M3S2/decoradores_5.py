def primeiro_decorador(func):
    def primeira_func():
        print("Execução antes da função")
        func()
        print("Execução depois da função")
    return primeira_func

def funcao_utilizadora():
    print("Priciso utilizar o decorator")

final = primeiro_decorador(funcao_utilizadora)

final()

