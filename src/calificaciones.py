def contar_calificaciones(calificaciones):
    conteo = 0
    for nota in calificaciones:
        conteo = conteo + 1
    return conteo


def sumar_calificaciones(calificaciones):
    suma_total = 0
    for nota in calificaciones:
        suma_total = suma_total + nota

    return suma_total


def calificacion_maxima(calificaciones):
    if len(calificaciones) == 0:
        return None

    maxima = calificaciones[0]
    for nota in calificaciones:
        if nota > maxima:
            maxima = nota

    return maxima


def calificacion_minima(calificaciones):

    if len(calificaciones) == 0:
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
           
            aprobados = aprobados + 1
            
    return aprobados


def contar_reprobados(calificaciones):
    reprobados = 0
    for nota in calificaciones:
        if nota < 70:
            reprobados = reprobados + 1
    return reprobados



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
    
    total = len(calificaciones)
    
    maxima = max(calificaciones)
    minima = min(calificaciones)
    
    promedio = sum(calificaciones) / total
    
    distribucion = {}
    for nota in calificaciones:
        distribucion[nota] = distribucion.get(nota, 0) + 1
        
    moda = max(distribucion, key=distribucion.get)
    
    notas_ordenadas = sorted(calificaciones)
    indice_mitad = total // 2
    if total % 2 != 0:
        mediana = float(notas_ordenadas[indice_mitad])
    else:
        mediana = (notas_ordenadas[indice_mitad - 1] + notas_ordenadas[indice_mitad]) / 2.0
        
    aprobados = sum(1 for nota in calificaciones if nota >= 70)
    reprobados = total - aprobados
    
    porcentaje_aprobados = (aprobados / total) * 100
    porcentaje_reprobados = (reprobados / total) * 100
    
    return {
        "total": total,
        "promedio": promedio,
        "moda": moda,
        "mediana": mediana,
        "maxima": maxima,
        "minima": minima,
        "porcentaje_aprobados": porcentaje_aprobados,
        "porcentaje_reprobados": porcentaje_reprobados,
        "distribucion": distribucion
    }
    return resultado
