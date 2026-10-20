#Datos MIguel

class Nodo:
    #def __init__(self, data, next=None, previus=None):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next #puntero al siguiente nodo
        #self.previus = previus #puntero al nodo anterior

class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None
    def agrega_inicio(self,dato):
        nuevo_nodo = Nodo(dato)
        #el nuevo nodo apunta a lo que actualmente tenga cabecera
        nuevo_nodo.next = self.head
        #la cabecera pasa a ser el nuevo nodo
        self.head = nuevo_nodo

    def esta_vacia(self):
        return self.head == None

    def vaciar(self):
        self.head = None
    def insertar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)
        #if not self.head:
        if self.esta_vacia():
            self.head = nuevo_nodo
            return
        actual = self.head
        while actual.next != None:
            actual = actual.next
        #es actualiza el puntero del ultimo nodo
        actual.next = nuevo_nodo
    def imprimir(self):
        actual = self.head
        elementos = []
        #recorre la lista desde la cabecera hasta que encuentre un nodo vacio
        while actual != None:
            #print("->",actual.data)
            elementos.append(str(actual.data))
            actual = actual.next
        print(" -> ".join(elementos) + " -> None")

    def eliminar(self, valor):
        #primero verifico que la lista no este vacia
        if self.esta_vacia():
            return False
        actual = self.head
        #verifco que el valor a eliminar sea la cabecera
        if actual.data == valor:
            self.head = actual.next
            return True
        #recorro la lista para encontrar el valor a eliminar
        while actual.next != None and actual.next.data != valor:
            actual = actual.next
        
        #si actual.next es None, significa que no se encontro el valor
        if actual.next == None:
            return False
        #actual.next es el nodo a eliminar
        #print(actual.data)
        if actual.next:
                actual.next = actual.next.next
        return True
    


#Crear una nueva lista enlazada simple
if(__name__ == "__main__"):
    ls = ListaEnlazadaSimple()
    ls.insertar_al_final(5)
    ls.insertar_al_final(3)
    ls.insertar_al_final(2)
    ls.insertar_al_final(8)
    print("Lista enlazada simple: ")
    #print(ls.head.data)
    #print(ls.head.next.data)
    #ls.vaciar()
    #print(ls.head.next.next.data)
    #print(ls.head.next.next.next.data)
    ls.imprimir()
    ls.eliminar(3)
    ls.imprimir()
#class ListaEnlazadaDoble:
#    def __init__(self):
#        self.head = None
    