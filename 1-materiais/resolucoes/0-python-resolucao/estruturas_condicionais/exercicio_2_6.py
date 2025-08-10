# operacao

def realiza_operacao():
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    tipo_operacao = input("Informe qual será a operação: ")

    if tipo_operacao == "multiplicação" or tipo_operacao == "*":
        return f"O resultado é: {num1 * num2}"
    elif tipo_operacao == "divisão" or tipo_operacao == "/":
        if num2 == 0:
            return "Valor inválido"
        else:
            return f"O resultado é: {num1 / num2}"
    elif tipo_operacao == "soma" or tipo_operacao == "+":
        return f"O resultado é: {num1 + num2}"
    elif tipo_operacao == "subtração" or tipo_operacao == "-":
        return f"O resultado é: {num1 - num2}"
    else:
        return "Tipo da operação é inválida! Tente novamente."

    