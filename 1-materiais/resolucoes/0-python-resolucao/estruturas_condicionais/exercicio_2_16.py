# recursos_humanos

def recursos_humanos():
    opcao_selecionada = int(input("Menu de opções\n1. Imposto\n2. Novo salário\n3. Classificação\n"))
    
    if opcao_selecionada == 1:
        print("entrou")
        salario_funcionario = float(input("Informe o seu salário: "))

        if salario_funcionario > 850:
            return f"O imposto, com base no seu salário é: {salario_funcionario * 0.15}"
        elif salario_funcionario >= 500.00 and salario_funcionario <= 850.00:
            return f"O imposto, com base no seu salário é: {salario_funcionario * 0.10}"
        else:
            return f"O imposto, com base no seu salário é: {salario_funcionario * 0.05}"
        
    elif opcao_selecionada == 2:
        salario_funcionario = float(input("Informe o seu salário: "))

        if salario_funcionario > 1500:
            return f"O valor do novo salário é de: {salario_funcionario + 25.00}"
        elif salario_funcionario >= 750.00 and salario_funcionario <= 1500.00:
            return f"O valor do novo salário é de: {salario_funcionario + 50.00}"
        elif salario_funcionario >= 450.00 and salario_funcionario < 750.00:
            return f"O valor do novo salário é de: {salario_funcionario + 75.00}"
        else:
            return f"O valor do novo salário é de: {salario_funcionario + 100.00}"
        
    elif opcao_selecionada == 3:
        salario_funcionario = float(input("Informe o seu salário: "))

        if salario_funcionario > 700:
            return "Bem remunerado!"
        else:
            return "Mal remunerado!"
    
    else:
        return "Selecione uma opção válida!"