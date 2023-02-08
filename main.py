from os import system

green = "\033[1;32m"
red = "\033[1;31m"
cancel = "\033[m"

while True:
    nota_1 = str(input("Digite a primeira nota: "))
    if(not nota_1.isnumeric()):
        print("Valor da primeira nota não é numerica, porfavor digite novamente.")
    else:
        nota_1 = int(nota_1)
        break
    
while True:
    nota_2 = str(input("Digite a segunda nota: "))
    if(not nota_2.isnumeric()):
        print("Valor da segunda nota não é numerica, porfavor digite novamente.")
    else:
        nota_2 = int(nota_2)
        break

media = (nota_1+nota_2)/2

system('cls')

print(f"A média do aluno corresponde à {media}.", end=' ')
if(media < 50):
    print(f"Portanto o aluno está {red}reprovado{cancel}.")
else:
    print(f"Portanto o aluno está {green}aprovado{cancel}.")
