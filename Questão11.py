preco = float(input("Informe o preco da mercadoria: "))
desconto = float(input("Informe o percentual do desconto: "))

valor = (desconto /100) * preco
total = preco - valor

print("O desconto foi de %.2f R$" %(valor))
print("O preco da mercadoria ficou em %.2f R$" %(total))

