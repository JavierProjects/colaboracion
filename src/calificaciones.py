"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""

def contar_calificaciones(calificaciones):
    total = 0
    for nota in calificaciones:
        total += 1
    return total


def sumar_calificaciones(calificaciones):
    suma = 0.0
    for nota in calificaciones:
        suma += nota
    return suma


def calificacion_maxima(calificaciones):
    if contar_calificaciones(calificaciones) == 0:
        return None
    maxima = calificaciones[0]
    for nota in calificaciones:
        if nota > maxima:
            maxima = nota
    return maxima


def calificacion_minima(calificaciones):
    if contar_calificaciones(calificaciones) == 0:
        return None
    minima = calificaciones[0]
    for nota in calificaciones:
        if nota < minima:
            minima = nota
    return minima


def contar_aprobados(calificaciones):
    aprobados = 0
    for nota in calificaciones:
        if nota >= 70:  
            aprobados += 1
    return aprobados


def contar_reprobados(calificaciones):
    reprobados = 0
    for nota in calificaciones:
        if nota < 70:
            reprobados += 1
    return reprobados


def clasificar_calificacion(calificacion):
    # Lógica corregida según las etiquetas exactas del test del profesor:
    if calificacion >= 90:
        return "Excelente"
    elif calificacion >= 80:
        return "Bueno"
    elif calificacion >= 70:
        return "Regular"
    else:
        return "Reprobado"


def promedio(calificaciones):
    total = contar_calificaciones(calificaciones)
    if total == 0:
        return 0.0
    return sumar_calificaciones(calificaciones) / total


def porcentaje_aprobados(calificaciones):
    total = contar_calificaciones(calificaciones)
    if total == 0:
        return 0.0
    return (contar_aprobados(calificaciones) / total) * 100


def porcentaje_reprobados(calificaciones):
    total = contar_calificaciones(calificaciones)
    if total == 0:
        return 0.0
    return (contar_reprobados(calificaciones) / total) * 100


def frecuencia_calificaciones(calificaciones):
    frecuencias = {}
    for nota in calificaciones:
        if nota in frecuencias:
            frecuencias[nota] += 1
        else:
            frecuencias[nota] = 1
    return frecuencias


def moda(calificaciones):
    if contar_calificaciones(calificaciones) == 0:
        return None
    frecuencias = frequency = frecuencia_calificaciones(calificaciones)
    max_frecuencia = 0
    valor_moda = calificaciones[0]
    for nota, conteo in frecuencias.items():
        if conteo > max_frecuencia:
            max_frecuencia = conteo
            valor_moda = nota
    return valor_moda


def mediana(calificaciones):
    total = contar_calificaciones(calificaciones)
    if total == 0:
        return None
    notas_ordenadas = list(calificaciones)
    for i in range(total):
        for j in range(0, total - i - 1):
            if notas_ordenadas[j] > notas_ordenadas[j + 1]:
                notas_ordenadas[j], notas_ordenadas[j + 1] = notas_ordenadas[j + 1], notas_ordenadas[j]
    mitad = total // 2
    if total % 2 != 0:
        return notas_ordenadas[mitad]
    else:
        return (notas_ordenadas[mitad - 1] + notas_ordenadas[mitad]) / 2.0


def resumen_calificaciones(calificaciones):
    resumen = {
        "total": contar_calificaciones(calificaciones),
        "promedio": promedio(calificaciones),
        "maxima": calificacion_maxima(calificaciones),
        "minima": calificacion_minima(calificaciones),
        "porcentaje_aprobados": porcentaje_aprobados(calificaciones),
        "porcentaje_reprobados": porcentaje_reprobados(calificaciones)
    }
    return resumen