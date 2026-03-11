import os
os.system("cls")

# ENTRADA
print("---------LOJA DE FRUTAS-----")
print(""" 
            |        até 5kg       |     Acima de 5kg  |
Morango     |     R$ 2,50 POR KG   |    R$ 2,20 POR KG |
Maça        |      R$ 1,80 POR KG  |   R$ 1,50 POR KG  |
""")


kg_mo = float(input("Digite a quantidade de morangos (Kg): "))
kg_maça = float(input("Digite a quantidade de maçãs (Kg): "))


if kg_mo <= 5:
     pre_mo = 2.50
else:
    pre_mo = 2.20

if kg_maça <= 5:
    pre_maça = 1.80
else:
    preco_maça = 1.50

to_mo = kg_mo * pre_mo
to_maca = kg_maça * pre_maça

va_total = to_mo + to_maca
peso_total = kg_mo + kg_maça

if peso_total > 10 or va_total > 15.00:
    desconto = va_total * 0.10
    valor_final = va_total - desconto
    print(f"você tem um desconto de 10% (R$ {desconto:.2f})")
else:
    valor_final = va_total
    print("Sem descontos")

# SAÍDA
print(f"Peso total: {peso_total:.2f} Kg")
print(f"Valor Total a Pagar: R$ {valor_final:.2f}")

print("==========FIM==========")



