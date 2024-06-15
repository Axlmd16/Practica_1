class Burbuja:

    def sort_burbuja_dsc(self, array):
        for i in range(len(array)):
            for j in range(len(array) - 1):
                if array[j] > array[j + 1]:
                    aux = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = aux
        return array

    def sort_burbuja_asc(self, array):
        for i in range(len(array)):
            for j in range(len(array) - 1):
                if array[j] < array[j + 1]:
                    aux = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = aux
        return array

    # Con atributos
    def sort_burbuja_attr_asc(self, array, attribute):
        for i in range(len(array)):
            for j in range(len(array) - 1):
                if getattr(array[j], attribute) < getattr(array[j + 1], attribute):
                    aux = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = aux
        return array

    def sort_burbuja_attr_dsc(self, array, attribute):
        for i in range(len(array)):
            for j in range(len(array) - 1):
                if getattr(array[j], attribute) > getattr(array[j + 1], attribute):
                    aux = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = aux
        return array
