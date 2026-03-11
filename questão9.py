import os
os.system("cls")

# ENTRADA
print("-----------EMPRESTIMO----------")

renda = float(input("digite a sua renda mensal: R$ "))
val_emp = float(input("informe o valor da empréstimo: R$ "))
parcelas = int(input("digte o numero de prestações dejesada: "))

val_pre = val_emp/ parcelas


condicao1 = val_emp <= (renda * 10)
condicao2 = val_pre <= (renda * 0.30)

if condicao1 and condicao2:
    print("Empréstimo CONCEDIDO")
else:
    print("Empréstimo NEGADO")
    
print("=======FIM========")

