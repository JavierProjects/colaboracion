"""
Módulo de asistencias.

Representación:
1 = asistió
0 = faltó
"""


def contar_clases(asistencias_alumno):
    contador = 0 
    for clase in asistencias_alumno:
        contador = contador + 1
    return contador


def contar_asistencias(asistencias_alumno):
    contador = 0
    for clase in asistencias_alumno:
        if clase == 1:
            contador = contador + 1
    return contador


def contar_faltas(asistencias_alumno):
    contador = 0
    for clase in asistencias_alumno:
        if clase == 0:
            contador = contador + 1
    return contador


def porcentaje_asistencia(asistencias_alumno):
    contador = 0
    for clase in asistencias_alumno:
        if clase == 1:
            contador = contador + 25.0
    return contador


def esta_en_riesgo(asistencias_alumno):
    contador = 0
    for clase in asistencias_alumno:
        if clase == 1:
            contador = contador + 25.0
    if contador == 0:
        return False
    if contador <= 80:
        return True
    else:
        return False

def alumnos_en_riesgo(asistencias):
    lista_en_riesgo = []
    for nombre in asistencias:
        notas = asistencias[nombre]
        asis = 0
        for clase in notas:
            if clase == 1:
                asis = asis + 25.0
        if asis < 80:
            lista_en_riesgo.append(nombre)
    return lista_en_riesgo

def promedio_asistencia_grupo(asistencias):
    if asistencias == []:
        return 0.0
    suma_porcentajes = 0.0
    contador_alumnos = 0
    for nombre in asistencias:
        notas = asistencias[nombre]
        asistencias_alumno = 0
        total_clases_alumno = 0
        for clase in notas:
            total_clases_alumno = total_clases_alumno + 1
            if clase == 1:
                asistencias_alumno = asistencias_alumno + 1
        if total_clases_alumno > 0:
            porcentaje = (asistencias_alumno / total_clases_alumno) * 100
            suma_porcentajes = suma_porcentajes + porcentaje
        contador_alumnos = contador_alumnos + 1
    if contador_alumnos > 0:
        return suma_porcentajes / contador_alumnos
    else:
        return 0.0
