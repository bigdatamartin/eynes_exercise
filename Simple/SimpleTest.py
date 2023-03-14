import Simple

def test_generar_lista_diccionarios():
    """
    >>> lista = Simple.generar_lista_diccionarios()
    >>> len(lista)
    10
    >>> all(isinstance(diccionario['id'], int) for diccionario in lista)
    True
    >>> all(isinstance(diccionario['edad'], int) and 1 <= diccionario['edad'] <= 100 for diccionario in lista)
    True
    """

def test_ordenar_lista_diccionarios():
    """
    >>> lista = Simple.generar_lista_diccionarios()
    >>> lista_ordenada = Simple.ordenar_lista_diccionarios(lista)
    >>> lista_ordenada[0]['edad'] >= lista_ordenada[-1]['edad']
    True
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
