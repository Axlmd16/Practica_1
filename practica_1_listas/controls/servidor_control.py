from controls.dao.data_access_object import Data_Access_Object
from models.servidor_publico import ServidorPublico


class ServidorControl(Data_Access_Object):
    def __init__(self):

        super().__init__(ServidorPublico)
        self.__servidor = None

    @property
    def _servidor(self):
        if self.__servidor == None:
            self.__servidor = ServidorPublico()
        return self.__servidor

    @_servidor.setter
    def _servidor(self, value):
        self.__servidor = value

    @property
    def save(self):
        self._servidor._id = self._generate_id()
        self._save(self._servidor)
        self.__servidor = None

    def list(self):
        return self._list()

    def update(self, pos):
        self._merge(self._servidor, pos)
        self.__servidor = None
