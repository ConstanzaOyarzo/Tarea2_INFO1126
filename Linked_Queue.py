# Cola doblemente enlazada
# Cola de vuelos programados

from Exceptions import OwnEmpty

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    # Nodo
    class Node:
        """Lightweight, non-public class for storing a singly linked node."""
        __slots__ = 'element', 'next'

        def __init__(self, element, next_node):
            self.element = element
            self.next = next_node

    # Cola Lista vuelos
    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self.size = 0  # number of elements in the queue

    # Devuelve el numero de elementos en la cola
    """ longitud """
    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    # Verifica si la cola esta vacia
    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0

    # Devuelve el primer elemento (head) sin eliminarlo
    # Consulta cual es el siguiente vuelo sin eliminarlo (?)
    """ obtener el primero """
    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise OwnEmpty if the queue is empty.
        """
        if self.is_empty():
            raise OwnEmpty("No hay vuelos registrados en este momento")
        return self.head.element  # front aligned with head of list
    
    """ obtener el ultimo """
    def last(self):
        if self.is_empty():
            raise OwnEmpty("No hay vuelos registrados en este momento")
        return self.tail.element 

    # Desencolar
    # Elimina Y devuelve el primer elemento (head)
    # Si la cola queda vacia, actualiza el ultimo elemento (tail) a None
    # Saca el siguiente vuelo (?)
    def dequeue(self):
        """Remove and return the first element of the queue (FIFO).

        Raise OwnEmpty if the queue is empty.
        """
        if self.is_empty():
            raise OwnEmpty("No hay vuelos registrados en este momento")
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():  # special case: queue is now empty
            self.tail = None  # the removed node was also the tail
        return answer
    
    """ Insertar al frente """
    """ Añade un vuelo al inicio de la lista (para emergencias) """
    def insertar_al_frente(self, vuelo):
        newest = self.Node(vuelo, self.head)  # apunta al nodo actual que era el primero
        self.head = newest               # ahora el nuevo nodo es el primero
        if self.is_empty():
            self.tail = newest           # si estaba vacía, head y tail son iguales
        self.size += 1

    # Encolar
    # Agrega un elemento al final de la cola (?)
    # Inserta nuevos vuelos
    """ Insertar al final """
    """ añade un vuelo al final de la lista (vuelos regulares) """
    def enqueue(self, vuelo):
        """Add an element to the back of the queue."""
        newest = self.Node(vuelo, None)  # node will become the new tail
        if self.is_empty():
            self.head = newest  # special case: queue was empty
        else:
            self.tail.next = newest
        self.tail = newest  # update reference to the new tail
        self.size += 1

    """ Insertar en posicion """
    def insertar_en_posicion(self, vuelo, posicion):
        # Valida que la posicion asignada no este fuera de rango
        if posicion < 0 or posicion > self.size:
            raise IndexError("Posición de vuelo fuera de rango")

        nuevo_nodo = self.Node(vuelo)

        # En caso que se quiera insertar en la primera posicion o en posicion cero
        # En ese caso se actualiza head
        if posicion == 0:
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
            if self.size == 0:
                self.tail = nuevo_nodo

        # Caso general para insertar en cualquier posicion que no sea la primera o la ultima
        else:
            actual = self.head
            for _ in range(posicion - 1):  # Avanzar hasta el nodo anterior a la posición
                actual = actual.next
            nuevo_nodo.next = actual.next
            actual.next = nuevo_nodo

            # En el caso de que se inserte al final
            # Entonces se actualiza tail
            if nuevo_nodo.next is None:
                self.tail = nuevo_nodo

        self.size += 1

    """ Extraer de posicion """
    def extraer_de_posicion(self, posicion):
        if self.is_empty():
            raise Exception("No hay vuelos registrados en este moment")
        if posicion < 0 or posicion >= self.size:
            raise IndexError("Posición de vuelo fuera de rango")

        # En caso que sea el primer elemento el que se extrae
        if posicion == 0:
            eliminado = self.head
            self.head = self.head.next
            if self.head is None:  # Si la cola queda vacía, actualizamos tail
                self.tail = None

        # Extrae cualquier posicion que no sea el inicio o final
        else:
            actual = self.head
            for _ in range(posicion - 1):
                actual = actual.next
            eliminado = actual.next
            actual.next = eliminado.next

            # Si es el el último nodo el que se elimina, se actualiza tail
            if eliminado.next is None:
                self.tail = actual

        self.size -= 1
        return eliminado.element