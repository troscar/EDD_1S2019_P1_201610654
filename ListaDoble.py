class NodoDoble():
    def __init__ (self, valor):
        self.next = None
        self.anterior = None
        self.valor = valor

class ListaDoble():
    def __init__(self):
        self.primer = None
        self.ultimo = None
        self.size = 0

    def estaVacia(self):
        return self.size == 0
    
    def Insertar_F (self,valor):
        nuevo = NodoDoble(valor)
        if(self.estaVacia()):
            self.primer = nuevo
        else:
            temporal = self.primer
            while(temporal.siguiente != None):
                