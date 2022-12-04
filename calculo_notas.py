from tkinter import *

print("Não usar vírgulas, digite números inteiros de 0 a 100.")

faixa1 = 5
faixa2 = 10
faixa3 = 15
faixa4 = 20
faixa5 = 30
faixa6 = 40
faixa7 = 50
faixa8 = 65
faixa9 = 75
maximo = 100


def funcao_convercao(self):
    # number = input("Digitar a nota 0 a 100: ")
    x1 = entrada.get()
    number = int(x1)

    if number > maximo:
        nota_final = "valor inválido"
        print("valor inválido")
    elif number > faixa9:
        nota_final = 5
        print("5")
    elif number > faixa8:
        nota_final = 4.5
        print("4,5")
    elif number > faixa7:
        nota_final = 4
        print("4")
    elif number > faixa6:
        nota_final = "3,5"
        print("3,5")
    elif number > faixa5:
        nota_final = 3
        print("3")
    elif number > faixa4:
        nota_final = 2.5
        print("2,5")
    elif number > faixa3:
        nota_final = 2
        print("2")
    elif number > faixa2:
        nota_final = 1.5
        print("1,5")
    elif number > faixa1:
        nota_final = 1
        print("1")
    elif number <= faixa1:
        nota_final = 0.5
        print("0,5")
    else:
        nota_final = "valor inválido"
        print("valor inválido")

    texto_nota["text"] = nota_final


janela = Tk()
janela.title("conversor de notas v.2022.0.a")

texto1 = Label(janela, text="Não usar vírgulas, digite números inteiros de 0 a 100:")
texto1.grid(column=0, row=0, padx=10, pady=10)
texto1.config(font=('helvetica', 12))


entrada = Entry(janela)
entrada.grid(column=0, row=1, padx=10, pady=10)
entrada.config(font=('helvetica', 24, 'bold'))

# Bind the Enter Key to the window
entrada.bind('<Return>', funcao_convercao)

# botao = Button(janela, text="calcular", command=funcao_convercao, bg='black', fg='white', font=('helvetica', 9, 'bold'))
# botao.grid(column=1, row=1, padx=10, pady=10)

texto_nota = Label(janela, text="__")
texto_nota.grid(column=1, row=1, padx=10, pady=10)
texto_nota.config(font=('helvetica', 24, 'bold'))

janela.mainloop()
