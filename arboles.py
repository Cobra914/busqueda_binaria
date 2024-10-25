class Nodo:
    """
    """
    def __init__(self, padre, hijo_izq, hijo_der):
        self.padre = padre
        self.hijo_izq = hijo_izq
        self.hijo_der = hijo_der
        self.nodo = [padre, hijo_izq, hijo_der]

    def __repr__(self):
        return f"El nodo es {self.nodo}"







if __name__ == "__main__":
    
    nodo = Nodo(1,2,3)
    print(nodo)
