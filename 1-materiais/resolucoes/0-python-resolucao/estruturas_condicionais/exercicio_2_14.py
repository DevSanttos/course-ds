# par_impar

def verifica_par_impar():
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        return "O número é par!"
    else:
        return "O número é ímpar!"