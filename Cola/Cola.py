class Queue:
    def __init__( self ):
        self.__data = list() # o tambien puedes declararlo asi list []

    def is_empty( self ):
        return len(self.__data) == 0

    def length ( self ):
        return len(self.__data)

    def enqueue (self, element):
        self.__data.append(element)

    def dequeue (self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def to_string(self):
        cadena =""
        for element in self.__data:
            cadena = cadena + "|" + str(element)
        cadena = cadena + "|"
        return cadena

#Tarea PriorityQueue

class BoundedPriorityQueue:
    def __init__(self, niveles):
        self.__data = [Queue() for x in range(niveles)]
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def length(self):
        return self.__size

    def enqueue(self, prioridad, element):
        if prioridad < len(self.__data) and prioridad >= 0:
            self.__data[prioridad].enqueue(element)
            self.__size += 1

    def dequeue(self):
        if not self.is_empty():
            for nivel in self.__data:
                if not nivel.is_empty():
                    self.__size -= 1
                    return nivel.dequeue()
        else:
            print("Todos han abandonado el barco")

    def to_string(self):
        for nivel in range(len(self.__data)):
            print(f"Nivel {nivel} --> {self.__data[nivel].to_string()}")
