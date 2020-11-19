class Nodo:
    def __init__(self, value, siguiente = None):
        self.data = value #falta encapsular
        self.siguiente = siguiente

class Linked_List: # constructor
    def __init__ (self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def append (self, value):
        nuevo = Nodo(value)
        if self.__head == None: #es equivalente a seld.is_empty
            self.__head = nuevo
        else:
            curr_node = self.__head #curr_node toma valor de head
            while curr_node.siguiente != None: #se revisa si el siguiente nodo esta vacio
                curr_node = curr_node.siguiente #si el siguiente nodo no esta vacio, curr_node toma el valor de ese nodo
            curr_node.siguiente = nuevo #al valor siguiente del que tiene curr_node se le da el valor de nuevo, solo si esa posicion esta vacia

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f" {curr_node.data}-->", end="")
            curr_node = curr_node.siguiente
        print("")

    def tail(self):
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        return curr_node

    def remove(self, value):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.siguiente
        else:
            anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
            else:
                print("El dato no existe en a lista")

    def preppend (self,value):
        nuevo = Nodo(value,self.__head)
        self.__head = nuevo

    def get(self, posicion= None ):
        contador=0
        dato = None
        if posicion == None:
            dato = self.tail().data
        else:
            pass
        return dato
