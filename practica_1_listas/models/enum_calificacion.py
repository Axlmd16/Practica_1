from enum import Enum


class EnumCalificacion(Enum):
    BUENO = "BUENO"
    REGULAR = "REGULAR"
    MALO = "MALO"
    MUY_BUENO = "MUY BUENO"
    EXCELENTE = "EXCELENTE"

    def capitalize(self):
        return self.value.capitalize()

    def get_value(self):
        return self.value
