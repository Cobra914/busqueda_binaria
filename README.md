# busqueda_binaria
Búsqueda Binaria

¿Recuerdas los árboles binarios que utilizamos para simplificar la búsqueda y que resolvimos con listas de listas? Por si no te acuerdas, aquí tienes de nuevo la definición:

Un árbol binario es una estructura de datos en la cual cada nodo tiene un valor y puede como máximo dos hijos que se denominan hijo izquierdo e hijo derecho. Un nodo no puede tener más de dos hijos (por eso el nombre de binario) pero puede tener menos, es decir, solamente puede tener cero, uno o dos hijos.

Si hacemos que, para cualquier nodo, todos los valores almacenados en el hijo izquierdo sean menores que el valor de ese nodo y que todos los valores almacenados en el hijo derecho sean mayores que el valor del nodo, tenemos un árbol binario de búsqueda (ABB).

Si un nodo no tiene hijos, se denomina nodo externo, en otro caso se denomina nodo interno.

Ahora usaremos clases para representarlo. Para ello vamos a usar "composición", es decir, vamos a hacer que una clase tenga atributos que sean a su vez clases.

1. Crea una clase que represente un nodo de un árbol binario de forma que debe tener un valor, un hijo izquierdo y un hijo derecho. Evidentemente, los hijos son opcionales, pero es evidente que son a su vez de tipo nodo. Es decir, un nodo está compuesto a su vez por dos nodos más.

2. Agrega a la clase un método buscar que permita encontrar un valor en el árbol aprovechando las ventajas de un árbol binario de búsqueda.

    * En caso de encontrarlo, el método devolverá el nodo (completo, es decir, un sub-árbol)
    * En caso de que no esté en el árbol, devolverá el valor None.

3. Agrega un método insertar que permita agregar un valor en el árbol de forma automática.

4. Agrega un atributo coste_ultima_busqueda a la clase que almacene el número de nodos consultados para realizar la búsqueda.

## ¿Quieres más retos?

1. Agrega un método que elimine un nodo
2. Agrega un método para obtener el número mayor en el árbol. ¿Cuántos nodos has tenido que consultar?
3. Haz lo mismo, pero esta vez para el mínimo
4. ¿Puedes obtener la suma de todos los nodos?
5. ¿Y contar los valores que hay almacenados en el árbol?
6. ¿Crees que podrías imprimir los valores ordenados por su valor?

## Ayuda a la implementación

Para que te resulte más fácil ver que las cosas funcionan prueba a incluir dos métodos extra para ver los valores del árbol:

* Utiliza el método __repr__() para devolver el valor del nodo como una cadena de texto. Eso te permitirá imprimir un nodo en la pantalla
* Crea un método mostrar_arbol() que, partiendo del nodo actual muestre el contenido del ábol, así verás el contenido para ver que los métodos funcionan como deben.
* Si quieres utilizar datos de ejemplo, puedes utilizar este fragmento de código para crear un árbol:
```
valores = [66, 34, 79, 26, 83, 39, 32, 60, 22, 74, 37, 80, 82, 50, 73, 31, 44, 33, 51]
arbol = Abb(valores[0])
for indice in range(1, len(valores)):
  arbol.insertar(valores[indice])
```

El método mostrar_arbol() devolverá la siguiente lista:
```
[66, 34, 26, 22, 32, 31, 33, 39, 37, 60, 50, 44, 51, 79, 74, 73, 83, 80, 82]
```
