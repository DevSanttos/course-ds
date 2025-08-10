# triangulo_lados

def verifica_validade_triangulo(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return "Os lados informados não formam um triângulo."
    else:
        return "Os lados informados formam um triângulo."