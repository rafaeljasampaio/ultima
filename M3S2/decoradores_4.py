def comprimento(funcao):
    def saudacao():
        print("Bom dia!")
        funcao()
        print("Boa Noite!")
    return saudacao

@comprimento
def boa_tarde():
    print("Boa Tarde!")

boa_tarde()