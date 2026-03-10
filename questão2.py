import os
os.system("cls")

# ENTRADA
print("----------SOLICITANDO DADOS-----------")

nome=input("por favor,digite seu nome: ")
sexo=input("por favor,nos informe seu sexo (M\F): ")
est_civ=input("por favor,nos informe seu estado civil: ")

# PROCESSAMENTO


if sexo == "F"  and est_civ == "casada":
    tempo=input("quanto tempo de casada (anos)? ")
    print("----------RESUMO--------") 
    print(f"seu nome é {nome} \no seu sexo é {sexo} \nseu estado civil é {est_civ} \no seu tempo de casada é {tempo}")

     
else:
    print("----------RESUMO--------") 
    print(f"seu nome é {nome} \no seu sexo é {sexo} \nseu estado civil é {est_civ}")

     
    