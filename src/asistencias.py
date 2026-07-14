"""
Módulo de asistencias.

Representación:
1 = asistió
0 = faltó
"""


def contar_clases(asistencias_alumno):
    c = 0
    for clase in asistencias_alumno:
        c = c + 1
    return c


def contar_asistencias(asistencias_alumno):
    c=0
    for asistencias in asistencias_alumno:
        if asistencias ==1:
           c= c + 1
    return c


def contar_faltas(asistencias_alumno):
    c=0
    for faltas in asistencias_alumno:
        if faltas ==0:
           c= c + 1
    return c


def porcentaje_asistencia(asistencias_alumno):
    asistencias = 0
    total = 0
    for asistencia in asistencias_alumno:
        total = total + 1
        if asistencia == 1:
            asistencias = asistencias + 1
    if total == 0:
        return 0.0
    return (asistencias * 100) / total


def esta_en_riesgo(asistencias_alumno):
    if porcentaje_asistencia(asistencias_alumno) <80:
       return True
    else:
        return False


def alumnos_en_riesgo(asistencias):
    riesgo=[]
    for alumno in asistencias:
         if esta_en_riesgo(asistencias[alumno]):
            riesgo.append(alumno)
    return riesgo


def promedio_asistencia_grupo(asistencias):
    suma=0
    total=0
    for alumno in asistencias:
        suma= suma + porcentaje_asistencia(asistencias [alumno])
        total= total + 1
    if total == 0:
       return 0

    return suma/total
