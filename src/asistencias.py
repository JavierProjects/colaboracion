"""
Módulo de encuestas.
"""

def promedio_encuestas(respuestas):
    if not respuestas: return 0.0
    return float(sum(respuestas) / len(respuestas))

def contar_respuestas(respuestas):
    return len(respuestas)

def obtener_opciones(respuestas):
    return list(set(respuestas))

def frecuencia_respuestas(respuestas):
    frecuencias = {}
    for r in respuestas:
        frecuencias[r] = frecuencias.get(r, 0) + 1
    return frecuencias

def respuesta_mas_frecuente(respuestas):
    if not respuestas: return None
    frecuencias = frecuencia_respuestas(respuestas)
    return max(frecuencias, key=frecuencias.get)

def porcentaje_respuesta(respuestas, opcion):
    if not respuestas: return 0.0
    conteo = respuestas.count(opcion)
    return (conteo / len(respuestas)) * 100.0