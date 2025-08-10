# maior_menor

def maior_menor():
    lista_numeros = []

    for i in range(3):
        numero = float(input(f"Digite o {i + 1}º número: "))
        lista_numeros.append(numero)

    maior_numero = max(lista_numeros)
    menor_numero = min(lista_numeros)

    return (f"O maior número é: {maior_numero}\n"
            f"O menor número é: {menor_numero}")