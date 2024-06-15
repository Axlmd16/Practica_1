class Insercion:

    def sort_insercion_dsc(self, array):
        for i in range(len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and t > array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = t

        return array

    def sort_insercion_asc(self, array):
        for i in range(len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and t < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = t

        return array

    def sort_insertion_attr_asc(self, array, attribute):
        for i in range(len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and getattr(t, attribute) < getattr(array[j], attribute):
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = t

        return array

    def sort_insertion_attr_dsc(self, array, attribute):
        for i in range(len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and getattr(t, attribute) > getattr(array[j], attribute):
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = t

        return array
