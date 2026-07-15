"""
Módulo de encuestas.

Implementa funciones para analizar respuestas usando listas y diccionarios.
"""


def contar_respuestas(respuestas):
       contador = 0
    for respuesta in respuestas:
        contador += 1
        
    return contador


if __name__ == "__main__":
   
    entrada_1 = ["Python", "Java", "Python"]
    resultado_1 = contar_respuestas(entrada_1)
    print(f"Entrada: {entrada_1}")
    print(f"Salida: {resultado_1}")  
    
    print("-" * 20)


def obtener_opciones(respuestas):
       resultado = []

    for r in respuestas:
        if r not in resultado:
            resultado.append(r)

    return resultado


def frecuencia_respuestas(respuestas):
     frecuencias = {}

    for r in respuestas:
        if r in frecuencias:
            frecuencias[r] += 1
        else:
            frecuencias[r] = 1

    return frecuencias


def respuesta_mas_comun(respuestas):
     if len(respuestas) == 0:
        return None

    frecuencias = {}

    for r in respuestas:
        if r in frecuencias:
            frecuencias[r] += 1
        else:
            frecuencias[r] = 1

    max_respuesta = None
    max_cantidad = 0

    for clave, valor in frecuencias.items():
        if valor > max_cantidad:
            max_cantidad = valor
            max_respuesta = clave

    return max_respuesta


def porcentaje_respuesta(respuestas, opcion):
     if len(respuestas) == 0:
        return 0.0

    total = len(respuestas)
    contador = 0

    for r in respuestas:
        if r == opcion:
            contador += 1

    return (contador / total) * 100


def resumen_encuesta(respuestas):
     if len(respuestas) == 0:
        return {
            "total": 0,
            "opciones": [],
            "frecuencias": {},
            "mas_comun": None
        }

    total = len(respuestas)

    opciones = []
    for r in respuestas:
        if r not in opciones:
            opciones.append(r)

    frecuencias = {}
    for r in respuestas:
        if r in frecuencias:
            frecuencias[r] += 1
        else:
            frecuencias[r] = 1

    mas_comun = None
    max_count = 0

    for clave, valor in frecuencias.items():
        if valor > max_count:
            max_count = valor
            mas_comun = clave

    return {
        "total": total,
        "opciones": opciones,
        "frecuencias": frecuencias,
        "mas_comun": mas_comun
    }
