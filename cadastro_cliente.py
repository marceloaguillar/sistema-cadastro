import tkinter as tk
import sqlite3
import pandas as pd
import phonenumbers

def formatar_telefone(*args):
    telefone = entry_telefone.get()
    
    # Remover todos os caracteres não numéricos do número de telefone
    telefone = ''.join(filter(str.isdigit, telefone))
    
    # Formatar o número de telefone com a formatação brasileira
    telefone_formatado = ''
    if telefone:
        telefone_formatado = phonenumbers.format_number(
            phonenumbers.parse(telefone, 'BR'),
            phonenumbers.PhoneNumberFormat.NATIONAL
        )
    
    # Atualizar o campo de entrada (Entry) com o telefone formatado
    entry_telefone.delete(0, tk.END)
    entry_telefone.insert(0, telefone_formatado)

def cadastrar_cliente():
    
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    conexao = sqlite3.connect('bancos_clientes.db')
    cursor = conexao.cursor()
    cursor.execute( '''INSERT INTO clientes (nome, email, telefone) values (?, ?, ?) ''', (nome,email,telefone))
           
    conexao.commit()
    conexao.close()
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

def exportar_cliente():
    return


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
entry_telefone.bind('<KeyRelease>', formatar_telefone)

#BOTÕES
botao_cadastrar = tk.Button(janela, text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=3, column=0, padx=10, pady=10)

botao_exportar = tk.Button(janela, text='Exportar banco de dados', command=exportar_cliente)
botao_exportar.grid(row=3, column=1, padx=10, pady=10)

janela.mainloop()
#CRIAR TABELA
#COMENTAR A CRIAÇÃO DO BANCO
#CRIAR A INTERFACE GRÁFICA
#INTEGRAR BANCO COM BOTÕES
