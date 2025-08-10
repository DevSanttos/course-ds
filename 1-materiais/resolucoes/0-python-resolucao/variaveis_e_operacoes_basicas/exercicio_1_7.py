# converte_tempo

def converte_tempo(dias, horas, minutos, segundos):
    total_segundo = 0
    total_segundo += segundos
    total_segundo += minutos * 60
    total_segundo += (horas * 60) * 60
    total_segundo += ((dias * 60) * 60) * 24
    return total_segundo