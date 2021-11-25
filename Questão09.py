dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

totaldias = (dias * 24) * 3600
totalhoras = horas * 3600
totalmin = minutos * 60
total = totaldias + totalhoras + totalmin + segundos
print("A quantidade de segundos é: %d " %(total))