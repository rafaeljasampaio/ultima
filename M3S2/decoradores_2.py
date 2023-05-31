def maiusculo(texto):
    return texto.upper()

def minusculo(texto):
    return texto.lower()

def mensagem(funcao):
    texto = funcao("ultima School")
    print(texto)


mensagem(maiusculo)
mensagem(minusculo)
