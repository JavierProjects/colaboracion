"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
    if not calificaciones:
        return 0
    return len(calificaciones)


def sumar_calificaciones(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones)


def calificacion_maxima(calificaciones):
    if not calificaciones:
        return None
    return max(calificaciones)


def calificacion_minima(calificaciones):
    if not calificaciones:
        return None
    return min(calificaciones)


def contar_aprobados(calificaciones):
    if not calificaciones:
        return 0
    aprobados = 0
    for c in calificaciones:
        if c >= 70:
            aprobados += 1
    return aprobados


def contar_reprobados(calificaciones):
    if not calificaciones:
        return 0
    reprobados = 0
    for c in calificaciones:
        if c < 70:
            reprobados += 1
    return reprobados


def clasificar_calificacion(calificacion):
    if calificacion >= 90:
        return "Excelente"
    elif calificacion >= 80:
        return "Muy Bien"
    elif calificacion >= 70:
        return "Bien"
    else:
        return "Reprobado"


def promedio(calificaciones):
    if not calificaciones:
        return None
    return float(sum(calificaciones) / len(calificaciones))


def porcentaje_aprobados(calificaciones):
    if not calificaciones:
        return 0.0
    aprobados = contar_aprobados(calificaciones)
    return float((aprobados / len(calificaciones)) * 100)


def porcentaje_reprobados(calificaciones):
    if not calificaciones:
        return 0.0
    reprobados = contar_reprobados(calificaciones)
    return float((reprobados / len(calificaciones)) * 100)


def frecuencia_calificaciones(calificaciones):
    if not calificaciones:
        return {}
    frecuencias = {}
    for c in calificaciones:
        c_int = int(c)
        if c_int in frecuencias:
            frecuencias[c_int] += 1
        else:
            frecuencias[c_int] = 1
    return frecuencias


def moda(calificaciones):
    if not calificaciones:
        return None
    
    frecuencias = frecuencia_calificaciones(calificaciones)
    max_frecuencia = -1
    moda_valor = None
    
    for calif, freq in frecuencias.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            moda_valor = calif
            
    return int(moda_valor) if moda_valor is not None else None


def mediana(calificaciones):
    if not calificaciones:
        return None
    
    lista_ordenada = sorted(calificaciones)
    n = len(lista_ordenada)
    mitad = n // 2
    
    if n % 2 != 0:
        return float(lista_ordenada[mitad])
    else:
        return float((lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2.0)


def resumen_calificaciones(calificaciones):
    if not calificaciones:
        return {
            "total": 0,
            "promedio": None,
            "moda": None,
            "mediana": None,
            "maxima": None,
            "minima": None,
            "porcentaje_aprobados": 0.0,
            "porcentaje_reprobados": 0.0,
            "distribucion": {}
        }
        
    return {
        "total": int(contar_calificaciones(calificaciones)),
        "promedio": promedio(calificaciones),
        "moda": moda(calificaciones),
        "mediana": mediana(calificaciones),
        "maxima": int(calificacion_maxima(calificaciones)),
        "minima": int(calificacion_minima(calificaciones)),
        "porcentaje_aprobados": porcentaje_aprobados(calificaciones),
        "porcentaje_reprobados": porcentaje_reprobados(calificaciones),
        "distribucion": frecuencia_calificaciones(calificaciones)
    }