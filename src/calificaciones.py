"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
    """Cuenta cuántas calificaciones hay en una lista."""
    contador = 0
    for _ in calificaciones:
        contador += 1
    return contador


def sumar_calificaciones(calificaciones):
    """Suma todas las calificaciones de una lista."""
    suma = 0
    for calificacion in calificaciones:
        suma += calificacion
    return suma


def calificacion_maxima(calificaciones):
    """Regresa la calificación más alta. Si la lista está vacía, regresa None."""
    if not calificaciones:
        return None
    
    maxima = calificaciones[0]
    for calificacion in calificaciones:
        if calificacion > maxima:
            maxima = calificacion
    return maxima


def calificacion_minima(calificaciones):
    """Regresa la calificación más baja. Si la lista está vacía, regresa None."""
    if not calificaciones:
        return None
    
    minima = calificaciones[0]
    for calificacion in calificaciones:
        if calificacion < minima:
            minima = calificacion
    return minima


def contar_aprobados(calificaciones):
    """Cuenta cuántas calificaciones son mayores o iguales a 70."""
    aprobados = 0
    for calificacion in calificaciones:
        if calificacion >= 70:
            aprobados += 1
    return aprobados


def contar_reprobados(calificaciones):
    """Cuenta cuántas calificaciones son menores a 70."""
    reprobados = 0
    for calificacion in calificaciones:
        if calificacion < 70:
            reprobados += 1
    return reprobados


def clasificar_calificacion(calificacion):
    """Clasifica una calificación según los rangos establecidos."""
    if 90 <= calificacion <= 100:
        return "Excelente"
    elif 80 <= calificacion <= 89:
        return "Bueno"
    elif 70 <= calificacion <= 79:
        return "Regular"
    else:
        return "Reprobado"


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
