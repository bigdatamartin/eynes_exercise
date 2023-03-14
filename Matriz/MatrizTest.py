import Matriz

def test_generar_matriz():
    """
    >>> len(Matriz.generar_matriz())
    5
    """
    pass

def test_buscar_secuencia():
    """
    >>> Matriz.buscar_secuencia([[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5]]) == None
    True
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
