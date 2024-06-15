class Merge:
    def sort(self, array, sort_attribute, ascending=True):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.sort(left_half, sort_attribute, ascending)
            self.sort(right_half, sort_attribute, ascending)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if (
                    getattr(left_half[i], sort_attribute)
                    < getattr(right_half[j], sort_attribute)
                    if ascending
                    else getattr(left_half[i], sort_attribute)
                    > getattr(right_half[j], sort_attribute)
                ):
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

        return array

    def sort_numbers(self, array, ascending=True):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.sort_numbers(left_half, ascending)
            self.sort_numbers(right_half, ascending)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if (
                    (left_half[i] < right_half[j])
                    if ascending
                    else (left_half[i] > right_half[j])
                ):
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

        return array
