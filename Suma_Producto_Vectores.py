# Creamos la clase node
class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list:

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
            print(node.data, node.next)
            node = node.next

    def obtenerSumatoria(self):
        node = self.head

        while node != None:
            self.__sumatoria += node.data
            node = node.next

        return self.__sumatoria

    def obtenerMultiplicacion(self):
        node = self.head

        while node != None:
            self.__multiplicacion *= node.data
            node = node.next

        return self.__multiplicacion

s = linked_list()  # Instancia de la clase
s.add_at_front(5)  # Agregamos un elemento al frente del nodo
s.add_at_end(8)  # Agregamos un elemento al final del nodo
s.add_at_front(9)  # Agregamos otro elemento al frente del nodo
s.add_at_end(4)
s.add_at_end(12)

x = linked_list()
x.add_at_front(14)  # Agregamos un elemento al frente del nodo
x.add_at_end(11)  # Agregamos un elemento al final del nodo
x.add_at_front(7)  # Agregamos otro elemento al frente del nodo
x.add_at_end(3)
x.add_at_end(8)

print("Vector 1:")
s.print_list()  # Imprimimos la lista de nodos
print("----------------------------------------------------------")
print("Vector 2:")
x.print_list()

print()
print("**********************************************************")
print("La suma de los vectores es: ", int(s.obtenerSumatoria() + x.obtenerSumatoria()))
print("El producto escalar es: ", int(s.obtenerMultiplicacion() + x.obtenerMultiplicacion()))