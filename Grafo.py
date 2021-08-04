
#TDA Grafo implementado mediante Listas de Adyacencia y no Matriz de Adyacencia
from ListaRecursiva import *
from Nodo import *

class Grafo():
    #Constructor
    def __init__(self):
        self.__vertice = None
        self.__lista = None
        self.__subGrafo = None

    def Crear(self, vertice, lista, subGrafo):
        self.__vertice = vertice
        self.__lista = lista
        self.__subGrafo = subGrafo
    
    #Modificadores
    def get_vertice(self):
        return self.__vertice
    def get_lista(self):
        return self.__lista
    def get_subGrafo(self):
        return self.__subGrafo

    def set_vertice(self, vertice):
        self.__vertice = vertice
    def set_lista(self, lista):
        self.__lista = lista
    def set_subGrafo(self, subGrafo):
        self.__subGrafo = subGrafo

    #Metodos
    def EstaVacio(self):
        return self.__vertice == None

    def ExisteVertice(self, V):
        if(self.EstaVacio()):
            return False
        elif(self.__vertice == V):
            return True
        else:
            self.__subGrafo.ExisteVertice(V)

    def AgregarVert(self, V):
        if(self.EstaVacio()):
            self.__vertice = V
            self.__lista = ListaRecursiva()
            self.__subGrafo = Grafo()
        else:
            self.__subGrafo.AgregarVert(V)

    #Verifica que no se agrege un vertice repetido
    def AgregarVertice(self,V): 
        if(not self.ExisteVertice(V)):
            self.AgregarVert(V)

    def AgregarArco(self, vo , vf , clave):
        if(not self.EstaVacio()):
            if(self.__vertice == vo ):
                if(self.__lista.Exite(clave)): #agregar otro estado(no deteminista)
                    self.__lista.ObtenerNodo(clave).get_estado().Agregar(vf)
                else:
                    #Agregamos el alfabeto, creo agregamos explicitamente
                    self.__lista.Agregar(Nodo(clave))
                    #Agregamos el vf
                    self.__lista.ObtenerNodo(clave).get_estado().Agregar(vf)
            else:
                self.__subGrafo.AgregarArco(vo,vf,clave)
        else:
            print("no se agrego")

    def MostrarGrafo(self):
        if(not self.EstaVacio()):
            print("Vertice: " + str(self.__vertice));
            self.__lista.VerNodos();
            self.__subGrafo.MostrarGrafo();  
        else:
            print();



rafo = Grafo()
rafo.AgregarVertice(1)
rafo.AgregarVertice(2)
rafo.AgregarVertice(3)
rafo.AgregarVertice(4)
rafo.AgregarVertice(5)

rafo.AgregarArco(1,2,"a")
rafo.AgregarArco(1,3,"b")
rafo.AgregarArco(2,2,"a")
rafo.AgregarArco(2,4,"b")
rafo.AgregarArco(3,5,"b")
rafo.AgregarArco(4,3,"a")
rafo.AgregarArco(5,4,"a")

rafo.MostrarGrafo()