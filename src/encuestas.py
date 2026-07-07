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
    frecuencias = {}
    for respuesta in respuestas:
        if respuesta in frecuencias:
            frecuencias[respuesta] += 1
        else:
            frecuencias[respuesta] = 1
    return frecuencias
    pass


def respuesta_mas_comun(respuestas):
    if not respuestas:
        return None
 
    frecuencias = frecuencia_respuestas(respuestas)
 
    mas_comun = None
    max_conteo = -1
    for opcion in obtener_opciones(respuestas):
        if frecuencias[opcion] > max_conteo:
            max_conteo = frecuencias[opcion]
            mas_comun = opcion
 
    return mas_comun
    pass


def porcentaje_respuesta(respuestas, opcion):
    pass


def resumen_encuesta(respuestas):
    pass
