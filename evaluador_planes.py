def regla_avance_valido(pieza):
    return 100 <= pieza["avance_mm_min"] <= 800
def regla_longitud_maxima(pieza):
    return pieza["longitud_mm"] <= 500
def regla_nombre_presente(pieza):
  return pieza["nombre"].strip() != ""
def calcular_tiempo(longitud_mm, avance_mm_min):
        return longitud_mm / avance_mm_min

def regla_tiempo_correcto(pieza, tolerancia=0.0001):
    tiempo_esperado = calcular_tiempo(pieza["longitud_mm"], pieza["avance_mm_min"])
    diferencia = abs(pieza["tiempo_min"] - tiempo_esperado)
    return diferencia <= tolerancia
    
    # TU CÓDIGO: calcula la diferencia entre pieza["tiempo_min"] y tiempo_esperado,
    
    # y devuelve True si la diferencia es menor o igual a 0.0001

pieza_buena = {"nombre": "eje A", "longitud_mm": 120, "avance_mm_min": 400, "tiempo_min": 0.3}
pieza_avanze_fiuera_de_rango = {"nombre": "eje B", "longitud_mm": 85, "avance_mm_min": 900, "tiempo_min": 0.0944}
pieza_longitud_excedida = {"nombre": "eje C", "longitud_mm": 600, "avance_mm_min": 400, "tiempo_min": 1.5}
pieza_sin_nombre = {"nombre": "     ", "longitud_mm": 120, "avance_mm_min": 400, "tiempo_min": 0.3}

lista = [pieza_buena, pieza_avanze_fiuera_de_rango, pieza_longitud_excedida, pieza_sin_nombre]

def evaluar_pieza(pieza):
    resultados = {
        "avance": regla_avance_valido(pieza),
        "longitud": regla_longitud_maxima(pieza),
        "nombre": regla_nombre_presente(pieza),
        "tiempo": regla_tiempo_correcto(pieza),
    }
    cumplidas = sum(resultados.values())
    return resultados, cumplidas
for pieza in lista:
    resultados, cumplidas = evaluar_pieza(pieza)
    print(f"{pieza['nombre']}: {cumplidas} de 3 reglas cumplidas")


print(regla_avance_valido(pieza_buena), regla_longitud_maxima(pieza_buena), regla_nombre_presente(pieza_buena))
print(regla_avance_valido(pieza_avanze_fiuera_de_rango), regla_longitud_maxima(pieza_avanze_fiuera_de_rango), regla_nombre_presente(pieza_avanze_fiuera_de_rango))
print(regla_avance_valido(pieza_longitud_excedida), regla_longitud_maxima(pieza_longitud_excedida), regla_nombre_presente(pieza_longitud_excedida))
print(regla_avance_valido(pieza_sin_nombre), regla_longitud_maxima(pieza_sin_nombre), regla_nombre_presente(pieza_sin_nombre))

total_cumplidas = 0
total_reglas = 0

with open("reporte_evaluacion.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Reporte de evaluación de plan\n")

    for pieza in lista:
        resultados, cumplidas = evaluar_pieza(pieza)
        total_cumplidas += cumplidas
        total_reglas += len(resultados)
        archivo.write(f"{pieza['nombre']}: {cumplidas} de {len(resultados)} reglas cumplidas\n")


    calificacion_general = (total_cumplidas / total_reglas) * 100 if total_reglas > 0 else 0
    
    porcentaje = round(calificacion_general, 2)
    archivo.write(f"Calificación general: {porcentaje}%\n")
