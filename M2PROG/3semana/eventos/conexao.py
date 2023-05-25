class conexao_open():
    import sqlite3
    conexao = sqlite3.connect('bdevento.sqlite3')
    cursor = conexao.cursor()
    conexao.commit()
    conexao.close()

