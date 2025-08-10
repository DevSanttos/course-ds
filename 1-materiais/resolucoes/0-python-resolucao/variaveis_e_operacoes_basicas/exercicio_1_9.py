# tempo_viagem

def calcula_tempo_viagem():
    distancia = float(input("Informe a distância a percorrer: "))
    velocidade_media = float(input("Informe a velocidade média do veículo: "))
    return f"O tempo de viagem é: {distancia / velocidade_media}"