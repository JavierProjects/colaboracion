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
     if len(calificaciones) == 0:
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
     total_elementos = len(calificaciones)
     maxima_nota = calificaciones[0]
     minima_nota = calificaciones[0]
     suma_total = 0
     aprobados = 0
     for nota in calificaciones:
        suma_total = suma_total + nota
        
        if nota > maxima_nota:
            maxima_nota = nota
            
        if nota < minima_nota:
            minima_nota = nota
            
        if nota >= 70:
            aprobados = aprobados + 1
     promedio_notas = suma_total / total_elementos
     porcentaje_ap = (aprobados / total_elementos) * 100
     porcentaje_rep = 100.0 - porcentaje_ap
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
     lista_ordenada = list(calificaciones)
     for i in range(len(lista_ordenada)):
        for j in range(0, len(lista_ordenada) - i - 1):
            if lista_ordenada[j] > lista_ordenada[j+1]:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
     mitad = len(lista_ordenada) // 2
     if len(lista_ordenada) % 2 == 0:
        mediana_nota = (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2.0
     else:
        mediana_nota = float(lista_ordenada[mitad])
        
     diccionario_distribucion = {}
     for nota in calificaciones:
        if nota not in diccionario_distribucion:
            cuenta = 0
            for c in calificaciones:
                if c == nota:
                    cuenta = cuenta + 1
            diccionario_distribucion[nota] = cuenta
     return {
        "total": total_elementos,
        "promedio": promedio_notas,
        "moda": elemento_mas_repetido,
        "mediana": mediana_nota,
        "maxima": maxima_nota,
        "minima": minima_nota,
        "porcentaje_aprobados": porcentaje_ap,
        "porcentaje_reprobados": porcentaje_rep,
        "distribucion": diccionario_distribucion
    }