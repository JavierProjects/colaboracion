def contar_respuestas(respuestas):
    total = 0

    for respuesta in respuestas:
        total = total + 1

    return total

def obtener_opciones(respuestas):
    opciones = []

    for respuesta in respuestas:
        if respuesta not in opciones:
            opciones.append(respuesta)

    return opciones
    
def frecuencia_respuestas(respuestas):
    frecuencias = {}

    for respuesta in respuestas:
        if respuesta in frecuencias:
            frecuencias[respuesta] = frecuencias[respuesta] + 1
        else:
            frecuencias[respuesta] = 1

    return frecuencias

def respuesta_mas_comun(respuestas):
    if respuestas == []:
        return None

    frecuencias = frecuencia_respuestas(respuestas)

    mas_comun = None
    mayor = 0

    for respuesta in frecuencias:
        if frecuencias[respuesta] > mayor:
            mayor = frecuencias[respuesta]
            mas_comun = respuesta

    return mas_comun

def porcentaje_respuesta(respuestas, opcion):
    total = contar_respuestas(respuestas)

    if total == 0:
        return 0.0

    cantidad = 0

    for respuesta in respuestas:
        if respuesta == opcion:
            cantidad = cantidad + 1

    porcentaje = (cantidad / total) * 100

    return porcentaje



