
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
            print('1')
            return False
        elif(self.__elemento.get_clave() == elemento):  #Mutar a nodo 
            return True
        else:
            print('2')
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
        elif(self.__elemento.get_clave() == elemento):
            #print("en lista encontro a")
            return self.__elemento
        else:
            print("Aqui todavia se;or")
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
            print("finNodos/el=Null , subL=Null")

#z=ListaRecursiva()
#z= Nodo("a")
#z.Agregar()
#print(z.EstaVacio())