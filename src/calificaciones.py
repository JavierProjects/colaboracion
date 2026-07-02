"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
    contador = 0

    for calificacion in calificaciones:
        contador += 1

    return contador



def sumar_calificaciones(calificaciones):
    suma = 0

    for calificacion in calificaciones:
        suma += calificacion

    return suma



def calificacion_maxima(calificaciones):
    if len(calificaciones) == 0:
        return None

    maxima = calificaciones[0]

    for calificacion in calificaciones:
        if calificacion > maxima:
            maxima = calificacion

    return maxima



def calificacion_minima(calificaciones):
    if len(calificaciones) == 0:
        return None

    minima = calificaciones[0]

    for calificacion in calificaciones:
        if calificacion < minima:
            minima = calificacion

    return minima


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
    if contar_calificaciones(calificaciones) == 0:
        return None

    return sumar_calificaciones(calificaciones) / contar_calificaciones(calificaciones)


def porcentaje_aprobados(calificaciones):
    if contar_calificaciones(calificaciones) == 0:
        return 0.0

    return (contar_aprobados(calificaciones) * 100) / contar_calificaciones(calificaciones)


def porcentaje_reprobados(calificaciones):
    if contar_calificaciones(calificaciones) == 0:
        return 0.0

    return (contar_reprobados(calificaciones) * 100) / contar_calificaciones(calificaciones)



def frecuencia_calificaciones(calificaciones):
    frecuencias = {}

    for calificacion in calificaciones:
        if calificacion in frecuencias:
            frecuencias[calificacion] += 1
        else:
            frecuencias[calificacion] = 1

    return frecuencias

def moda(calificaciones):
    if contar_calificaciones(calificaciones) == 0:
        return None

    frecuencias = frecuencia_calificaciones(calificaciones)

    mayor_frecuencia = 0
    resultado = None

    for calificacion in frecuencias:
        if frecuencias[calificacion] > mayor_frecuencia:
            mayor_frecuencia = frecuencias[calificacion]
            resultado = calificacion

    return resultado



def mediana(calificaciones):
    pass


def resumen_calificaciones(calificaciones):
    pass
