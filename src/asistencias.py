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
    pass


def porcentaje_asistencia(asistencias_alumno):
    pass


def esta_en_riesgo(asistencias_alumno):
    pass


def alumnos_en_riesgo(asistencias):
    pass


def promedio_asistencia_grupo(asistencias):
    pass
