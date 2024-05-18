class ServidorPublico:
    def __init__(self) -> None:
        self.__id = 0
        self.__nombre = ""
        self.__descripcion = " "

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _descripcion(self, value):
        self.__descripcion = value

    def serializable(self):
        return {
            "id": self.__id,
            "nombre": self._nombre,
            "descripcion": self.__descripcion,
        }

    def deserializable(data: dict):
        servidor_publico = ServidorPublico()
        servidor_publico._id = data["id"]
        servidor_publico._nombre = data["nombre"]
        servidor_publico._descripcion = data["descripcion"]
        return servidor_publico

    def __str__(self) -> str:
        return f"{self.__id} - {self.__nombre} - {self.__descripcion}"
