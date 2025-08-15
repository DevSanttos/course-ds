# juros_deposito

def calcula_juros_deposito(valor_deposito_inicial, taxa_juros):
    taxa_juros_formatada = 1 + taxa_juros / 100
    armazena_montante = valor_deposito_inicial * taxa_juros_formatada

    for i in range(11):
        valor_deposito_mes_corrente = float(input(f"Informe o valor do depósito do mês {i + 2}: "))
        armazena_montante += valor_deposito_mes_corrente
        print(f"O montante atual é: {armazena_montante * taxa_juros_formatada}")

    return armazena_montante


