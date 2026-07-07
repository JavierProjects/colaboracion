"""Módulo de reportes.

Aquí se integran resultados de calificaciones, asistencias y encuestas.
"""

from src.calificaciones import promedio, porcentaje_aprobados
from src.encuestas import respuesta_mas_comun


def reporte_general(calificaciones, asistencias, respuestas):

    suma_porcentajes = 0

    for registros in asistencias.values():
        asistencias_presentes = 0

        for valor in registros:
            asistencias_presentes = asistencias_presentes + valor

        porcentaje_alumno = (
            asistencias_presentes / len(registros)
        ) * 100

        suma_porcentajes = suma_porcentajes + porcentaje_alumno

    if len(asistencias) == 0:
        promedio_asistencia = 0.0
    else:
        promedio_asistencia = suma_porcentajes / len(asistencias)

    reporte = {
        "promedio_calificaciones": promedio(calificaciones),
        "porcentaje_aprobados": porcentaje_aprobados(calificaciones),
        "promedio_asistencia": promedio_asistencia,
        "respuesta_mas_comun": respuesta_mas_comun(respuestas)
    }

    return reporte