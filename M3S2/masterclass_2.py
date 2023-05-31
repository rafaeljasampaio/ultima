def mostrar(func):
    def interno():
        print("O usuário atual é: ", end="")
        func()
    return interno


def quem():
    print("Alice")

myobj = mostrar(quem)
myobj()



