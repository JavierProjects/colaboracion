"""
Módulo de asistencias.

Representación:
1 = asistió
0 = faltó
"""


def contar_clases(asistencias_alumno):
<<<<<<< Updated upstream
    pass


def contar_asistencias(asistencias_alumno):
    pass


=======


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
>>>>>>> Stashed changes
def contar_faltas(asistencias_alumno):
    contador=0
    for asistencia in asistencias_alumno:
        if asistencia == 0:
            contador+= 1
    return contador
    ##pass


def porcentaje_asistencia(asistencias_alumno):
    contador=0
    for asistencia in asistencias_alumno:
        if asistencia == 1:
            contador+= 1
    asistencia=(100/contar_clases(a))*contador
    return asistencia
    ##pass


def esta_en_riesgo(asistencias_alumno):
    contador=0
    for asistencia in asistencias_alumno:
        if asistencia == 1:
            contador+= 1
    asistencia=(100/contar_clases(a))*contador
    if asistencia >= 80:
        return False
    elif asistencia<80:
        return True

a=[1, 1, 0, 1] 
b=[1, 1, 1, 1] 
    

def alumnos_en_riesgo(asistencias):
    alumnos_riesgo = []
    
    for alumno, lista_asistencias in asistencias.items():
        if not lista_asistencias:
            porcentaje = 0
        else:
            total_asistencias = lista_asistencias.count(1)
            porcentaje = (total_asistencias / len(lista_asistencias)) * 100
        
        if porcentaje < 80:
            alumnos_riesgo.append(alumno)
            
    resultado_final = alumnos_riesgo
    return resultado_final


def promedio_asistencia_grupo(asistencias):
    if not asistencias:
        resultado_final = 0.0
        return resultado_final
        
    suma_porcentajes = 0
    
    for lista_asistencias in asistencias.values():
        if not lista_asistencias:
            porcentaje = 0.0
        else:
            porcentaje = (lista_asistencias.count(1) / len(lista_asistencias)) * 100
        suma_porcentajes += porcentaje
        
    resultado_final = suma_porcentajes / len(asistencias)
    return resultado_final
