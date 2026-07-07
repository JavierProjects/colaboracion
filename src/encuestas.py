"""
Módulo de encuestas.
Implementa funciones para analizar respuestas usando listas y diccionarios.
"""


def contar_respuestas(respuestas):
    return len(respuestas)


def obtener_opciones(respuestas):
    opciones = []

    for respuesta in respuestas:
        if respuesta not in opciones:
            opciones.append(respuesta)

    return opciones


def frecuencia_respuestas(respuestas):
    frecuencias = {}

    for respuesta in respuestas:
        if respuesta in frecuencias:
            frecuencias[respuesta] += 1
        else:
            frecuencias[respuesta] = 1

    return frecuencias


def respuesta_mas_comun(respuestas):
    if len(respuestas) == 0:
        return None

    frecuencias = frecuencia_respuestas(respuestas)

    mayor = 0
    comun = None

    for respuesta in frecuencias:
        if frecuencias[respuesta] > mayor:
            mayor = frecuencias[respuesta]
            comun = respuesta

    return comun



def porcentaje_respuesta(respuestas, opcion):
    if len(respuestas) == 0:
        return 0.0

    contador = 0

    for respuesta in respuestas:
        if respuesta == opcion:
            contador += 1

    return (contador / len(respuestas)) * 100


def resumen_encuesta(respuestas):
    resumen = {
        "total": contar_respuestas(respuestas),
        "opciones": obtener_opciones(respuestas),
        "frecuencias": frecuencia_respuestas(respuestas),
        "mas_comun": respuesta_mas_comun(respuestas)
    }

    return resumen