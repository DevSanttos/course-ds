# opera_real

def opera_real(num_real):
    parte_inteira = int(num_real)
    parte_fracionaria = num_real - parte_inteira
    num_real_arredondado_para_uma_casa = round(num_real, 1)
    num_real_arredondado_para_inteiro = round(num_real)
    return (f"Parte inteira: {parte_inteira} \n"
            f"Parte fracionaria: {parte_fracionaria} \n"
            f"Arredondamento para uma casa decimal: {num_real_arredondado_para_uma_casa} \n"
            f"Arredondamento para um inteiro: {num_real_arredondado_para_inteiro}")