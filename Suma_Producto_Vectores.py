# Creamos la clase node
class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list:

    """
    Se asignan los atributos, los cuales son
    las operaciones que se desean obtener, en la multiplicacion
    toma un valor de 1 ya que si le asignamos un valor de 0, la
    multilpicacion dara como resultado 0.
    """
    __sumatoria = 0
    __multiplicacion = 1

    def getSumatoria(self):
        return self.__sumatoria

    def getMultiplicacion(self):
        return self.__multiplicacion

    def __init__(self):
        self.head = None

    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)

    # Método para eliminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, node.next)  #Se muestra el dato y el nodo siguiente
            node = node.next

    """
    Se agrega el metodo para obtener las sumas
    de los nodos, en el que se hace us de un ciclo while, en el que 
    realiza un recorrido hasta que el nodo sea nulo finaliza.
    """
    def obtenerSumatoria(self):
        node = self.head

        while node != None:
            self.__sumatoria += node.data
            node = node.next

        return self.__sumatoria

    """
    Se asigna el metodo para realizar la multiplicacion de los 
    nodos.
    """
    def obtenerMultiplicacion(self):
        node = self.head

        while node != None:
            self.__multiplicacion *= node.data
            node = node.next

        return self.__multiplicacion

s = linked_list()  # Instancia de la clase
x = linked_list()

"""
Datos que se le agregan a lo nodos en el Vector 1:
"""
# Se agregan elementos al frente del nodo
s.add_at_front(5)
s.add_at_front(9)

# Se agregan elementos al final del nodo
s.add_at_end(4)
s.add_at_end(12)
s.add_at_end(8)

"""
Datos que se le agregan a lo nodos en el Vector 2:
"""
# Se agregan elementos al frente del nodo
x.add_at_front(7)
x.add_at_front(12)

# Se agregan elementos al final del nodo
x.add_at_end(15)
x.add_at_end(6)
x.add_at_end(2)

print("Vector 1:")
s.print_list()  # Se imprime la lista de nodos del vector 1
print("----------------------------------------------------------")
print("Vector 2:")
x.print_list()   # Se imprime la lista de nodos del vector 2

print()
print("**********************************************************")
print("La suma de los vectores es: ", int(s.obtenerSumatoria() + x.obtenerSumatoria()))  # Se muestra la suma de los dos vectores
print("El producto escalar es: ", int(s.obtenerMultiplicacion() + x.obtenerMultiplicacion()))  # Se muestra la multiplicacion de los dos vectores