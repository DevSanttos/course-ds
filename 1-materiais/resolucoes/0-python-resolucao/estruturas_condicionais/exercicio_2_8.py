# energia_eletrica

def calcula_valor_energia_eletrica():
    quantidade_kwh = float(input("Informe a quantidade de KWh consumida: "))
    tipo_instalacao = input("Informe o tipo de instalação (R para Residencial, I para Industrial, C para Comercial): ").strip().upper()

    if tipo_instalacao == "R":
        if quantidade_kwh > 500:
            return quantidade_kwh * 0.65
        else:
            return quantidade_kwh * 0.4

    if tipo_instalacao == "C":
        if quantidade_kwh > 1000:
            return quantidade_kwh * 0.60
        else:
            return quantidade_kwh * 0.55

    if tipo_instalacao == "I":
        if quantidade_kwh > 5000:
            return quantidade_kwh * 0.68
        else:
            return quantidade_kwh * 0.57

    return "Tipo de instalação inválido. Use R, I ou C."