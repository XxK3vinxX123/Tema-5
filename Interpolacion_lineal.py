def interpolacion_lineal(x0, y0, x1, y1, x):
    """
    Interpolación lineal entre dos puntos (x0, y0) y (x1, y1).
    Retorna el valor interpolado de y para un valor dado de x.
    """
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))

# Ejemplo de uso
x0 = 0
y0 = 0
x1 = 10
y1 = 100

x = 5  # Valor de x para interpolar
y_interpolado = interpolacion_lineal(x0, y0, x1, y1, x)
print(f"Para x={x}, el valor interpolado de y es: {y_interpolado}")
