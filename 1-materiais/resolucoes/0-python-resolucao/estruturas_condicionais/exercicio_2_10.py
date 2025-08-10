# triangulo_angulos

def verifica_validade_angulos_triangulo(lado_a, lado_b, lado_c):
    if lado_a < 90 and lado_b < 90 and lado_c < 90:
        return "Triângulo acutângulo"
    elif lado_a == 90 or lado_b == 90 or lado_c == 90:
        return "Triângulo retângulo"
    elif lado_a > 90 or lado_b > 90 or lado_c > 90:
        return "Triângulo obtusângulo"
    else:
        return "Não é um triângulo válido"