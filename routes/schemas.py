# schemas.py

person_schema = {
    "type": "object",
    "properties": {
        "apellidos": {"type": "string"},
        "nombres": {"type": "string"},
        "direccion": {"type": "string"},
        "tipo": {"type": "string"},
        "telefono": {"type": "string"},
        "dni": {"type": "string"},
    },
    "required": ["apellidos", "nombres", "direccion", "tipo", "telefono", "dni"],
}

censo_schema = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "fecha": {"type": "string"},
        "direccion": {"type": "string"},
    },
    "required": ["nombre", "fecha", "direccion"],
}
