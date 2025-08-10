# insere_numero

def ordena_numeros(num1, num2, num3, num4, num5, num6, num7):
    lista_numeros = [num1, num2, num3, num4, num5, num6, num7]
    aux = 0;
    ultimo_indice_dos_crescentes = 0;

    # 7 1 2 4 1 2 3


    for i in range(len(lista_numeros)):
        if (lista_numeros[i] + 1) == lista_numeros[i + 1]:
            aux += 1
            ultimo_indice_dos_crescentes = i
        else:
            aux = 0

    indice_inicio_dos_crescentes = lista_numeros[ultimo_indice_dos_crescentes - 2]

    return indice_inicio_dos_crescentes