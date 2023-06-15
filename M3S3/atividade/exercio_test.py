from exercicio1 import TotalProduto

def TestTotalProduto():
    assert valor_com_desconto(5, 10) == 47.50
    assert valor_sem_desconto(5, 10) == 50.00
