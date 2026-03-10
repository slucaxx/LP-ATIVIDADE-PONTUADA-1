import os
os.system("cls")

# ENTRADA
print("----------VALORES A,B,C ------------")

n1=int(input("por favor,digite um numero: "))
n2=int(input("por favor,digite outro numero: "))
n3=int(input("por favor,digite o terceiro numero: "))

# PROCESSAMENTO
soma= n1+n2

if soma < n3:
    print(f"a soma ({soma}) do primeiro numero ({n1}) mais o segundo numero ({n2}) é menor que o terceiro numero ({n3})")
elif soma > n3:
    print(f"a soma ({soma}) do primeiro numero ({n1}) mais o segundo numero ({n2}) é maior que o terceiro numero ({n3})")
    
print("======FIM======")
