from datetime import datetime


class Atencion:
    def __init__(self):
        self.__id = 0
        self.__fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__comentario = " "
        self.__calificacion = " "
        self.__tiempo_despacho = 0
        self.__id_servidor_publico = 0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _comentario(self):
        return self.__comentario

    @_comentario.setter
    def _comentario(self, value):
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
            "calificacion": self.__calificacion,
            "tiempo_despacho": self.__tiempo_despacho,
            "id_servidor_publico": self.__id_servidor_publico,
        }

    def deserializable(data: dict):
        atencion = Atencion()
        atencion._id = data["id"]
        atencion._fecha = data["fecha"]
        atencion._comentario = data["comentario"]
        atencion._calificacion = data["calificacion"]
        atencion._tiempo_despacho = data["tiempo_despacho"]
        atencion._id_servidor_publico = data["id_servidor_publico"]
        return atencion

    def __str__(self) -> str:
        return f"Fecha: {self.__fecha}, Comentario: {self.__comentario}, Calificacion: {self.__calificacion}, Tiempo_Despacho: {self.__tiempo_despacho}, Id Servidor Publico: {self.__id_servidor_publico}"
