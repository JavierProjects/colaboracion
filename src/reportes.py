"""
Módulo de reportes.

Aquí se integran resultados de calificaciones, asistencias y encuestas.
"""
from src.calificaciones import promedio, porcentaje_aprobados
from src.asistencias import promedio_asistencia_grupo
from src.encuestas import respuesta_mas_comun
 
 
def reporte_general(calificaciones, asistencias, respuestas):
    return {
        "promedio_calificaciones": promedio(calificaciones),
        "porcentaje_aprobados": porcentaje_aprobados(calificaciones),
        "promedio_asistencia": promedio_asistencia_grupo(asistencias),
        "respuesta_mas_comun": respuesta_mas_comun(respuestas),
    }

    
    pass
