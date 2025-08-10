# quilowatt

def realiza_calculo_quilowatt(valor_salario_minimo, quantidade_quilowatt_consumida):
    valor_quilowatt = valor_salario_minimo / 5
    valor_conta_energia = valor_quilowatt * quantidade_quilowatt_consumida
    valor_a_pagar_com_desconto = valor_conta_energia - (valor_conta_energia * 0.15)

    return (f"Valor de cada quilowatt: {valor_quilowatt:.2f} \n"
            f"Valor da conta de energia: {valor_conta_energia:.2f} \n"
            f"Valor da conta com desconto: {valor_a_pagar_com_desconto:.2f}")