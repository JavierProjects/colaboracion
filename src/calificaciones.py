"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
     return len(calificaciones)
    pass


def sumar_calificaciones(calificaciones):
    return sum(calificaciones)
    pass


def calificacion_maxima(calificaciones):
    if contar_calificaciones(calificaciones) == 0:
        return None
    maxima = calificaciones[0]
    for calificacion in calificaciones:
        if calificacion > maxima:
            maxima = calificacion
    return maxima
    
    pass


def calificacion_minima(calificaciones):
    if contar_calificaciones(calificaciones) == 0:
        return None
 
    minima = calificaciones[0]
    for calificacion in calificaciones:
        if calificacion < minima:
            minima = calificacion
    return minima
    pass


def contar_aprobados(calificaciones):
    contador = 0
    for calificacion in calificaciones:
        if calificacion >= 70:
            contador += 1
    return contador
    pass


def contar_reprobados(calificaciones):
    contador = 0
    for calificacion in calificaciones:
        if calificacion < 70:
            contador += 1
    return contador
    pass


def clasificar_calificacion(calificacion):
     if calificacion >= 90:
        return "Excelente"
    elif calificacion >= 80:
        return "Bueno"
    elif calificacion >= 70:
        return "Regular"
    else:
        return "Reprobado"
    pass


def promedio(calificaciones):
    pass


def porcentaje_aprobados(calificaciones):
    pass


def porcentaje_reprobados(calificaciones):
    pass


def frecuencia_calificaciones(calificaciones):
    pass


def moda(calificaciones):
    pass


def mediana(calificaciones):
    pass


def resumen_calificaciones(calificaciones):
    pass
