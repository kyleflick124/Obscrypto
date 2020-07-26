#--------------------------------
#Programa de Criptografia Obscura 
#--------------------------------
#Esse programa foi feito como projeto para
#o semeste 2020/01 do HackoonSpace.
#Link do GitHub: 
#fonfon.com
#--------------------------------


#importando Tkinter, já disponível na biblioteca de python, para fazer o GUI do programa.
import tkinter as tk

#Importando base 64, para fazer um dos processos de criptografia:
import base64

#declarando a janela do programa como a variável "window" e definindo algumas
#outras opções como o título da guia e o tamanho do GUI.
window = tk.Tk()

window.title("Obscrypto")

window.geometry("640x640")


#------------FUNÇÕES-----------------

#A partir de agora definiremos e modificaremos as diferentes estruturas do GUI: título, caixas de texto e botões.
#As funções precisam ser definidas antes dessas estruturas pois os mesmos só vão executar a função depois de 
#um input do usuário, como nas funções que definimos em programas normais em python.

def decimal_to_octal(decimal):
    octal = 0
    i = 0
    while (decimal <= 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10 

def criptografar():
	password = str(entry_field1.get())
	
	#-------------Criptografando!-----------------
	
	#Duplicando a senha invertidamente:
	password = list(password)
	i = len(password)
	i = i - 1
	while i >= 0:
		password.append(password[i])
		i = i - 1
	
	#transformando todos os caracteres da senha em ascii:
	i = 0
	for char in password:
		x = len(password)
		while i < x:
			password[i] = ord(password[i])
			i = i+1
	x = len(password) * 2	
	i = 0
	while i < x:
		password.insert(i + 1," ")
		i = i + 2
	
	#transformando todos os caracteres da senha para octal:
	i = 0
	for char in password:
		x = len(password)
		while i < x:
			if password[i] == 32:
				password[i] = 0o40
			else:
				password[i] = oct(password[i])
			i = i+1
		
	#agora transformando a senha em uma string, para não contar os espaços:
	strings = [str(char) for char in password]
	string = "  ".join(strings)
	password = str(string)

	#transformando todos os caracteres da senha para base64:
	password_bytes = password.encode('ascii')
	base64_bytes = base64.b64encode(password_bytes)
	base64_password = base64_bytes.decode('ascii')
	password = base64_password
	
	#----------Fim-da-Criptografia----------------
	return password
	
def password_display():
	newpassword = criptografar()
	
	#criando o local onde a nova senha será exibida:
	display1 = tk.Text(master=window, height=20, width=50)
	display1.grid(column=1, row =4)
	
	display1.insert(tk.END, newpassword)
	
#-------------LABELS-----------------

title = tk.Label(text="Bem vindo ao Obscrypto, um software que usa criptografia obscura para tornar suas senhas ainda mais seguras!")
title.grid(column=1, row=0)

title2 = tk.Label(text="Para iniciar, insira sua possível senha na caixa de texto abaixo e clique no botão!")
title2.grid(column=1, row=1)


#------------ENTRIES-----------------

entry_field1 = tk.Entry()
entry_field1.grid(column=1, row=2)

#------------BUTTONS-----------------

button1 = tk.Button(text="criptografar!", command=password_display)
button1.grid(column=1, row=3)

#a função mainloop garante que o programa seja executado como um loop
#de eventos constante, até que o "X" para sair do programa seja clicado
#ou o programa seja finalizado.
window.mainloop()

#Observação: O mainloop só conta as mudanças feitas à grade que vierem
#antes dele no código, se tivesse um texto após o mainloop ele não seria
#acrescentado.
