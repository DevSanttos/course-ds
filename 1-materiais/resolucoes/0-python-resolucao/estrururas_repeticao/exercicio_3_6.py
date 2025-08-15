# leitura_numeros

def realiza_leitura_numero():
    armazena_quant_numeros_informados = 0
    realiza_soma_numeros_informados = 0
    while True:
        numero_corrente = float(input("Informe um número: "))

        if numero_corrente != 0:
            armazena_quant_numeros_informados += 1
            realiza_soma_numeros_informados += numero_corrente
        else:
            break
    
    return print(f"Quantidade de números digitados: {armazena_quant_numeros_informados}\nSoma dos números: {realiza_soma_numeros_informados} \nMédia dos números: {realiza_soma_numeros_informados/armazena_quant_numeros_informados}")

    