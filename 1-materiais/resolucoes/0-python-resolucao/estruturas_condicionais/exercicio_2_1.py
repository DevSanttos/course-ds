# analisa_numeros

def analisa_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if num1 > num2:
        return f"O primeiro número ({num1}) é maior que o segundo ({num2})."
    elif num1 < num2:
        return f"O segundo número ({num2}) é maior que o primeiro ({num1})."
    else:
        return f"Os números são iguais ({num1})."