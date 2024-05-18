import sys

from models.servidor_publico import ServidorPublico

sys.path.append("../")

from controls.servidor_control import ServidorControl
from controls.servidor_control_array import ServidorControlArray

ac = ServidorControlArray(5)
ac._servidor._nombre = "Juan"
ac._servidor._descripcion = "Descripcion"
ac.save

print(ac.__servidores.__str__)
