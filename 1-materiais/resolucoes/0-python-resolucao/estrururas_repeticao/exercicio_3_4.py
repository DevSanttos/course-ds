# juros

def realiza_calculo_juros(valor_deposito, taxa_de_juros):
    # 24 meses
    for i in range(24):
        resultado_rendimento += valor_deposito * (taxa_de_juros / 100)

    return 