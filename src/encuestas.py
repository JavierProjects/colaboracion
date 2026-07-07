"""
Módulo de encuestas.

Implementa funciones para analizar respuestas usando listas y diccionarios.
"""


def contar_respuestas(respuestas):
    total = 0

    for respuesta in respuestas:
        total = total + 1

    return total

def obtener_opciones(respuestas):
    opciones = []

    for respuesta in respuestas:
        if respuesta not in opciones:
            opciones.append(respuesta)

    return opciones


def frecuencia_respuestas(respuestas):
    pass


def respuesta_mas_comun(respuestas):
    pass


def porcentaje_respuesta(respuestas, opcion):
    pass


def resumen_encuesta(respuestas):
    pass

