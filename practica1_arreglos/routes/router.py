from flask import Blueprint, request, redirect, render_template, url_for
import time

from controls.atencion_control import AtencionControl
from controls.servidor_control import ServidorControl
from models.enum_calificacion import EnumCalificacion

router = Blueprint("router", __name__)

vc = ServidorControl(3)
ac = AtencionControl(10)


@router.route("/")
def home():

    try:
        servicios = vc.list()
    except Exception as e:
        print(e)

    return render_template("index.html", servicios=servicios)


@router.route("/atencion/guardar/<int:id>", methods=["POST", "GET"])
def guardar_atencion(id):
    start_time = time.time()

    calificaciones = [
        (EnumCalificacion.value, EnumCalificacion.name.capitalize())
        for EnumCalificacion in EnumCalificacion
    ]

    if request.method == "POST":
        data = request.form
        ac._atencion._id_servidor_publico = id
        ac._atencion._fecha = str(data["fecha"])
        ac._atencion._tiempo_despacho = data["tiempo"]
        ac._atencion._comentario = data["comentario"]
        ac._atencion._calificacion = EnumCalificacion[data["calificacion"].upper()]
        ac.save
        end_time = time.time()
        print(
            "Tiempo de ejecución de guardar_atencion (POST): ",
            end_time - start_time,
            "segundos",
        )
        return redirect(url_for("router.home"))

    end_time = time.time()
    print(
        "Tiempo de ejecución de guardar_atencion (GET): ",
        end_time - start_time,
        "segundos",
    )

    return render_template("atenciones/guardar.html", calificaciones=calificaciones)


@router.route("/atencion/listar/<int:id>")
def listar_atenciones(id):
    start_time = time.time()

    atenciones = [
        atencion.serializable()
        for atencion in ac.list()
        if atencion is not None and atencion._id_servidor_publico == id
    ]

    end_time = time.time()
    print(
        "Tiempo de ejecución de listar_atenciones: ", end_time - start_time, "segundos"
    )

    return render_template("atenciones/listar.html", atenciones=atenciones)
