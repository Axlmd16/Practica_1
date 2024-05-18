from controls.dao.data_access_object import Data_Access_Object
from models.servidor_publico import ServidorPublico


class ServidorControl(Data_Access_Object):
    def __init__(self, size: int):
        super().__init__(ServidorPublico, size)
        self.__servidor = None

    @property
    def _servidor(self):
        if self.__servidor == None:
            self.__servidor = ServidorPublico()
        return self.__servidor

    @_servidor.setter
    def _servidor(self, value):
        if isinstance(value, ServidorPublico):
            self.__servidor = value
        else:
            raise ValueError("El valor debe ser una instancia de ServidorPublico")

    @property
    def guardar(self):
        self._servidor._id = self._generate_id()
        self._save(self._servidor)
        self.__servidor = None

    def list(self):
        return self._list()

    def update(self, pos):
        self._merge(self._servidor, pos)
        self._servidor = None
