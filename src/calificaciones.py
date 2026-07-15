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
    return sum(calificaciones)/ len(calificaciones)


def porcentaje_aprobados(calificaciones):
    if not calificaciones:
        return 0.0
    aprobados =  0
    for calificacion in calificaciones:
        if calificacion >= 70:
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
    if len(calificaciones) == 0:
        return None
    
    elemento_mas_repetido = calificaciones[0]
    maximo_repeticiones = 0

    for calificacion_actual in calificaciones:
        veces_que_aparece = 0

        for otra_calificacion in calificaciones:
            if calificacion_actual == otra_calificacion:
                veces_que_aparece = veces_que_aparece + 1

        if veces_que_aparece > maximo_repeticiones:
            maximo_repeticiones = veces_que_aparece
            elemento_mas_repetido = calificacion_actual
    
    return elemento_mas_repetido


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
        
        moda = None
        max_frecuencia = 0

        for nota in distribucion:
            frecuencia = distribucion[nota]
            if frecuencia > max_frecuencia or (frecuencia == max_frecuencia and (moda is None or nota > moda)):
                max_frecuencia = frecuencia
                moda = nota

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