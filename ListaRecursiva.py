
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
        if(self.EstaVacio()):               #Asi se agrega el primer nodo
            self.__elemento = elemento
            self.__subLista = ListaRecursiva() #lopez
        else:
            self.__subLista.Agregar(elemento)

    def Exite(self, elemento):          #Optimizar el return
        if(self.EstaVacio()):
            return False
        elif(self.__elemento.get_clave() == elemento):
            return True
        else:                           #Ver el siguiente nodo
            #print('2')                  #Falta inicializar
            z = self.__subLista
            z.Exite(elemento)
            #self.__subLista.Existe(elemento)

    def ObtenerIesimo(self, i):
        if(i<=1):
            return self.__elemento
        else:
            self.__subLista.ObtenerIesimo(i-1)

    def ObtenerNodo(self, elemento):
        if(self.EstaVacio()):
            print("Noneee")
            return None
        elif(self.__elemento.get_clave() == elemento):
            return self.__elemento #sino con get
        else:
            return self.__subLista.ObtenerNodo(elemento)

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
