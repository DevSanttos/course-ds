#preco_viagem

def calcula_preco_viagem():
    distancia = float(input("Informe a distância a percorrer: "))

    if distancia <= 200:
        return f"O valor a ser pago é de: {round(distancia) * 0.50}"
    else:
        return f"O valor a ser pago é de: {round(distancia) * 0.45}"