lista_ejercicio = [66, 34, 79, 26, 83, 39, 32, 60, 22, 74, 37, 80, 82, 50, 73, 66, 31, 44, 33, 51]

def insertar_numero(numero, arbol):
    '''
    nodo = [valor, [hijo_izquierdo], [hijo_derecho]]

    Inserta un número al árbol binaro de búsqueda (pre definido).
    Si el número ingresado es menor o igual que el valor del nodo
    el número será insertado en el hijo izquierdo.
    Si el número ingresado es mayor que el valor del nodo
    el número será insertado en el hijo derecho.
    '''
    insertado = False
    actual = arbol

    while not insertado:
        if len(actual) > 0:
            if actual[0] > numero:
                actual = actual[1]
            else:
                actual = actual[2]
        else:
            actual.extend([numero, [], []])
            insertado = True

    return arbol

abb = []
for numero in lista_ejercicio:
    insertar_numero(numero, abb)

print(abb)