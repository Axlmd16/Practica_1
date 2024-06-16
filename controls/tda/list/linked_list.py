import datetime
from numbers import Number
from controls.tda.array.tdaArray import TDAArray
from controls.tda.list.node import Node
from controls.tda.list.sorts.burbuja import Burbuja
from controls.tda.list.sorts.merge import Merge
from controls.tda.list.sorts.quick import Quick
from controls.tda.list.sorts.shell import Shell


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

    def add_pos(self, data, pos):
        if pos == 0:
            self.add_first(data)
        elif pos == self._length - 1:
            self.add_last(data)
        else:
            search_preview = self.get_node(pos - 1)
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
                out += "=> " + str(node._data)
                node = node._next
        return out

    @property
    def print(self):
        node = self.__head
        data = ""
        while node is not None:
            data += str(node._data) + " -> "
            node = node._next
        print(data)

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
        node = self.__head
        while node is not None:
            array.append(node._data)
            node = node._next
        return array

    def to_list(self, array):
        self.clear()
        for i in range(0, len(array)):
            self.add_last(array[i])
        return self

    def deleteFirst(self):
        if self.isEmpty:
            raise IndexError("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element

    def deleteLast(self):
        if self.isEmpty:
            raise IndexError("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)

            # self.__head = aux
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element

    def delete(self, pos=0):

        if self.isEmpty:
            raise IndexError("List empty")
        elif pos < 0 or pos >= self.__length:
            raise IndexError("Error, It is out of the limit of the list")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == (self.__length - 1):
            return self.deleteLast()
        else:
            preview = self.getNode(pos - 1)
            actually = self.getNode(pos)
            element = preview._data
            next = actually._next
            actually = None
            preview._next = next
            self._length = self._length - 1
            return element

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Error, It is out of the limit of the list")
        else:
            return self.get_node(index)._value

    def sort_numbers(self, type=0, algorithm="quick_sort"):
        if self.is_empty:
            raise Exception("List is empty")
        else:
            array = self.to_array
            if isinstance(array[0], Number):
                order = type == 0
                if algorithm == "quick_sort":
                    sorted_array = Quick().sort_numbers(array, order)
                elif algorithm == "merge_sort":
                    sorted_array = Merge().sort_numbers(array, order)
                else:
                    sorted_array = Shell().sort_numbers(array, order)
                self.to_list(sorted_array)
        return self

    def sort_models(self, attribute, type=0, algorithm="quick_sort"):
        if self.is_empty:
            raise Exception("List is empty")
        else:
            array = self.to_array
            if isinstance(array[0], object):
                order = type == 0
                sort_attribute = "_" + attribute

                if algorithm == "quick_sort":
                    sorted_array = Quick().sort(array, sort_attribute, order)
                elif algorithm == "merge_sort":
                    sorted_array = Merge().sort(array, sort_attribute, order)
                else:
                    sorted_array = Shell().sort(array, sort_attribute, order)

                self.to_list(sorted_array)
        return self

    # def sort_models(self, attribute, type=1):
    #     if self.is_empty:
    #         raise Exception("List is empty")
    #     else:
    #         array = self.to_array
    #         if isinstance(array[0], object):
    #             array.sort(key=lambda x: getattr(x, "_" + attribute), reverse=type != 1)
    #         self.to_list(array)
    #     return self

    # Prueba de sort_models con fechas
    # def sort_models(self, attribute, type=1):
    #     if self.is_empty:
    #         raise Exception("List is empty")
    #     else:
    #         array = self.to_array
    #         if isinstance(array[0], object):

    #             def get_key(x):
    #                 value = getattr(x, "_" + attribute)
    #                 if isinstance(value, (int, float, str, bool)):
    #                     return value
    #                 elif isinstance(value, datetime.date):
    #                     return value.toordinal()
    #                 else:
    #                     raise TypeError(f"Unsupported attribute type: {type(value)}")

    #             array.sort(key=get_key, reverse=type != 1)
    #         self.to_list(array)
    #     return self

    def search_numbers_lineal(self, value):
        lista = Linked_List()
        if self.is_empty:
            raise Exception("List is empty")
        else:
            array = self.to_array
            for i in range(0, len(array)):
                if array[i] == value:
                    lista.add(array[i])
        return lista
    

    # def search_models(self, attribute, value):
    #     lista = Linked_List()
    #     if self.is_empty:
    #         raise Exception("List is empty")
    #     else:
    #         array = self.to_array
    #         if isinstance(array[0], object):
    #             array = [x for x in array if getattr(x, "_" + attribute) == value]
    #         lista.to_list(array)
    #     return lista

    def search_models_binary(self, attribute, value):
        if self.is_empty:
            raise Exception("List is empty")
        else:
            self.sort_models(attribute)
            array = self.to_array
            if isinstance(array[0], object):
                low = 0
                high = len(array) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if getattr(array[mid], "_" + attribute) == value:
                        return array[mid]
                    elif getattr(array[mid], "_" + attribute) < value:
                        low = mid + 1
                    else:
                        high = mid - 1
        return None

    def search_models_lb(self, attribute, value):
        if self.is_empty:
            raise Exception("List is empty")
        else:
            index = self.__search_binary_index(attribute, value)
            if index is None:
                return []

            lista = Linked_List()
            array = self.to_array
            results = []

            left = index
            while left >= 0 and getattr(array[left], "_" + attribute) == value:
                results.insert(0, array[left])
                left -= 1

            right = index + 1
            while (
                right < len(array) and getattr(array[right], "_" + attribute) == value
            ):
                results.append(array[right])
                right += 1

            lista.to_list(results)
        return lista

    def __search_binary_index(self, attribute, value):
        if self.is_empty:
            raise Exception("List is empty")
        else:
            self.sort_models(attribute)
            array = self.to_array
            if isinstance(array[0], object):
                low = 0
                high = len(array) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if getattr(array[mid], "_" + attribute) == value:
                        return mid
                    elif getattr(array[mid], "_" + attribute) < value:
                        low = mid + 1
                    else:
                        high = mid - 1
        return None

    # def search_time_minors(self, value):
    #     lista = Linked_List()
    #     if self.is_empty:
    #         raise Exception("List is empty")
    #     else:
    #         array = self.to_array
    #         if isinstance(array[0], object):
    #             array = [x for x in array if getattr(x, "_" + attribute) < value]
    #         lista.to_list(array)
    #     return lista
