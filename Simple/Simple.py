def generar_lista_diccionarios():
    import random
    lista = []
    for i in range(10):
        diccionario = {
            'id': i,
            'edad': random.randint(1, 100)
        }
        lista.append(diccionario)
    return lista


def ordenar_lista_diccionarios(lista):
    return sorted(lista, key=lambda x: x['edad'], reverse=True)
