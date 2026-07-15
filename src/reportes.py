"""
Módulo de reportes.

Aquí se integran resultados de calificaciones, asistencias y encuestas.
"""


def reporte_general(calificaciones, asistencias, respuestas):
    suma = 0

    for calificacion in calificaciones:
        suma = suma + calificacion

    promedio_calificaciones = suma / len(calificaciones)

    aprobados = 0
    for calificacion in calificaciones:
        if calificacion >= 70:
            aprobados = aprobados + 1

    porcentaje_aprobados = (aprobados / len(calificaciones)) * 100

    suma_porcentajes = 0

    for alumno in asistencias:
        asistencias_alumno = asistencias[alumno]

        asistencias_realizadas = 0
        for asistencia in asistencias_alumno:
            if asistencia == 1:
                asistencias_realizadas = asistencias_realizadas + 1

        porcentaje = (asistencias_realizadas / len(asistencias_alumno)) * 100
        suma_porcentajes = suma_porcentajes + porcentaje

    promedio_asistencia = suma_porcentajes / len(asistencias)

    conteo = {}

    for respuesta in respuestas:
        if respuesta in conteo:
            conteo[respuesta] = conteo[respuesta] + 1
        else:
            conteo[respuesta] = 1

    respuesta_mas_comun = ""
    mayor = 0

    for respuesta in conteo:
        if conteo[respuesta] > mayor:
            mayor = conteo[respuesta]
            respuesta_mas_comun = respuesta

    return {
        "promedio_calificaciones": promedio_calificaciones,
        "porcentaje_aprobados": porcentaje_aprobados,
        "promedio_asistencia": promedio_asistencia,
        "respuesta_mas_comun": respuesta_mas_comun
    }
