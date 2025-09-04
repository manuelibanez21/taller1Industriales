def calcular_hamming(bits):
    """
    Genera un código Hamming (7,4) a partir de 4 bits de datos.
    """
    d1, d2, d3, d4 = [int(x) for x in bits]
    p1 = (d1 + d2 + d4) % 2
    p2 = (d1 + d3 + d4) % 2
    p3 = (d2 + d3 + d4) % 2
    return f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"

def verificar_hamming(code):
    """
    Verifica y corrige un código Hamming (7,4).
    """
    c = [int(x) for x in code]
    p1 = (c[2] + c[4] + c[6]) % 2
    p2 = (c[2] + c[5] + c[6]) % 2
    p3 = (c[4] + c[5] + c[6]) % 2
    error = p1*1 + p2*2 + p3*4
    if error != 0:
        print(f"Error en la posición {error}, corrigiendo...")
        c[error-1] = 1 - c[error-1]
    return "".join(str(x) for x in c)

# Ejemplo de uso
data = "1011"
code = calcular_hamming(data)
print("Código Hamming:", code)
print("Verificación:", verificar_hamming(code))
