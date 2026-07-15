"""
Módulo de asistencias.

Representación:
1 = asistió
0 = faltó
"""


def contar_clases(asistencias_alumno):
    return len(asistencias_alumno)


def contar_asistencias(asistencias_alumno):
    return asistencias_alumno.count(1)


def contar_faltas(asistencias_alumno):
    return asistencias_alumno.count(0)


def porcentaje_asistencia(asistencias_alumno):
    total_clases = contar_clases(asistencias_alumno)
    if total_clases == 0:
        return 0.0

    asistencias = contar_asistencias(asistencias_alumno)
    return (asistencias / total_clases) * 100



def esta_en_riesgo(asistencias_alumno):
    return porcentaje_asistencia(asistencias_alumno) < 80



def alumnos_en_riesgo(asistencias):
    lista_riesgo = []
    for alumno, lista_asistencias in asistencias.items():
        if esta_en_riesgo(lista_asistencias):
            lista_riesgo.append(alumno)
    return lista_riesgo


def promedio_asistencia_grupo(asistencias):
 
    if not asistencias:
        return 0.0
    
    suma_porcentajes = 0.0
    total_alumnos = len(asistencias)
    
    for lista_asistencias in asistencias.values():
        suma_porcentajes += porcentaje_asistencia(lista_asistencias)
        
    return suma_porcentajes / total_alumnos
