def mostrar(func):
    def interno(a, b):
        print(a + " está " + b)
        return func(a,b)
    
    return interno


#def quem(a,b):

a = "Alice"
b = "eviando email"

if __name__ == "__main__":

    mostrar(a, b)


#myobj = mostrar(quem)
#myobj()

#quem()


