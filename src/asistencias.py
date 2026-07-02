"""
Módulo de asistencias.

Representación:
1 = asistió
0 = faltó
"""


def contar_clases(asistencias_alumno):

    return len(asistencias_alumno)

a=[1,1,0,1]
print(contar_clases(a))

def contar_asistencias(asistencias_alumno):
    contador=0
    for asistencia in asistencias_alumno:
        if asistencia == 1:
            contador+= 1
    return contador
    ##pass


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
