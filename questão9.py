import os
os.system("cls")

# ENTRADA
print("-----------EMPRESTIMO----------")

renda = float(input("Renda mensal: R$ "))
val_emp = float(input("Valor total do empréstimo: R$ "))
parcelas = int(input("Número de prestações: "))

val_pre = val_emp/ parcelas


condicao1 = val_emp <= (renda * 10)
condicao2 = valor_prestacao <= (renda * 0.30)

if condicao1 and condicao2:
    print("Empréstimo CONCEDIDO!")
     print("- Valor total excede 10x a renda.")
else:
    print("Empréstimo NEGADO!")
    print("- Valor da prestação excede 30% da renda.")
        

print("=======FIM========")
