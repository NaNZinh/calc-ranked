def calculo(x, y):
    saldoVitorias = x - y
    return saldoVitorias

def verificacao(x):
    if x <= 10:
        nivel = "Ferro"
    elif x > 10 and x <= 20:
        nivel = "Bronze"
    elif x > 20 and x <= 50:
        nivel = "Prata"
    elif x > 50 and x <= 80:
        nivel = "Ouro"
    elif x > 80 and x <= 90:
        nivel = "Diamante"
    elif x > 90 and x <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    return nivel
vitorias = 100
derrotas = 49
saldoVitorias = calculo(vitorias, derrotas)
nivel = verificacao(saldoVitorias)
print("O Herói tem o saldo de", saldoVitorias, "está no nível", nivel)