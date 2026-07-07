
"""
Módulo de asistencias.

Representación:
1 = asistió
0 = faltó
"""


def contar_clases(asistencias_alumno):
    if asistencias_alumno is None:
        return 0
    return len(asistencias_alumno)



def contar_asistencias(asistencias_alumno):
    rep = 0
    for n in asistencias_alumno:
        if n == 1:
            rep = rep + 1
    return rep



def contar_faltas(asistencias_alumno):
     rep = 0
    for n in asistencias_alumno:
        if n == 0:
            rep = rep + 1
    return rep


def porcentaje_asistencia(asistencias_alumno):
 if len(asistencias_alumno) == 0:
        return 0.0
    rep1 = 0
    for n in asistencias_alumno:
        if n == 1:
            rep1 = rep1 + 1
    porcentaje = (rep1 / len(asistencias_alumno)) * 100
    return porcentaje

def esta_en_riesgo(asistencias_alumno):
     rep = 0
    for n in asistencias_alumno:
        if n == 1:
            rep = rep + 1
    porcentaje = (rep / len(asistencias_alumno)) * 100
    if porcentaje < 80:
        return True
    else:
        return False

def alumnos_en_riesgo(asistencias):
    riesgo = []
    for alumno, lista_asistencia in asistencias.items():
        asistencias = 0
        alumnos = 0
        for n in lista_asistencia:
            alumnos = alumnos + 1
            if n == 1:
                asistencias = asistencias + 1
        porcentaje = (asistencias / alumnos) * 100
        if porcentaje < 80:
            riesgo.append(alumno)
    return riesgo
    
def promedio_asistencia_grupo(asistencias):
porcentajes = 0.0
    tot_almn = 0
    for alumno, lista_asistencia in asistencias.items():
        tot_almn = tot_almn +1
        asistencias = 0
        alumnos = 0
        for n in lista_asistencia:
            alumnos = alumnos + 1
            if n == 1:
                asistencias = asistencias + 1
        if alumnos > 0:
            porcentaje_individual = (asistencias / alumnos) * 100
        else:
            porcentaje_individual = 0.0
        porcentajes = porcentajes + porcentaje_individual
    if tot_almn > 0:
        prom = porcentajes / tot_almn
    else:
        prom = 0.0
    return prom
