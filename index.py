#Programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite 
v = int(input('Diga a velocidade do carro:'))
if v >80:
    print('Você recebeu uma multa no valor de R$ {}, pois excedeu o limite de 80km/h permitido'. format((v - 80)* 7))
else:
    print('Siga viagem')