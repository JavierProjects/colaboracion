"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_clases(asistencias_alumno):
    pass
    
def contar_calificaciones(calificaciones):
    contador = 0
    for calificacion in calificaciones:
        contador += 1
    return contador

def contar_asistencias(asistencias_alumno):
    pass
def sumar_calificaciones(calificaciones):
    suma = 0

    for calificacion in calificaciones:
        suma += calificacion

    return suma

def contar_faltas(asistencias_alumno):
    pass
def calificacion_maxima(calificaciones):
    if calificaciones == []:
        return None
    maxima = calificaciones[0]
    for calificacion in calificaciones:
        if calificacion > maxima:
            maxima = calificacion
    return maxima

def porcentaje_asistencia(asistencias_alumno):
    pass
def calificacion_minima(calificaciones):
    if calificaciones ==[]:
        return None 
    minima = calificacion[0]
    for calificacion in calificaciones:
        if calificaion < minima:
            minima = calificacion
    return minima 

def esta_en_riesgo(asistencias_alumno):
    pass
def contar_aprobados(calificaciones):
    if calificaciones <=70:
        return "Mayor que 70"
    else:
        return "Menor que 70"

def alumnos_en_riesgo(asistencias):
    pass
def contar_reprobados(calificaciones):
    if calificaciones <70:
        return "Aprobado"
    else:
        return "Reprobado"

def promedio_asistencia_grupo(asistencias):
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