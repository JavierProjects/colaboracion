"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
    return len(calificaciones)


def sumar_calificaciones(calificaciones):
    return sum(calificaciones)

def calificacion_maxima(calificaciones):
    if not calificaciones:
        return None
    return max(calificaciones)

def calificacion_minima(calificaciones):
    if not calificaciones:
        return None
    return min(calificaciones)

def contar_aprobados(calificaciones):
    aprobados = 0
    for calificacion in calificaciones:
        if calificacion >= 70:
            aprobados += 1
    return aprobados


def contar_reprobados(calificaciones):
    reprobados = 0
    for calificacion in calificaciones:
        if calificacion < 70:
            reprobados += 1
    return reprobados


def clasificar_calificacion(calificacion):
    if calificacion >= 90:
        return "Excelente"
    elif calificacion >= 80:
        return "Bueno"
    elif calificacion >= 70:
        return "Regular"
    else:
        return "Reprobado"

def promedio(calificaciones):
    if not calificaciones:
        return None
    return sumar_calificaciones(calificaciones) / contar_calificaciones(calificaciones)


def porcentaje_aprobados(calificaciones):
    if not calificaciones:
        return 0.0
    return (contar_aprobados(calificaciones) / contar_calificaciones(calificaciones)) * 100


def porcentaje_reprobados(calificaciones):
    if not calificaciones:
        return 0.0
    return (contar_reprobados(calificaciones) / contar_calificaciones(calificaciones)) * 100


def frecuencia_calificaciones(calificaciones):
    frecuencias = {}
    for cal in calificaciones:
        if cal in frecuencias:
            frecuencias[cal] += 1
        else:
            frecuencias[cal] = 1
    return frecuencias

def moda(calificaciones):
    if not calificaciones:
        return None

    frecuencias = frecuencia_calificaciones(calificaciones)
    moda_val = None
    max_frecuencia = -1

    for cal, frec in frecuencias.items():
        if frec > max_frecuencia:
            max_frecuencia = frec
            moda_val = cal
            
    return moda_val

def mediana(calificaciones):
    if not calificaciones:
        return None

    ordenadas = sorted(calificaciones)
    n = len(ordenadas)
    mitad = n // 2

    # Si la cantidad es par

    if n % 2 == 0:
        return (ordenadas[mitad -1] + ordenadas[mitad]) / 2.0

    # Si es impar
    else:
        return ordenadas[mitad]


def resumen_calificaciones(calificaciones):
    if not calificaciones:
        return{
        "total": 0,
        "promedio": None,
        "moda": None,
        "mediana": None,
        "maxima": None,
        "minima": None,
        "porcentaje_aprobados": 0.0,
        "porcentaje_reprobados": 0.0,
        "distribucion": {}
        }

    return {
        "total": contar_calificaciones(calificaciones),
        "promedio": promedio(calificaciones),
        "moda": moda(calificaciones),
        "mediana": mediana(calificaciones),
        "maxima": calificacion_maxima(calificaciones),
        "minima": calificacion_minima(calificaciones),
        "porcentaje_aprobados": porcentaje_aprobados(calificaciones),
        "porcentaje_reprobados": porcentaje_reprobados(calificaciones),
        "distribucion": frecuencia_calificaciones(calificaciones)
    }
# by osvdevv