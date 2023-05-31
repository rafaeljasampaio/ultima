def ola(func):
    def inner():
        print("Ola ")
        func()
        print("Tudo bem? ")
    return inner


def nome():
    print("Alice")


print("Antes")
variavel_obj = ola(nome)
print("depois")
variavel_obj()
print("Final")


