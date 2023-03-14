def generar_matriz():
    import random
    matriz = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

def buscar_secuencia(matriz):
    for i in range(5):
        for j in range(2):
            if matriz[i][j] == matriz[i][j+1] == matriz[i][j+2] == matriz[i][j+3]:
                return (i, j), (i, j+3)
    
    for j in range(5):
        for i in range(2):
            if matriz[i][j] == matriz[i+1][j] == matriz[i+2][j] == matriz[i+3][j]:
                return (i, j), (i+3, j)
    
    return None

if __name__ == '__main__':
    matriz = generar_matriz()
    print("Matriz generada:")
    for fila in matriz:
        print(fila)
    
    resultado = buscar_secuencia(matriz)
    if resultado:
        print("Se encontró una secuencia de 4 números consecutivos:")
        print(f"Posición inicial: {resultado[0]}")
        print(f"Posición final: {resultado[1]}")
    else:
        print("No se encontró ninguna secuencia de 4 números consecutivos.")
