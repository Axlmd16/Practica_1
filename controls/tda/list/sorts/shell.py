class Shell:
    def sort(self, array, sort_attribute, ascending=True):
        n = len(array)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                while j >= gap and (
                    (
                        getattr(array[j - gap], sort_attribute)
                        > getattr(temp, sort_attribute)
                    )
                    if ascending
                    else (
                        getattr(array[j - gap], sort_attribute)
                        < getattr(temp, sort_attribute)
                    )
                ):
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2

        return array

    def sort_numbers(self, array, ascending=True):
        n = len(array)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                while j >= gap and (
                    (array[j - gap] > temp) if ascending else (array[j - gap] < temp)
                ):
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2

        return array
