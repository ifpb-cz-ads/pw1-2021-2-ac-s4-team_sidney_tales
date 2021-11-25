salario = float(input("Informe o valor do salario: "))
aumento = float(input("Informe o percentual do aumento: "))

valor = (aumento /100) * salario
total = valor + salario

print("O aumento foi de %.2f R$" %(valor))
print("O salario ficou em %.2f R$" %(total))
