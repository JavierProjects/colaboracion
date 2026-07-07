"""
Módulo de calificaciones.

Implementa estas funciones usando Python puro: listas, ciclos,
condicionales, diccionarios y funciones.
"""


def contar_calificaciones(calificaciones):
<<<<<<< HEAD
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
=======
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
>>>>>>> 1628f27d932dbbc1765b43ecab1206c30f46134b
            aprobados += 1
    return aprobados


def contar_reprobados(calificaciones):
<<<<<<< HEAD
    if not calificaciones:
        return 0
    reprobados = 0
    for c in calificaciones:
        if c < 70:
=======
    reprobados = 0
    for calificacion in calificaciones:
        if calificacion < 70:
>>>>>>> 1628f27d932dbbc1765b43ecab1206c30f46134b
            reprobados += 1
    return reprobados


def clasificar_calificacion(calificacion):
<<<<<<< HEAD
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
=======
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
>>>>>>> 1628f27d932dbbc1765b43ecab1206c30f46134b
    return frecuencias


def moda(calificaciones):
    if not calificaciones:
        return None
<<<<<<< HEAD
    
    frecuencias = frecuencia_calificaciones(calificaciones)
    max_frecuencia = -1
    moda_valor = None
    
    for calif, freq in frecuencias.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            moda_valor = calif
            
    return int(moda_valor) if moda_valor is not None else None

=======
    frecuencias = frecuencia_calificaciones(calificaciones)
    
    maxfrecuencia = 0
    moda = calificaciones[0]
    
    for calificacion, frequencia in frecuencias.items():
        if frequencia > maxfrecuencia:
            maxfrecuencia = frequencia
            moda = calificacion
            
    return moda
>>>>>>> 1628f27d932dbbc1765b43ecab1206c30f46134b

def mediana(calificaciones):
    if not calificaciones:
        return None
<<<<<<< HEAD
    
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
=======
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
>>>>>>> 1628f27d932dbbc1765b43ecab1206c30f46134b
    }