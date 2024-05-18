from flask import Blueprint, request, redirect, render_template, url_for

from controls.atencion_control import AtencionControl
from controls.servidor_control import ServidorControl
from models.enum_calificacion import EnumCalificacion

router = Blueprint("router", __name__)

vc = ServidorControl()
ac = AtencionControl()


@router.route("/")
def home():
    servicios = vc.list()
    return render_template("index.html", servicios=servicios)


@router.route("/atencion/guardar/<int:id>", methods=["POST", "GET"])
def guardar_atencion(id):

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
        return redirect(url_for("router.home"))

    return render_template("atenciones/guardar.html", calificaciones=calificaciones)


@router.route("/atencion/listar/<int:id>")
def listar_atenciones(id):

    atenciones = [
        atencion.serializable()
        for atencion in ac.list()
        if atencion._id_servidor_publico == id
    ]

    return render_template("atenciones/listar.html", atenciones=atenciones)
