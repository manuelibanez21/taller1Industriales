def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else:  
            tmp = xor('0'*pick, tmp) + divident[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    return tmp

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    return data + remainder

# Ejemplo de uso
data = "1011001"
key = "1101"   # Polinomio generador
encoded = encodeData(data, key)
print("Datos enviados:", encoded)
