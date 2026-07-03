"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
    pass


def sumar_calificaciones(calificaciones):
    pass


def calificacion_maxima(calificaciones):
    pass


def calificacion_minima(calificaciones):
    pass


def contar_aprobados(calificaciones):
    pass


def contar_reprobados(calificaciones):
    pass


def clasificar_calificacion(calificacion):
    pass


def promedio(calificaciones):
    if not calificaciones:
        return None
    return sum(calificaciones) / len(calificaciones)


def porcentaje_aprobados(calificaciones):
    if not calificaciones:
        return 0.0
    aprobados = 0
    for nota in calificaciones:
        if nota >= 70:
            aprobados += 1
    return (aprobados / len(calificaciones)) * 100


def porcentaje_reprobados(calificaciones):
    if not calificaciones:
        return 0.0
    
    reprobados = 0
    for nota in calificaciones:
        if nota < 70:
            reprobados += 1
            
    return (reprobados / len(calificaciones)) * 100


def frecuencia_calificaciones(calificaciones):
    if not calificaciones:
        return {}
    
    frecuencias = {}
    for nota in calificaciones:
        if nota in frecuencias:
            frecuencias[nota] += 1
        else:
            frecuencias[nota] = 1 
            
    return frecuencias


def moda(calificaciones):
    if not calificaciones:
        return None
    
    frecuencias = {}
    for nota in calificaciones:
        frecuencias[nota] = frecuencias.get(nota, 0) + 1
        
    moda = max(frecuencias, key=frecuencias.get)
    
    return moda


def mediana(calificaciones):
    if not calificaciones:
        return None
    
    ordenadas = sorted(calificaciones)
    n = len(ordenadas)
    centro = n // 2
    
    if n % 2 != 0:
        return float(ordenadas[centro])
    
    else:
        return (ordenadas[centro - 1] + ordenadas[centro]) / 2.0


def resumen_calificaciones(calificaciones):
    pass
