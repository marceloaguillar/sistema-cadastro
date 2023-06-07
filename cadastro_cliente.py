import tkinter as tk
import sqlite3
import pandas as pd

#CRIAR BANCO DE DADOS
#conexao = sqlite3.connect('bancos_clientes.db')
#cursor = conexao.cursor()
#cursor.execute(''' CREATE TABLE clientes (
   # nome text,
   # sobrenome text,
   # email text,
   # telefone text
 #   )
#''')

#conexao.commit()
#conexao.close()


janela = tk.Tk()
janela.title('Ferramenta de Cadastro de Clientes')

#IDENTIFICAÇÃO DAS ENTRADAS
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=1, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=2, column=0, padx=10, pady=10)

#ENTRADAS
entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='E-mail', width=30)
entry_email.grid(row=1, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

#botões



janela.mainloop()
#CRIAR TABELA
#COMENTAR A CRIAÇÃO DO BANCO
#CRIAR A INTERFACE GRÁFICA
#INTEGRAR BANCO COM BOTÕES
