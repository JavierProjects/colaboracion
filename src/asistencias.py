"""
Módulo de asistencias.

Representación:
1 = asistió
0 = faltó
"""

def contar_clases(asistencias_alumno):
    total_clases = len(asistencias_alumno)
    return total_clases

def contar_asistencias(asistencias_alumno):
    asistencias = 0
    for asistencia in asistencias_alumno:
        if asistencia == 1:
            asistencias = asistencias + 1
    return asistencias

def contar_faltas(asistencias_alumno):
    faltas = 0
    for falta in asistencias_alumno:
        if falta == 0:
            faltas = faltas + 1
    return faltas

def porcentaje_asistencia(asistencias_alumno):
    if len(asistencias_alumno) == 0:
        return 0.0
    total_clases = len(asistencias_alumno)
    asistencias = 0
    for asis in asistencias_alumno:
        if asis == 1:
            asistencias = asistencias + 1
            
    porcentaje = (asistencias / total_clases) * 100
    return porcentaje

def esta_en_riesgo(asistencias_alumno):
    if len(asistencias_alumno) == 0:
        return True
    total_clases = len(asistencias_alumno)
    asistencias = 0
    for asis in asistencias_alumno:
        if asis == 1:
            asistencias = asistencias + 1
    porcentaje = (asistencias / total_clases) * 100
    if porcentaje < 80:
        return True
    else:
        return False


def alumnos_en_riesgo(asistencias):
    en_riesgo = []
    for alumno, lista_asistencias in asistencias.items():
        
        if len(lista_asistencias) == 0:
            en_riesgo.append(alumno)
        else:
            unos = 0
            for asis in lista_asistencias:
                if asis == 1:
                    unos = unos + 1
            porcentaje = (unos / len(lista_asistencias)) * 100
            if porcentaje < 80:
                en_riesgo.append(alumno)
    return en_riesgo
   


def promedio_asistencia_grupo(asistencias):
    if len(asistencias) == 0:
        return 0.0
    suma_porcentajes = 0
    for alumno in asistencias:
        lista_asistencias = asistencias[alumno]
        if len(lista_asistencias) == 0:
            porcentaje_alumno = 0.0
        else:
            unos = 0
            for asis in lista_asistencias:
                if asis == 1:
                    unos = unos + 1
            porcentaje_alumno = (unos / len(lista_asistencias)) * 100
        suma_porcentajes = suma_porcentajes + porcentaje_alumno
    promedio_grupo = suma_porcentajes / len(asistencias)
    
    return promedio_grupo