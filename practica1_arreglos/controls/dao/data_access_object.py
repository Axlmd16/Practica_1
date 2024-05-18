from typing import Type, TypeVar, Generic

import json
import os

from controls.tda.array.array import Array
from controls.tda.list.linked_list import Linked_List


T = TypeVar("T")


class Data_Access_Object(Generic[T]):
    atype: T

    def __init__(self, atype: T, array_size: int):
        self.atype = atype
        self.arreglo = Array(array_size)
        self.file = atype.__name__.lower() + ".json"
        self.url = (
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            + "/data/"
        )

    def _list(self) -> T:
        if os.path.isfile(self.url + self.file):
            with open(self.url + self.file, "r") as f:
                datos = json.load(f)
                self.arreglo.clear()
                for i, data in enumerate(datos):
                    a = self.atype.deserializable(data)
                    self.arreglo.save_pos(a, i)
        return self.arreglo

    def __transform__(self):
        return json.dumps(
            [
                self.arreglo._array[i].serializable()
                for i in range(self.arreglo._size)
                if self.arreglo._array[i] is not None
            ],
            indent=4,
        )

    def _to_dict(self):
        aux = []
        self._list()
        for i in range(self.arreglo._size):
            if self.arreglo._array[i] is not None:
                aux.append(self.arreglo._array[i].serializable())
        return aux

    def _save(self, data: T) -> None:
        self.arreglo.save(data)
        existing_data = []
        if os.path.isfile(self.url + self.file):
            with open(self.url + self.file, "r") as a:
                existing_data = json.load(a)
        existing_data.append(data.serializable())
        with open(self.url + self.file, "w") as a:
            a.write(json.dumps(existing_data, indent=4))

    def _merge(self, data: T, pos) -> None:
        self.arreglo.save_pos(data, pos)
        with open(self.url + self.file, "w") as a:
            a.write(self.__transform__())

    def _generate_id(self) -> int:
        arreglo = self._list()
        if arreglo._size == 0:
            return 0
        else:
            for i in range(arreglo._size - 1, -1, -1):
                if arreglo._array[i] is not None:
                    return arreglo._array[i]._id + 1
            return 0
