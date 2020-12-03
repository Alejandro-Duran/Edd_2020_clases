from Array2D import array2d
from Stack import Stack
class LaberintoADT:
    '''
    0 pasillo, 1 pared, Ssalida y E entrada
    pasillo es una tupla((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
    entrada en una tupla (5,2)
    salidaen una tupla (2,5)
    '''
    def __init__(self, rens, cols, pasillos, entrada, salida):
        self.__laberinto = array2d(rens, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1],'0')
        self.set_entrada(entrada[0],entrada[1])
        self.set_salida(salida[0],salida[1])
        self.__camino = Stack()
        self.__previa = None

    def to_string(self):
        self.__laberinto.to_string()

    '''
    Establece la entrada "E" en la matriz, verificar limites perifericos
    '''

    def set_entrada (self, ren, col):
        # Terminar la validación de entrada
        self.__laberinto.set_item(ren,col,'E')

    '''
    Establecer salida "S", dentro de lo limites perifericos de la matriz
    '''
    def set_salida(self, ren, col):
        #Terminar las validaciones
        self.__laberinto.set_item(ren,col,'S')

    def es_salida(self, ren, col):
        return self.__laberinto.get_item(ren,col)=="S"

    def buscar_entrada(self):
        encontrado = False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range (self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(tope[0],tope[1])=="E":
                    self.__camono.push(tuple(renglon,columna))
                    encontrado = True
        return encontrado


    def set_previa(self. pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def resolver_laberinto(self):
        #APLICAR REGLAS
