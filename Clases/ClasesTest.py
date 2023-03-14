import Clases

def test_circulo():
    """
    >>> c1 = Clases.Circulo(5)
    >>> c1.radio
    5
    >>> c1.radio = 7
    >>> c1.radio
    7
    >>> c1.area()
    153.93804002589985
    >>> c1.perimetro()
    43.982297150257104
    >>> print(c1)
    Circulo de radio 7
    >>> repr(c1)
    'Circulo(7)'
    >>> c2 = c1 * 2
    >>> c2.radio
    14
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)