# Importa tudo da biblioteca tkinter, necessária para a interface gráfica (IG).
from tkinter import *

# O comando print envia a mensagem para o terminal, não é visualizado na IG.
print("Não usar vírgulas, digite números inteiros de 0 a 100.")

# Faixas com os valores que definem os máximos e mínimos nos intervalos.
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
janela.title("conversor v.2022")


texto1 = Label(janela, text="Digite números inteiros de 0 a 100:")
texto1.grid(column=0, row=0, padx=10, pady=10)
texto1.config(font=('helvetica', 12))


entrada = Entry(janela, width=3)
entrada.grid(column=0, row=1, padx=10, pady=10)
entrada.config(font=('helvetica', 24, 'bold'))

# Habilita o uso da tecla ENTER para atribuição do valor
entrada.bind('<Return>', funcao_convercao)

texto_nota = Label(janela, text="__")
texto_nota.grid(column=0, row=2, padx=10, pady=10)
texto_nota.config(font=('helvetica', 24, 'bold'))


message = ('Critério de conversão:\n'
           '\n'
           'abaixo de 5:        0,5\n'
           'acima de 5 até 10:  1,0\n'
           'acima de 10 até 15: 1,5\n'
           'acima de 15 até 20: 2,0\n'
           'acima de 20 até 30: 2,5\n'
           'acima de 30 até 40: 3,0\n'
           'acima de 40 até 50: 3,5\n'
           'acima de 50 até 65: 4,0\n'
           'acima de 65 até 75: 4,5\n'
           'acima de 75:        5,0 \n'
           '\n'
           'Digitar apenas números inteiros\n'
           'não utilizar ponto ou vírgula\n'
           '\n'
           'Desenvolvido em Python por:\n'
           'Waldo Costa\n'
           'waldocosta.com.br')

text_box = Text(
    janela,
    height=19,
    width=32
)
text_box.grid(column=0, row=3, padx=10, pady=10)
text_box.insert('end', message)
text_box.config(state='disabled')

janela.mainloop()
