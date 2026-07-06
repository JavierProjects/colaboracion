


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
    pass


def porcentaje_aprobados(calificaciones):
     if not calificaciones:
        return 0.0
    
    aprobados = [c for c in calificaciones if c >= 70]
    
    return (len(aprobados) / len(calificaciones)) * 100

   
    pass


def porcentaje_reprobados(calificaciones):
     if not calificaciones:
        return 0.0
   
    reprobados = [c for c in calificaciones if c < 70]
    
    porcentaje = (len(reprobados) / len(calificaciones)) * 100
    return float(porcentaje)

    
    pass


def frecuencia_calificaciones(calificaciones):
      frecuencias = {}
    
    for nota in calificaciones:
        if nota in frecuencias:
            frecuencias[nota] += 1
        else:
            frecuencias[nota] = 1
            
    return frecuencias

   
 
    pass


def moda(calificaciones):
    if not calificaciones:
        return None
    
    frecuencias = {}
    for nota in calificaciones:
        frecuencias[nota] = frecuencias.get(nota, 0) + 1
    
    return max(frecuencias, key=frecuencias.get)

   
    pass


def mediana(calificaciones):
     if not calificaciones:
        return None
  
    lista_ordenada = sorted(calificaciones)
    n = len(lista_ordenada)
    medio = n // 2
    
    if n % 2 != 0:
        return lista_ordenada[medio]
   
    else:
        return (lista_ordenada[medio - 1] + lista_ordenada[medio]) / 2

    
    pass


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
    promedio = sum(calificaciones) / total

    porc_reprobados = porcentaje_reprobados(calificaciones)
    porc_aprobados = 100.0 - porc_reprobados
    
    return {
        "total": total,
        "promedio": float(promedio),
        "moda": moda(calificaciones),
        "mediana": float(mediana(calificaciones)),
        "maxima": max(calificaciones),
        "minima": min(calificaciones),
        "porcentaje_aprobados": float(porc_aprobados),
        "porcentaje_reprobados": float(porc_reprobados),
        "distribucion": frecuencia_calificaciones(calificaciones)
    }

  

    pass
