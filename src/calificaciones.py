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
    if len(calificaciones) == 0:
        return None
    return max(calificaciones)

def calificacion_minima(calificaciones):
    if len(calificaciones) == 0:
        return None
    return min(calificaciones)


def contar_aprobados(calificaciones):
    contador = 0

    for calificacion in calificaciones:
        if calificacion >= 70:
            contador += 1

    return contador


def contar_reprobados(calificaciones):
    contador = 0

    for calificacion in calificaciones:
        if calificacion < 70:
            contador += 1

    return contador

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
    if len(calificaciones) == 0:
        return None
    return sum(calificaciones) / len(calificaciones)


def porcentaje_aprobados(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    return (contar_aprobados(calificaciones) / len(calificaciones)) * 100


def porcentaje_reprobados(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    return (contar_reprobados(calificaciones) / len(calificaciones)) * 100


def frecuencia_calificaciones(calificaciones):
    frecuencias = {}

    for calificacion in calificaciones:
        if calificacion in frecuencias:
            frecuencias[calificacion] += 1
        else:
            frecuencias[calificacion] = 1

    return frecuencias


def moda(calificaciones):
    if len(calificaciones) == 0:
        return None

    frecuencias = frecuencia_calificaciones(calificaciones)

    mayor_frecuencia = max(frecuencias.values())

    for calificacion, frecuencia in frecuencias.items():
        if frecuencia == mayor_frecuencia:
            return calificacion


def mediana(calificaciones):
    if len(calificaciones) == 0:
        return None

    datos = sorted(calificaciones)
    n = len(datos)

    if n % 2 == 1:
        return datos[n // 2]
    else:
        return (datos[n // 2 - 1] + datos[n // 2]) / 2


def resumen_calificaciones(calificaciones):
    if len(calificaciones) == 0:
        return {
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
