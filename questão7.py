import os
os.system("cls")


# ENTRADA
print("------- ANALISE DE PRODUTOS -------")

nome = input("Digite o nome do produto: ")
quantidade = int(input("digite a quantidade desejada : "))
preco = float(input("digite o Preço do profuto: "))

total_bruto = quantidade * preco

if quantidade <= 5:
    percentual = 2 / 100
elif quantidade <= 10:
    percentual = 3 / 100
else:
    percentual = 5 / 100


valor_do_desconto = total_bruto * percentual
total_a_pagar = total_bruto - valor_do_desconto

print(f"Produto: {nome}")
print(f"Você escolheu {quantidade} unidades.")
print(f"Desconto : {percentual*100}%")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
    
