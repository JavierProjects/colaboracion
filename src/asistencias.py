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
    pass
