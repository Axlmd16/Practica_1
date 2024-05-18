from models.enum_calificacion import EnumCalificacion


class Atencion:
    def __init__(self):
        self.__id = 0
        self.__fecha = " "
        self.__comentario = " "
        self.__calificacion = EnumCalificacion.BUENO
        self.__tiempo_despacho = 0
        self.__id_servidor_publico = 0

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _descripcion(self):
        return self.__comentario

    @_descripcion.setter
    def _descripcion(self, value):
        self.__comentario = value

    @property
    def _calificacion(self):
        return self.__calificacion

    @_calificacion.setter
    def _calificacion(self, value):
        self.__calificacion = value

    @property
    def _tiempo_despacho(self):
        return self.__tiempo_despacho

    @_tiempo_despacho.setter
    def _tiempo_despacho(self, value):
        self.__tiempo_despacho = value

    @property
    def _id_servidor_publico(self):
        return self.__id_servidor_publico

    @_id_servidor_publico.setter
    def _id_servidor_publico(self, value):
        self.__id_servidor_publico = value

    def serializable(self):
        return {
            "id": self.__id,
            "fecha": self.__fecha,
            "comentario": self.__comentario,
            "calificacion": self.__calificacion.capitalize(),
            "tiempo_despacho": self.__tiempo_despacho,
            "id_servidor_publico": self.__id_servidor_publico,
        }

    def deserializable(data: dict):
        atencion = Atencion()
        atencion._id = data["id"]
        atencion._fecha = data["fecha"]
        atencion._comentario = data["comentario"]
        atencion._calificacion = EnumCalificacion[data["calificacion"].upper()]
        atencion._tiempo_despacho = data["tiempo_despacho"]
        atencion._id_servidor_publico = data["id_servidor_publico"]
        return atencion

    def __str__(self) -> str:
        return str(self.__id) + " " + self.__fecha + " " + self.__comentario
