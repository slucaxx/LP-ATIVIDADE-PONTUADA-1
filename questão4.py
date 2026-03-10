import os
os.system("cls")

# ENTRADA
print("---------LOJA DE FRUTAS-----")
print(""" 
            |        até 5kg       |     Acima de 5kg  |
Morango     |     R$ 2,50 POR KG   |    R$ 2,20 POR KG |
Maça        |      R$ 1,80 POR KG  |   R$ 1,50 POR KG  |
""")


kg_morango = float(input("Digite a quantidade de morangos (Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (Kg): "))


if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_morango = kg_morango * preco_morango
total_maca = kg_maca * preco_maca

valor_bruto = total_morango + total_maca
peso_total = kg_morango + kg_maca

if peso_total > 10 or valor_bruto > 15.00:
    desconto = valor_bruto * 0.10
    valor_final = valor_bruto - desconto
    print(f"\nDesconto de 10% aplicado! (R$ {desconto:.2f})")
else:
    valor_final = valor_bruto
    print("\nSem descontos adicionais aplicados.")

# SAÍDA
print(f"Peso total: {peso_total:.22f} Kg")
print(f"Valor Total a Pagar: R$ {valor_final:.2f}")


