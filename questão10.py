import os
os.system("cls")

# ENTRADA
print("-----------POSTO----------")

litros = float(input("Quantidade de litros: "))
tipo = input("Tipo (A-Álcool, G-Gasolina): ")

preco_a = 3.79
preco_g = 6.59

if tipo == 'A':
    total_bruto = litros * preco_a
    desc = 0.03 if litros <= 20 else 0.05
    valor_final = total_bruto * (1 - desc)
    
elif tipo == 'G':
    total_bruto = litros * preco_g
    desc = 0.04 if litros <= 20 else 0.06
    valor_final = total_bruto * (1 - desc)

print(f"Valor a pagar: R$ {valor_final:.2f}")