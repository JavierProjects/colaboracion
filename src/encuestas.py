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
