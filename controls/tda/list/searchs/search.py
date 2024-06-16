from controls.tda.list.linked_list import Linked_List


class Search:
    def search_models_binary(self, attribute, value, lista):
        if lista.is_empty:
            raise Exception("List is empty")
        else:
            lista.sort_models(attribute)
            array = lista.to_array
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

    def search_models_lb(self, attribute, value, lista):
        if lista.is_empty:
            raise Exception("List is empty")
        else:
            index = self.__search_binary_index(attribute, value, lista)
            if index is None:
                return []

            lista_search = Linked_List()
            array = lista.to_array
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

            lista_search.to_list(results)
        return lista_search

    def __search_binary_index(self, attribute, value, lista):
        if lista.is_empty:
            raise Exception("List is empty")
        else:
            lista.sort_models(attribute)
            array = lista.to_array
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
        return low

    def search_tiempo_menor(self, attribute, value, lista):
        if lista.is_empty:
            raise Exception("List is empty")
        else:
            index = self.__search_binary_index(attribute, value, lista)
            if index is None:
                return Linked_List()

            lista_search = Linked_List()
            array = lista.to_array

            left = index - 1
            while left >= 0 and getattr(array[left], "_" + attribute) < value:
                lista_search.add(array[left])
                left -= 1

        return lista_search

    def search_tiempo_mayor(self, attribute, value, lista):
        if lista.is_empty:
            raise Exception("List is empty")
        else:
            index = self.__search_binary_index(attribute, value, lista)
            if index is None:
                return Linked_List()

            lista_search = Linked_List()
            array = lista.to_array

            right = index + 1
            while right < len(array) and getattr(array[right], "_" + attribute) > value:
                lista_search.add(array[right])
                right += 1

        return lista_search

    def search_numbers_lineal(self, value, lista):
        if lista.is_empty:
            raise Exception("List is empty")
        else:
            lista_search = Linked_List()
            array = lista.to_array
            for number in array:
                if number == value:
                    lista_search.add(number)
        return lista_search

    def search_numbers_binary_lineal(self, value, lista):
        if lista.is_empty:
            raise Exception("List is empty")
        else:
            index = self.__search_binary_index(value, lista)
            if index is None:
                return Linked_List()

            lista_search = Linked_List()
            array = lista.to_array

            left = index
            while left >= 0 and array[left] == value:
                lista_search.add(array[left])
                left -= 1

            right = index + 1
            while right < len(array) and array[right] == value:
                lista_search.add(array[right])
                right += 1

        return lista_search
