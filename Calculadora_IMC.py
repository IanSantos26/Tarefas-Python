from tkinter import *


janela= Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg='#808080')

#=================================#
#Palheta de Cores

cor1='#808080' #cinza 
cor2='#000000' #preto
cor3='#993399' #roxo
cor4='#ffffff' #branco

#=================================#

#Divisão da Janela

frame_superior= Frame(janela,width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_superior.grid(row=0, column=0, sticky=NSEW)

frame_inferior= Frame(janela,width=295, height=180, bg=cor1, pady=0, padx=0, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=NSEW)

#Definição parte Superior

app_nome= Label(frame_superior, text='Calcuradora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=cor1, fg=cor2)
app_nome.place(x=0, y=0)

app_linha= Label(frame_superior, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1 '), bg=cor3, fg=cor3)
app_linha.place(x=0, y=35)

#=================================#

#Logica do Calculo


def calcular():

    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] = "Seu IMC é: Abaixo do Peso"
    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = "Seu IMC é: Normal"
    elif resultado >= 25 and resultado < 30:
        l_resultado_texto['text'] = "Seu IMC é: Sobrepeso"
    else:
        l_resultado_texto['text'] = 'Seu IMC é: Obesidade'


    l_resultado['text'] = "{:.{}f}".format(resultado, 2)


    #=================================#


#Definição parte Inferior

l_peso= Label(frame_inferior, text='Insira seu Peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor2)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_peso= Entry(frame_inferior, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

#=================================#

l_altura= Label(frame_inferior, text='Insira sua Altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor2)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_altura= Entry(frame_inferior, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

#=================================#

l_resultado= Label(frame_inferior, text='---', width=5, height=1, padx=6, pady=12,  relief='flat', anchor='center', font=('Ivy 24 bold'), bg=cor3, fg=cor4)
l_resultado.place(x=175, y=10)

#=================================#

l_resultado_texto= Label(frame_inferior, text='', width=37, height=1, padx=0, pady=12,  relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor2)
l_resultado_texto.place(x=0, y=90)

#=================================#

b_calcular= Button(frame_inferior, command=calcular, text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=cor3, fg=cor4)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

#=================================#



janela.mainloop()

