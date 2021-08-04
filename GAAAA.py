class ListaRecursiva():
    
    #Contructor
    def __init__(self):
        self.__elemento = None
        self.__subLista = None

    #Propiedades 
    def get_elemento(self):
        return self.__elemento
    def get_subLista(self):
        return self.__subLista

    def set_elemento(self, elemento):
        self.__elemento = elemento
    def set_sublista(self, subLista):
        self.__subLista = subLista

    #Propiedades
    def EstaVacio(self):
        return self.__elemento == None and self.__subLista == None

    def Agregar(self, elemento):
        if(self.EstaVacio()):
            self.__elemento = elemento
            self.__subLista = ListaRecursiva()
        else:
            self.__subLista.Agregar(elemento)

    def Exite(self, elemento):          #Optimizar el return
        if(self.EstaVacio()):
            return False
        elif(self.__elemento == elemento):
            return True
        else:
            self.__subLista.Existe(elemento)

    def ObtenerIesimo(self, i):
        if(i<=1):
            return self.__elemento
        else:
            self.__subLista.ObtenerIesimo(i-1)

    def ObtenerNodo(self, elemento):
        if(self.EstaVacio()):
            print("Noneee")
            return None
        elif(self.__elemento == elemento):
            print("en lista encontro a")
            return self.__elemento
        else:
            self.__subLista.ObtenerNodo(elemento)

    def MostrarLista(self):
        if (not self.EstaVacio()):
            print(str(self.__elemento) + " -> " , end="")
            self.__subLista.MostrarLista()
        else:
            print("fin")

    def VerNodos(self):
        if(not self.EstaVacio()):
            self.__elemento.MostrarNodo() #Mostrar caracteres de estado
            self.__subLista.VerNodos()     #Mostrar siguente estado
        else:
            print("")
#_______________________________________________________________________
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
                                        #       la clave(no determinista)

#__________________________________________________________________________


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
                    #self.__lista.VerNodos()
                    #Agregamos el vf
                    #print(self.__lista.ObtenerNodo(clave))
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
#rafo.AgregarArco(1,3,"b")
#rafo.AgregarArco(2,2,"a")
#rafo.AgregarArco(2,4,"b")
#rafo.AgregarArco(3,5,"b")
#rafo.AgregarArco(4,3,"a")
#rafo.AgregarArco(5,4,"a")

#rafo.MostrarGrafo()
