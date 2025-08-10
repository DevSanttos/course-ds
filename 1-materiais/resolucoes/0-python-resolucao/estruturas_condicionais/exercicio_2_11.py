# nota_ponderada

def nota_ponderada():
    trabalho_lab = {
        "nota": float(input("Digite a nota do trabalho de laboratório: ")),
        "Peso": 2
    }

    prova_semestal = {
        "nota": float(input("Digite a nota da prova semestral: ")),
        "Peso": 3
    }

    exame_final = {
        "nota": float(input("Digite a nota do exame final: ")),
        "Peso": 5
    }

    trabalho_lab["nota"] *= trabalho_lab["Peso"]
    prova_semestal["nota"] *= prova_semestal["Peso"]
    exame_final["nota"] *= exame_final["Peso"]

    return (trabalho_lab["nota"] + prova_semestal["nota"] + exame_final["nota"]) / 10


