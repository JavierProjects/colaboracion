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
    pass


def porcentaje_respuesta(respuestas, opcion):
    pass


def resumen_encuesta(respuestas):
    pass