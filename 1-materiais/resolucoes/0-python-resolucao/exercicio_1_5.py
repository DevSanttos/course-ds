# media_altura

def media_altura():
    altura = []
    for i in range(4):
        altura.append(float(input("Digite a sua altura: ")))

    return f"A média da altura do respectivo grupo é: {(sum(altura) / 4):.2f}"