"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
    pass


def sumar_calificaciones(calificaciones):
    pass


def calificacion_maxima(calificaciones):
    pass


def calificacion_minima(calificaciones):
    pass


def contar_aprobados(calificaciones):
    pass


def contar_reprobados(calificaciones):
    pass


def clasificar_calificacion(calificacion):
    pass


def promedio(calificaciones):
      if len(calificaciones) == 0:
        return None

    suma = 0

    for calificacion in calificaciones:
        suma += calificacion

    return suma / len(calificaciones)


def porcentaje_aprobados(calificaciones):
     if len(calificaciones) == 0:
        return 0.0

    aprobados = 0

    for calificacion in calificaciones:
        if calificacion >= 70:
            aprobados += 1

    return (aprobados / len(calificaciones)) * 100



def porcentaje_reprobados(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    reprobados = 0

    for calificacion in calificaciones:
        if calificacion <70:
           reprobados += 1

    return (reprobados / len(calificaciones)) * 100




def frecuencia_calificaciones(calificaciones):
     if len(cal) == 0:
        return {}

    frecuencia = {}

    for numero in cal:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1

    return frecuencia


def moda(calificaciones):
    if len(calificaciones) == 0:
        return None

    mayor = 0
    moda = None

    for calificacion in calificaciones:
        repeticiones = 0

        for valores in calificaciones:
            if calificacion == valores:
                repeticiones += 1

        if repeticiones > mayor:
            mayor = repeticiones
            moda = calificacion

    return moda


def mediana(calificaciones):
     if len(calificaciones) == 0:
        return None

    calificaciones = sorted(calificaciones)
    valor = len(calificaciones)
    
    if valor%2==1:
        return calificaciones[valor //2]
    else:
        mediana1 = calificaciones[valor //2-1]
        mediana2 = calificaciones[valor //2]
        return(mediana1 + mediana2 )/2
        



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
        "total": len(calificaciones),
        "promedio": promedio(calificaciones),
        "moda": moda(calificaciones),
        "mediana": mediana(calificaciones),
        "maxima": max(calificaciones),
        "minima": min(calificaciones),
        "porcentaje_aprobados": porcentaje_aprobados(calificaciones),
        "porcentaje_reprobados": porcentaje_reprobados(calificaciones),
        "distribucion": frecuencia_calificaciones(calificaciones)
    }

