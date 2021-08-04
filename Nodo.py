from ListaRecursiva import *

class Nodo():
    def __init__(self,clave):
        self.__clave = clave
        self.__estado = ListaRecursiva()

    #Propiedades
    def get_clave(self):
        return self.__clave
    def get_estado(self):
        return self.__estado

    def set_clave(self, clave):
        self.__clave == clave
    def set_estado(self, estado):
        self.__estado = estado

    #Metodos
    def MostrarNodo(self):
        print(self.__clave + " --> ", end="")    #Mostrar clave (caracter)
        self.__estado.MostrarLista()    #Mostrar los estados que conduce 

