import os
os.system("cls")

# ENTRADA
print("-------SOLICITANDO DADOS---------")
print("se os numeros forem iguais usaremos a soma,se forem diferente multiplicação")

n1=int(input("digite um numero: "))
n2=int(input("digite outro numero: "))


soma=n1+n2
multiplicação=n1*n2

if n1 == n2:
   print(f"a soma dos numero ({n1}) e ({n2}) foi {soma}")
else:
    print(f"a multiplicação dos numeros ({n1}) e ({n2}) foi ({multiplicação})")

print("======FIM=======")