from controls.tda.list.linked_list import Linked_List
from controls.tda.list.searchs.search import Search
from flask import (
    Blueprint,
    request,
    redirect,
    render_template,
    url_for,
    make_response,
    jsonify,
)

from controls.atencion_control import AtencionControl
from controls.servidor_control import ServidorControl

router = Blueprint("router", __name__)

vc = ServidorControl()
ac = AtencionControl()


@router.route("/")
def home():
    servicios = vc.list()

    print(type(servicios))

    return render_template("index.html", servicios=servicios)


@router.route("/atencion/guardar/<int:id>", methods=["POST", "GET"])
def guardar_atencion(id):

    if request.method == "POST":
        data = request.form
        if (
            "fecha" in data
            and "tiempo" in data
            and "comentario" in data
            and "calificacion" in data
        ):
            ac._atencion._id_servidor_publico = id
            ac._atencion._fecha = data["fecha"]
            ac._atencion._tiempo_despacho = int(data["tiempo"])
            ac._atencion._comentario = data["comentario"]
            ac._atencion._calificacion = data["calificacion"]
            ac.save()

    return render_template("atenciones/guardar.html")


@router.route("/atencion/listar/<int:id>", methods=["GET"])
def listar_atenciones(id):
    atenciones = Linked_List()

    for atencion in ac.list():
        if atencion._id_servidor_publico == id:
            atenciones.add(atencion.serializable())

    atributos = ["Fecha", "Comentario", "Calificacion", "Tiempo_Despacho"]
    return render_template(
        "atenciones/listar.html", atenciones=atenciones, atributos=atributos, id=id
    )


@router.route("/atencion/ordenar/<int:id>", methods=["GET"])
def ordenar_atenciones(id):
    sort_method = request.args.get("sort_method", "quick_sort")
    attr = request.args.get("attr")
    order = request.args.get("order")
    print(sort_method, attr, order)

    atenciones = Linked_List()

    for atencion in ac.list():
        if atencion._id_servidor_publico == id:
            atenciones.add(atencion)

    sorted_atenciones = atenciones.sort_models(attr, int(order), sort_method)

    return jsonify(
        {
            "msg": "Ordenado exitosamente",
            "data": [atencion.serializable() for atencion in sorted_atenciones],
        }
    )


@router.route("/atencion/buscar/<int:id>", methods=["GET"])
def buscar_atenciones(id):
    value_search = request.args.get("text")
    attr_search = request.args.get("attr")

    atenciones = Linked_List()

    for atencion in ac.list():
        if atencion._id_servidor_publico == id:
            atenciones.add(atencion)

    if attr_search == "fecha":
        atencion_found = Search().search_models_binary(
            attr_search, value_search, atenciones
        )
        found_atenciones = Linked_List()
        if atencion_found is not None:
            found_atenciones.add(atencion_found)

    elif attr_search == "calificacion":
        found_atenciones = Search().search_models_lb(
            attr_search, value_search, atenciones
        )
    elif attr_search == "tiempo_despacho_menor":
        found_atenciones = Search().search_tiempo_menor(
            "tiempo_despacho", int(value_search), atenciones
        )
    elif attr_search == "tiempo_despacho_mayor":
        found_atenciones = Search().search_tiempo_mayor(
            "tiempo_despacho", int(value_search), atenciones
        )

    return jsonify(
        {
            "msg": "Busqueda exitosa",
            "data": [atencion.serializable() for atencion in found_atenciones],
        }
    )
