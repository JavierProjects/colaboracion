"""
Módulo de asistencias.

Representación:
1 = asistió
0 = faltó
"""


def contar_clases(asistencias_alumno):
    return len(asistencias_alumno)

#contar_clases([1, 1, 0, 1])


def contar_asistencias(asistencias_alumno):
    return asistencias_alumno.count(1)

#contar_asistencias([1, 1, 0, 1])

def contar_faltas(asistencias_alumno):
    return asistencias_alumno.count(0)

#contar_faltas([1, 1, 0, 1])


def porcentaje_asistencia(asistencias_alumno):
    total_clases = contar_clases(asistencias_alumno)
    if total_clases == 0:
        return 0.0
    
    asistencias = contar_asistencias(asistencias_alumno)
    return (asistencias / total_clases) * 100

porcentaje_asistencia([1, 1, 0, 1])


def esta_en_riesgo(asistencias_alumno):
    return porcentaje_asistencia(asistencias_alumno) < 80

#esta_en_riesgo([1, 1, 0, 1])


def alumnos_en_riesgo(asistencias):
    lista_riesgo = []
    for alumno, lista_asistencias in asistencias.items():
        if esta_en_riesgo(lista_asistencias):
            lista_riesgo.append(alumno)
    return lista_riesgo

#alumnos_en_riesgo({"Ana": [1, 1, 1, 1], "Luis": [1, 0, 0, 1], "María": [1, 1, 1, 0]})


def promedio_asistencia_grupo(asistencias):
    if not asistencias:
        return 0.0
    
    total_porcentajes = 0
    for lista_asistencias in asistencias.values():
        total_porcentajes += porcentaje_asistencia(lista_asistencias)
        
    return total_porcentajes / len(asistencias)

#promedio_asistencia_grupo({"Ana": [1, 1, 1, 1], "Luis": [1, 0, 0, 1]})
