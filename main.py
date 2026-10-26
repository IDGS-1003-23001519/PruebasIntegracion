def procesar_datos(valor):
    if valor < 0:
        raise ValueError("El valor no puede ser negativo")
    return f"Procesamiento exitoso: {valor * 2}"