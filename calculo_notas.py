faixa1=5
faixa2=10
faixa3=15
faixa4=20
faixa5=30
faixa6=40
faixa7=50
faixa8=65
faixa9=75
maximo=100


print("Não usar vírgulas, digite números inteiros de 0 a 100.")

while True:

    number = input("Digitar a nota 0 a 100: ")
    number = int(number)

    if number > maximo :
        print("valor inválido")
    elif number > faixa9 :
        print("")
        print("5")
        print("")
    elif number > faixa8:
        print("")
        print("4,5")
        print("")
    elif number > faixa7:
        print("")
        print("4")
        print("")
    elif number > faixa6:
        print("")
        print("3,5")
        print("")
    elif number > faixa5:
        print("3")
    elif number > faixa4:
        print("")
        print("2,5")
        print("")
    elif number > faixa3:
        print("")
        print("2")
        print("")
    elif number > faixa2:
        print("")
        print("1,5")
        print("")
    elif number > faixa1:
        print("")
        print("1")
        print("")
    elif number <= faixa1:
        print("")
        print("0,5")
        print("")
    else :
        print("")
        print("valor inválido")
        print("")
