
def contar_calificaciones(calificaciones):
    """Cuenta cuántas calificaciones hay en una lista."""
    return len(calificaciones)


def sumar_calificaciones(calificaciones):
    """Suma todas las calificaciones de una lista."""
    return sum(calificaciones)


def calificacion_maxima(calificaciones):
    """Regresa la calificación más alta. Si está vacía, regresa None."""
    if not calificaciones:
        return None
    return max(calificaciones)


def calificacion_minima(calificaciones):
    """Regresa la calificación más baja. Si está vacía, regresa None."""
    if not calificaciones:
        return None
    return min(calificaciones)


def contar_aprobados(calificaciones):
    """Cuenta cuántas calificaciones son mayores o iguales a 70."""
    return sum(1 for c in calificaciones if c >= 70)


def contar_reprobados(calificaciones):
    """Cuenta cuántas calificaciones son menores a 70."""
    return sum(1 for c in calificaciones if c < 70)


def clasificar_calificacion(calificacion):
    """Clasifica una calificación individual según su rango."""
    if calificacion >= 90:
        return "Excelente"
    elif calificacion >= 80:
        return "Bueno"
    elif calificacion >= 70:
        return "Regular"
    else:
        return "Reprobado"


def promedio(calificaciones):
    """Regresa el promedio de las calificaciones. Si está vacía, regresa 0.0."""
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def porcentaje_aprobados(calificaciones):
    """Regresa el porcentaje de aprobados (0 a 100). Si está vacía, regresa 0.0."""
    if not calificaciones:
        return 0.0
    aprobados = contar_aprobados(calificaciones)
    return (aprobados / len(calificaciones)) * 100


def porcentaje_reprobados(calificaciones):
    """Regresa el porcentaje de reprobados (0 a 100). Si está vacía, regresa 0.0."""
    if not calificaciones:
        return 0.0
    reprobados = contar_reprobados(calificaciones)
    return (reprobados / len(calificaciones)) * 100


def frecuencia_calificaciones(calificaciones):
    """Regresa un diccionario con las veces que se repite cada calificación."""
    frecuencias = {}
    for c in calificaciones:
        if c in frecuencias:
            frecuencias[c] += 1
        else:
            frecuencias[c] = 1
    return frecuencias


def moda(calificaciones):
    """Regresa la calificación que más se repite (o una lista de ellas si hay empate). Si está vacía, None."""
    if not calificaciones:
        return None
    
    frecuencias = frecuencia_calificaciones(calificaciones)
    max_frecuencia = max(frecuencias.values())
    
    modas = [calif for calif, frec in frecuencias.items() if frec == max_frecuencia]
    
  
    return modas


def mediana(calificaciones):
    """Regresa la mediana de las calificaciones. Si está vacía, regresa None."""
    if not calificaciones:
        return None
    
    # Ordenamos la lista de menor a mayor sin modificar la original
    ordenadas = sorted(calificaciones)
    n = len(ordenadas)
    mitad = n // 2
    
    # Si es impar, es el elemento del centro
    if n % 2 != 0:
        return float(ordenadas[mitad])
    # Si es par, es el promedio de los dos elementos del centro
    else:
        return (ordenadas[mitad - 1] + ordenadas[mitad]) / 2.0


def resumen_calificaciones(calificaciones):
    """Regresa un diccionario con estadísticas generales de las calificaciones."""
    return {
        "total": contar_calificaciones(calificaciones),
        "promedio": promedio(calificaciones),
        "maxima": calificacion_maxima(calificaciones),
        "minima": calificacion_minima(calificaciones),
        "aprobados": contar_aprobados(calificaciones),
        "reprobados": contar_reprobados(calificaciones)
    }