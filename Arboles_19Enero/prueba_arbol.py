class NodoArbol:
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def recorrido_prefijo(self):
        print(self.data)
        aux = self.left
        for nodo in range (5):
            if aux != None:
                print(aux.data)
                aux = aux.left
        aux = self.right
        for nodo in range (5):
            if aux != None:
                print(aux.data)
                aux = aux.right

    def recorrido_sufijo(self):
        aux = self.left
        i = 1
        for nodo in range(5):
            if aux != None:
                print(aux.data)
                aux = aux.left
                i+=1

arbol = NodoArbol("R", NodoArbol("C"), NodoArbol("H"))
#print(arbol.left.data)
#print(arbol.right.data)
#print(arbol.data)

arbol2 = NodoArbol(4, NodoArbol(3, NodoArbol(2, NodoArbol(2, None, None)), None), NodoArbol(5,None,None))

arbol.recorrido_prefijo()
print("--------------------")
arbol2.recorrido_prefijo()
print("--------------------")
arbol2.recorrido_sufijo()
