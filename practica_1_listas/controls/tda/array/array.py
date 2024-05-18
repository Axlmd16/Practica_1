class Array:
    # Constructor
    def __init__(self, size, value=None):
        self.__size = size
        self.__position = 0
        if size > 0:
            self.__array = []
            for i in range(0, self.__size):
                self.__array.append(None)
        else:
            self.__array = None

    # Getters y Setters
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def _array(self):
        return self.__array

    @_array.setter
    def _array(self, value):
        self.__array = value

    # Metodos
    def save_pos(self, value, pos):
        if pos < self.__size:
            self.__array[pos] = value
        else:
            raise Exception("Posicion fuera de rango")

    def save(self, value):
        if self.__position < self.__size:
            self.__array[self.__position] = value
            self.__position += 1
        else:
            raise Exception("Posicion fuera de rango")

    def check(self):
        for i, value in enumerate(self.__array):
            if value is None:
                return i
        return -1

    @property
    def __str__(self) -> str:
        return f"Size: {self.__size}, Array: {self.__array}"
