"""
Módulo de encuestas.

Implementa funciones para analizar respuestas usando listas y diccionarios.
"""


def contar_respuestas(respuestas):
    return len(respuestas)
    pass


def obtener_opciones(respuestas):
    opciones = []
    for respuesta in respuestas:
        if respuesta not in opciones:
            opciones.append(respuesta)
    return opciones
    pass


def frecuencia_respuestas(respuestas):
    pass


def respuesta_mas_comun(respuestas):
    pass


def porcentaje_respuesta(respuestas, opcion):
    pass


def resumen_encuesta(respuestas):
    pass
