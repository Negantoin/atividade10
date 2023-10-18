# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
vel = float(input("Digite a velocidade registrada em Km/h: "))
if vel > 60:
    multa = vel * 7
    print("Que motorista malvado! Sua multa é de: R$", multa)