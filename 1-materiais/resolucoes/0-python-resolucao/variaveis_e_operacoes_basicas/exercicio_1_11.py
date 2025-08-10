# aluguel_carro

def calcula_aluguel_carro():
    quantidade_km_percorridos = float(input("Informe a quantidade de KM percorridos: "))
    quantidade_dias_alugado = int(input("Informe a quantidade de dias alugados: "))
    valor_por_km = 0.15
    valor_por_dia = 60
    return (quantidade_km_percorridos * valor_por_km) + (quantidade_dias_alugado * valor_por_dia)