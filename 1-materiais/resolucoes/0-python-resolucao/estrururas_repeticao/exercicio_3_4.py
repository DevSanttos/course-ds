# juros

def realiza_calculo_juros(valor_deposito, porcentagem_taxa_de_juros):
    # 24 meses
    armazenaValor = valor_deposito
    for i in range(2):
        armazenaValor *= float(1 + (porcentagem_taxa_de_juros / 100))

    return print(f"Valor: {armazenaValor:.2f}")