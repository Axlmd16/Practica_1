from controls.tda.list.node import Node


class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def is_empty(self):
        return self.__head is None or self.__length == 0

    def add_first(self, data):
        if self.is_empty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length += 1
        else:
            head_old = self.__head
            node = Node(data, head_old)
            self.__head = node
            self.__length += 1

    def add_last(self, data):
        if self.is_empty:
            self.add_first(data)
        else:
            aux = Node(data)
            self.__last._next = aux
            self.__last = aux
            self.__length += 1

    def add(self, data, post):
        if post == 0:
            self.add_first(data)
        elif post == self._length - 1:
            self.add_last(data)
        else:
            search_preview = self.get_node(post - 1)
            aux = Node(data, search_preview._next)
            search_preview._next = aux
            self._length += 1

    def add(self, data):
        if self.is_empty:
            self.add_first(data)
        else:
            self.add_last(data)

    def get_node(self, post):
        if self.is_empty:
            raise Exception("Error, Lista vacia")
        elif post < 0 or post >= self._length:
            raise IndexError("Error, Esta fuera del limite de la lista")
        elif post == 0:
            return self.__head
        elif post == (self._length - 1):
            return self.__last
        else:
            search = self.__head
            cont = 0
            while cont < post:
                cont += 1
                search = search._next
            return search

    def get_first(self):
        if self.is_empty:
            raise Exception("Error, List is empty")
        else:
            return self.__head._data

    def get_last(self):
        if self.is_empty:
            raise Exception("Error, List is empty")
        else:
            return self.__last._data

    def get(self, index):
        if self.is_empty:
            raise Exception("Error, Lista vacia")
        elif index < 0 or index >= self._length:
            raise IndexError("Error, It is out of the limit of the list")
        elif index == 0:
            return self.get_first()
        elif index == (self._length - 1):
            return self.get_last()
        else:
            search = self.get_node(index)
            return search._data

    def __str__(self) -> str:
        out = ""
        if self.is_empty:
            out = "List is empty"
        else:
            node = self.__head
            while node is not None:
                out += "=> " + str(node._data) + "\n"
                node = node._next
        return out

    def update(self, pos, data):
        if self.is_empty:
            raise Exception("List is empty")
        elif pos < 0 or pos >= self._length:
            raise IndexError("Error, It is out of the limit of the list")
        elif pos == 0:
            self.__head._data = data
        elif pos == (self._length):
            self.__last._data = data
        else:
            nodo = self.get_node(pos)
            nodo._data = data

    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        else:
            item = self.__current._data
            self.__current = self.__current._next
            return item

    @property
    def to_array(self):
        array = []
        if self._length > 0:
            aux = self.__head
            for _ in range(self._length):
                array.append(aux._data)
                aux = aux._next
        return array

    @property
    def to_list(self, m):
        self.clear()
        for e in m:
            self.add(e, self._length)
        return self

    def delete_first(self):
        if self.is_empty:
            raise Exception("List is empty")
        else:
            self.__head = self.__head._next
            self._length -= 1

    def delete_last(self):
        if self.is_empty:
            raise Exception("List is empty")
        else:
            node = self.get_node(self._length - 2)
            node._next = None
            self.__last = node
            self._length -= 1

    def delete(self, index):
        if self.is_empty:
            raise Exception("List is empty")
        elif index < 0 or index >= self._length:
            raise IndexError("Error, It is out of the limit of the list")
        else:
            node = self.get_node(index - 1)
            node._next = node._next._next
            self._length -= 1


def __getitem__(self, index):
    if index < 0 or index >= self._length:
        raise IndexError("Error, It is out of the limit of the list")
    else:
        return self.get_node(index)._value
