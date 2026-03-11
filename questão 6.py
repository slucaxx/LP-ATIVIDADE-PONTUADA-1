import os
os.system("cls")

# ENTRADA
print("-------SISTEMA DE NOTAS-------")

nota1=float(input("digite sus primeira nota: "))
nota2=float(input("digite sus segunda nota: "))

media=(nota1+nota2) /2

if media >= 6.00:
    print(f"PARABENS,você está aprovado, sua media é {media}")
elif media == 4.00:
    print(f"PARABENS,você foi aprovado por pouco,sua media é {media}")
else:
    print(f"QUE PENA,você está reprovado,sua media é {media}")

print("=========FIM===========")
    
