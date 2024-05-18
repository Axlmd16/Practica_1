from controls.dao.data_access_object import Data_Access_Object
from models.atencion import Atencion


class AtencionControl(Data_Access_Object):
    def __init__(self, size: int):
        super().__init__(Atencion, size)
        self.__atencion = None

    @property
    def _atencion(self):
        if self.__atencion == None:
            self.__atencion = Atencion()
        return self.__atencion

    @_atencion.setter
    def _atencion(self, value):
        if isinstance(value, Atencion):
            self.__atencion = value
        else:
            raise ValueError("El valor debe ser una instancia de ServidorPublico")

    @property
    def save(self):
        self._atencion._id = self._generate_id()
        self._save(self._atencion)
        self.__atencion = None

    def list(self):
        return self._list()

    def update(self, pos):
        self._merge(self._atencion, pos)
        self.__atencion = None
