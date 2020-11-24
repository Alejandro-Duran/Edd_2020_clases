class NodoDoble:
    def __init__(self, value, siguiente=None, anterior=None):
        self.data = value
        self.siguiente = siguiente
        self.anterior = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble(None)
        self.__tail = NodoDoble(None)
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def append (self, value):
        if self.is_empty():
            nuevo = NodoDoble(value)
            self.__head = nuevo
            self.__tail = nuevo
        else:
            nuevo = NodoDoble(value, None, self.__tail)
            self.__tail.siguiente = nuevo
            self.__tail = nuevo
        self.__size += 1

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f" <-- {curr_node.data} -->",end="")
            curr_node = curr_node.siguiente
        print("")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f" <-- {curr_node.data} -->",end="")
            curr_node = curr_node.anterior
        print("")

    def remove_from_head(self,value):
        curr_node =self.__head
        while curr_node.data != value and curr_node != None:
            curr_node = curr_node.siguiente
        if curr_node.data == value:
            curr_node.anterior.siguiente = curr_node.siguiente
            curr_node.siguiente.anterior = curr_node.anterior
