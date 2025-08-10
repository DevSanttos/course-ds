# aumento_salario_faixa

def calcula_aumento_salarial():
    salario = float(input("Informe o salário do funcionário: "))

    if salario > 1250:
        return f"O aumento salarial é de: {salario * 0.1:.2f}"
    else:
        return f"O aumento salarial é de: {salario * 0.15:.2f}"
