import sys

from models.servidor_publico import ServidorPublico

sys.path.append("../")

from controls.servidor_control import ServidorControl

ac = ServidorControl()

ac._servidor._nombre = "Juan Perez"
ac._servidor._descripcion = "Servicio de atencion al cliente"
ac.guardar

ac._servidor._nombre = "Maria Lopez"
ac._servidor._descripcion = "Servicio de cobranza"
ac.guardar

ac._servidor._nombre = "Pedro Ramirez"
ac._servidor._descripcion = "Servicio de ventas"
ac.guardar
