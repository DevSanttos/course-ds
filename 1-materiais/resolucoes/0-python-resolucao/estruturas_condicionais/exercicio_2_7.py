# emprestimo

def aprova_emprestimo():
    valor_casa = float(input("Informe o valor da casa: "))
    salario = float(input("Informe o valor do salário: "))
    quantidade_anos_a_pagar = int(input("Informe a quantidade de anos a pagar: "))

    valor_da_prestacao = valor_casa / (quantidade_anos_a_pagar * 12)

    if valor_da_prestacao > 0.3 * salario:
        return "Emprestimo negado, uma vez que o valor da prestação é maior que 30% do salário."
    else:
        return f"Emprestimo aprovado. Valor da prestão: {valor_da_prestacao:.2f}"

