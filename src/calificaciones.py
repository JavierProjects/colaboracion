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
