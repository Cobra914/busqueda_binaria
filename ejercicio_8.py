arbol_binario = [
  1,
  [7,
    [2,
      [],
      []],
    [6, 
      [5,
        [],
        []],
      [11,
        [],
        []]]],
    [9,
      [],
      [9, 
        [5,
          [],
          []],
        []]]
]


def buscar_mayor(arbol):
    '''
    Devuelve el valor mayor contenido en un árbol
    '''
    mayor = arbol[0]

    for elemento in arbol:
        if isinstance(elemento, int):
            if elemento >= mayor:
                mayor = elemento
        elif isinstance(elemento, list) and elemento != []:
            mayor_valor = buscar_mayor(elemento)
            if mayor_valor >= mayor:
                mayor = mayor_valor

    return mayor

      


l = buscar_mayor(arbol_binario)
print(l)
