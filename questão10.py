import os
os.system("cls")

# Entrada
print("""
---------------------TABELA DE DESCONTO---------------------
         | Até 25 litros,desconto de 2% por litro
ÁLCOOL   | acima de 25 litros,desconto do 4% por litros
_______________________________________________________________-
         | até 25 litos,desconto de 3% por litos
GASOLINA | acima de 25 litos,desconto de 5% por litro
   """)
litros = float(input("Digite a quantidade de litros dejesado: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ")

preco_gasolina = 6.59
preco_alcool = 3.79

val_final = 0

if tipo == 'A':
    if litros <= 24:
        desconto = 0.02
    elif litros > 25:
        desconto = 0.04 
    val_final = litros * (preco_alcool *  desconto)


elif tipo == 'G':
    if litros <= 24:
        desconto = 0.03 
    elif litros > 25:
        desconto = 0.05
    val_final = litros * (preco_gasolina * desconto)

else:
    print("Tipo de combustível inválido!")

# Saída
if val_final > 0:
    print(f"Total a pagar: R$ {val_final:.2f}")
