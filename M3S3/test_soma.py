from soma import SomaDoisNumeros

def test_soma():
    assert SomaDoisNumeros(2, 5) == 7
    assert SomaDoisNumeros(-5, 5) == 0
    assert SomaDoisNumeros(0, 0) == 0
