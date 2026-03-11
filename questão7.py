import os
os.system("cls")


# ENTRADA
print("------- ANALISE DE PRODUTOS -------")

nome = input("Digite o nome do produto: ")
quantidade = int(input("digite a quantidade desejada: "))
preco = float(input("digite o Preço do profuto: "))

total = quantidade * preco

if quantidade <= 5:
    percentual = 2 / 100
elif quantidade <= 10:
    percentual = 3 / 100
else:
    percentual = 5 / 100


valord = total * percentual
total_pa = total - valord

print(f"Produto: {nome}")
print(f"Você escolheu {quantidade} unidades.")
print(f"Desconto : {percentual*100}%")
print(f"Total a pagar: R$ {total_pa:.2f}")
    

