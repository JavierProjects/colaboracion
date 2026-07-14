def promedio_encuestas(respuestas):
    if not respuestas: return 0.0
    return float(sum(respuestas) / len(respuestas))

def frecuencia_respuestas(respuestas):
    frecuencias = {}
    for r in respuestas:
        frecuencias[r] = frecuencias.get(r, 0) + 1
    return frecuencias

def obtener_opciones(respuestas):
    return list(dict.fromkeys(respuestas))

def resumen_encuesta(respuestas):
    if not respuestas:
        # Se agregan "total" y "opciones" porque las pruebas los buscan
        return {"total": 0, "promedio_calificaciones": 0.0, "frecuencia": {}, "opciones": []}
    
    return {
        "total": len(respuestas),
        "promedio_calificaciones": promedio_encuestas(respuestas),
        "frecuencia": frecuencia_respuestas(respuestas),
        "opciones": obtener_opciones(respuestas)
    }