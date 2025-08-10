# multa

def verifica_multa():
    velocidade = float(input("Informe a velocidade do carro: "))

    if velocidade > 80:
        return f"Você foi multado! Valor da multa: {(round(velocidade) - 80) * 30} reais."
    else:
        return "Tudo certo! Você não foi multado."

