def contar_calificaciones(calificaciones):
    return len(calificaciones)


def sumar_calificaciones(calificaciones):
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
    return len([c for c in calificaciones if c >= 70])


def contar_reprobados(calificaciones):
    return len([c for c in calificaciones if c < 70])


def clasificar_calificacion(calificacion):
    if calificacion >= 90:
        return "Excelente"
    elif calificacion >= 80:
        return "Bueno"
    elif calificacion >= 70:
        return "Regular"
    else:
        return "Reprobado"


def promedio(calificaciones):
    if not calificaciones:
        return None
    return sum(calificaciones) / len(calificaciones)


def porcentaje_aprobados(calificaciones):
    if not calificaciones:
        return 0.0
    aprobados = [c for c in calificaciones if c >= 70]
    return (len(aprobados) / len(calificaciones)) * 100


def porcentaje_reprobados(calificaciones):
    if not calificaciones:
        return 0.0
    reprobados = [c for c in calificaciones if c < 70]
    return (len(reprobados) / len(calificaciones)) * 100


def frecuencia_calificaciones(calificaciones):
    frecuencia = {}
    for c in calificaciones:
        frecuencia[c] = frecuencia.get(c, 0) + 1
    return frecuencia


def moda(calificaciones):
    if not calificaciones:
        return None
    frecuencia = frecuencia_calificaciones(calificaciones)
    return max(frecuencia, key=frecuencia.get)


def mediana(calificaciones):
    if not calificaciones:
        return None
    ordenadas = sorted(calificaciones)
    n = len(ordenadas)
    medio = n // 2
    if n % 2 == 1:
        return ordenadas[medio]
    return (ordenadas[medio - 1] + ordenadas[medio]) / 2


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
        "total": len(calificaciones),
        "promedio": promedio(calificaciones),
        "moda": moda(calificaciones),
        "mediana": mediana(calificaciones),
        "maxima": max(calificaciones),
        "minima": min(calificaciones),
        "porcentaje_aprobados": porcentaje_aprobados(calificaciones),
        "porcentaje_reprobados": porcentaje_reprobados(calificaciones),
        "distribucion": frecuencia_calificaciones(calificaciones)
    }