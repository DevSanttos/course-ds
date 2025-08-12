# apresenta_numeros

def apresenta_numeros():
    I = int(input("Informe o valor de I: "))
    A = float(input("Informe o valor de A: "))
    B = float(input("Informe o valor de B: "))
    C = float(input("Informe o valor de C: "))
    aux = []

    if I == 1: 
        sorted(A, B, C)
    elif I == 2:
        sorted(A, B, C, reverse=True)
    elif I == 3:
        aux.append(A)
        aux.append(B)
        aux.append(C)
        
        maior_valor = max(aux)

        if maior_valor == A:
            valor_realocacao = aux.pop[1]
            aux.insert(1, maior_valor)
            aux.insert(0, valor_realocacao)
            return f"Segue a apresentação dos números: {aux}"
        elif maior_valor == C:
            valor_realocacao = aux.pop[1]
            aux.insert(1, maior_valor)
            aux.insert(0, valor_realocacao)
            return f"Segue a apresentação dos números: {aux}"
        else:
            return f"Segue a apresentação dos números: {aux}"