
distancia = float(input('Insira distancia a ser percorrida durante a viagem em km: '))
velocidade = float(input('Insira a velocidade média esperada em km/h: '))
duracao = int(distancia / velocidade), 'horas'
if distancia % velocidade != 0:
duracao = int(distancia / velocidade), 'horas e', int(distancia % velocidade), 'minutos'

print(duracao)
