"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
    contador = 0
    for contar in calificaciones:
        contador += 1
    return contador


def sumar_calificaciones(calificaciones):
    total = 0
    for calificacion in calificaciones:
        total += calificacion
    return total


def calificacion_maxima(calificaciones):
    if not calificaciones: return None
    
    maxima = calificaciones[0]
    for calificacion in calificaciones:
        if calificacion > maxima:
            maxima = calificacion
    return maxima


def calificacion_minima(calificaciones):
    if not calificaciones: return None
    
    minima = calificaciones[0]
    for calificacion in calificaciones:
        if calificacion < minima:
            minima = calificacion
    return minima


def contar_aprobados(calificaciones):
    aprobados = 0
    for calificacion in calificaciones:
        if calificacion >= 70:
            aprobados += 1
    return aprobados


def contar_reprobados(calificaciones):
    reprobados = 0
    for calificacion in calificaciones:
        if calificacion < 70:
            reprobados += 1
    return reprobados


def clasificar_calificacion(calificacion):
    if calificacion >= 90: return "Excelente"
    if calificacion >= 80: return "Bueno"
    if calificacion >= 70: return "Regular"
    return "Reprobado"


def promedio(calificaciones):
    if not calificaciones: return None
    return sumar_calificaciones(calificaciones) / len(calificaciones) 


def porcentaje_aprobados(calificaciones):
    if not calificaciones: return 0.0
    return (contar_aprobados(calificaciones) / len(calificaciones)) * 100


def porcentaje_reprobados(calificaciones):
    if not calificaciones: return 0.0
    return (contar_reprobados(calificaciones) / len(calificaciones)) * 100


def frecuencia_calificaciones(calificaciones):
    frecuencias = {}
    for calificacion in calificaciones:
        if calificacion in frecuencias:
            frecuencias[calificacion] += 1
        else:
            frecuencias[calificacion] = 1
    return frecuencias


def moda(calificaciones):
    if not calificaciones:
        return None
    frecuencias = frecuencia_calificaciones(calificaciones)
    
    maxfrecuencia = 0
    moda = calificaciones[0]
    
    for calificacion, frequencia in frecuencias.items():
        if frequencia > maxfrecuencia:
            maxfrecuencia = frequencia
            moda = calificacion
            
    return moda

def mediana(calificaciones):
    if not calificaciones:
        return None
    lista = list(calificaciones)
    n = contar_calificaciones(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista [j+1]:
                lista[j], lista[j +1] = lista[j + 1], lista[j]
    if n % 2 != 0:
        return lista[n//2]
    else:
        mitad1 = lista[(n//2) - 1]


def resumen_calificaciones(calificaciones):
    return {
        "total": contar_calificaciones(calificaciones),
        "promedio": promedio(calificaciones),
        "maxima": calificacion_maxima(calificaciones),
        "minima": calificacion_minima(calificaciones),
        "aprobados": contar_aprobados(calificaciones),
        "reprobados": contar_reprobados(calificaciones),
        "porcentaje_aprobados": porcentaje_aprobados(calificaciones),
        "porcentaje_reprobados": porcentaje_reprobados(calificaciones),
        "moda": moda(calificaciones),
        "mediana": mediana(calificaciones),
        "distribucion": frecuencia_calificaciones(calificaciones) 
    }