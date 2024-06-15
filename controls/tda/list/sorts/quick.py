class Quick:
    def sort(self, array, attr, ascendente=True):
        size = len(array)
        if size > 1:
            self.__quick_sort(array, 0, size - 1, attr, ascendente)
        return array

    def __quick_sort(self, array, low, high, attr, ascendente):
        if low < high:
            pi = self.__partition(array, low, high, attr, ascendente)
            self.__quick_sort(array, low, pi - 1, attr, ascendente)
            self.__quick_sort(array, pi + 1, high, attr, ascendente)

    def __partition(self, array, low, high, attr, ascendente):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if (
                getattr(array[j], attr) < getattr(pivot, attr)
                if ascendente
                else getattr(array[j], attr) > getattr(pivot, attr)
            ):
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def sort_numbers(self, array, ascending=True):
        size = len(array)
        if size > 1:
            self.__quick_sort_numbers(array, 0, size - 1, ascending)
        return array

    def __quick_sort_numbers(self, array, low, high, ascending):
        if low < high:
            pi = self.__partition_numbers(array, low, high, ascending)
            self.__quick_sort_numbers(array, low, pi - 1, ascending)
            self.__quick_sort_numbers(array, pi + 1, high, ascending)

    def __partition_numbers(self, array, low, high, ascending):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if (array[j] < pivot) if ascending else (array[j] > pivot):
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
