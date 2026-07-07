"""
Módulo de encuestas.

Implementa funciones para analizar respuestas usando listas y diccionarios.
"""


def contar_respuestas(respuestas):
    if respuestas is None:
        return 0
    return len(respuestas)


def obtener_opciones(respuestas):
    if respuestas is None:
        return []
    opciones_unicas = []
    for respuesta in respuestas:
        if respuesta not in opciones_unicas:
            opciones_unicas.append(respuesta)
    return opciones_unicas


def frecuencia_respuestas(respuestas):
    frec = {}
    for frecuencia in respuestas:
        if frecuencia in frec:
            frec[frecuencia] += 1
        else:
            frec[frecuencia] =1
    return frec


def respuesta_mas_comun(respuestas):
    if respuestas is None or len(respuestas) == 0:
        return None        
    frec = {}
    for rep in respuestas:
        if rep in frec:
            frec[rep] += 1
        else:
            frec[rep] = 1          
    mas_rep = None
    mayorval = -1
    for r, contar in frec.items():
        if contar > mayorval:
            mayorval = contar
            mas_rep = r
    return mas_rep


def porcentaje_respuesta(respuestas, opcion):
    if len(respuestas) == 0:
        return 0.0
    coincidencias = 0
    for r in respuestas:
        if r == opcion:
            coincidencias += 1
    porcentaje = (coincidencias / len(respuestas)) * 100
    
    return porcentaje


def resumen_encuesta(respuestas):
    if respuestas is None:
        respuestas = []
    resumen = {
        "total": contar_respuestas(respuestas),
        "opciones": obtener_opciones(respuestas),
        "frecuencias": frecuencia_respuestas(respuestas),
        "mas_comun": respuesta_mas_comun(respuestas)
    }
    return resumen