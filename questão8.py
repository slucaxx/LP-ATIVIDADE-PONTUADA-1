import os
os.system("cls")

# ENTRADA
print("----------LOJA DE CDS--------")
cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ")

if cor == "verde":
    preco = 10.00
elif cor == "azul":
    preco = 20.00
elif cor == "amarelo":
    preco = 30.00
elif cor == "vermelho":
    preco = 40.00
else:
    preco = None

if preco:
    print(f"O preço do CD é R$ {preco:.2f}")
else:
    print("Cor inválida!")

print("========FIM=========")
