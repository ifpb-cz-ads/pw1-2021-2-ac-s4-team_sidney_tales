km = float(input("Informe a quantidade de km rodados: "))
quantDias = int(input("Informe a quantidade de dias que o carro foi alugado: "))

valorDias = quantDias * 60
valorKm = km * 0.15

total = valorDias + valorKm

print("O valor pago será de %.2f R$" %(total))
