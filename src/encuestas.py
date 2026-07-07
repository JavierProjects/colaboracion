def contar_respuestas(respuestas):
    """Cuenta cuántas respuestas hay en una lista."""
    return len(respuestas)


def obtener_opciones(respuestas):
    """Regresa una lista con las opciones únicas conservando el orden de aparición."""
    opciones_unicas = []
    for respuesta in respuestas:
        if respuesta not in opciones_unicas:
            opciones_unicas.append(respuesta)
    return opciones_unicas


def frecuencia_respuestas(respuestas):
    """Regresa un diccionario con la frecuencia absoluta de las respuestas."""
    frecuencias = {}
    for respuesta in respuestas:
        if respuesta in frecuencias:
            frecuencias[respuesta] += 1
        else:
            frecuencias[respuesta] = 1
    return frecuencias


def respuesta_mas_comun(respuestas):
    """Regresa la respuesta que más se repite. Si está vacía, regresa None."""
    if not respuestas:
        return None
    
    frecuencias = frecuencia_respuestas(respuestas)
    # Buscamos la clave con el valor máximo
    return max(frecuencias, key=frecuencias.get)


def porcentaje_respuesta(respuestas, opcion):
    """Calcula el porcentaje (0 a 100) que representa una opción específica."""
    total = contar_respuestas(respuestas)
    if total == 0:
        return 0.0
    
    # Contamos cuántas veces aparece la opción específica
    veces = respuestas.count(opcion)
    return (veces / total) * 100


def resumen_encuesta(respuestas):
    """Regresa un diccionario con el resumen completo de la encuesta."""
    return {
        "total": contar_respuestas(respuestas),
        "opciones": obtener_opciones(respuestas),
        "frecuencias": frecuencia_respuestas(respuestas),
        "mas_comun": respuesta_mas_comun(respuestas)
    }