import os
os.system("cls")

# ENTRADA

print("---------OPERAÇÃO-----")

n1=int(input("digige um numero: "))
n2=int(input("digige outro numero: "))
sinal=input("digite a operação desejada (+,-,* ou /): ")

soma=n1+n2
subtração=n1-n2
multiplicação=n1*n2
divisão=n1/n2

if sinal == "+":
    print(f"o resultado com o sinal {sinal} foi {soma}")
elif sinal == "-":
    print(f"o resultado com o sinal {sinal} foi {subtração}")
elif sinal == "*":
    print(f"o resultado com o sinal {sinal} foi {multiplicação}")
elif sinal == "/":
    print(f"o resultado com o sinal {sinal} foi {divisão}")
    
print("=======FIM======")
