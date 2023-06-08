import tkinter as tk
import sqlite3
import pandas as pd
import phonenumbers

def formatar_nome(event):
    nome = entry_nome.get()

    # Formatar o nome com a primeira letra maiúscula
    nome_formatado = nome.title()

    # Atualizar o campo de entrada (Entry) com o nome formatado
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, nome_formatado)

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

    #VERIFICAR SE TODOS AS INFORMAÇÕES FORAM PREENCHIDAS, ANTES DE MANDR PARA O BANCO DE DADOS
    if nome == '' or email == '' or telefone == '':
        label_mensagem.config(text='PREENCHA TODAS AS INFORMAÇÕES....')
        return

    conexao = sqlite3.connect('bancos_clientes.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)''', (nome, email, telefone))

    conexao.commit()
    conexao.close()

    label_mensagem.config(text='CLIENTE CADASTRADO COM SUCESSO!')
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)


def exportar_cliente():
    conexao = sqlite3.connect('bancos_clientes.db') 
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, email, telefone FROM clientes")
    clientes_db = cursor.fetchall()
    clientes_db = pd.DataFrame(clientes_db, columns=["Nome","E-mail","Telefone"])
    clientes_db.to_excel('BANCO DE DADOS DE CLIENTES.xlsx', index=False)  # Remova o índice (ID)
    conexao.commit()
    conexao.close()



janela = tk.Tk()
janela.title('CADASTRO DE CLIENTES')

#IDENTIFICAÇÃO DAS ENTRADAS
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=1, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=2, column=0, padx=10, pady=10)

#ENTRADAS
label_mensagem = tk.Label(janela, text='')
label_mensagem.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)
entry_nome.bind('<KeyRelease>', formatar_nome)

entry_email = tk.Entry(janela, text='E-mail', width=30)
entry_email.grid(row=1, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)
entry_telefone.bind('<KeyRelease>', formatar_telefone)

#BOTÕES
botao_cadastrar = tk.Button(janela, text='CADASTRAR CLIENTE', command=cadastrar_cliente)
botao_cadastrar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

botao_exportar = tk.Button(janela, text='EXPORTAR BANCO DE DADOS', command=exportar_cliente)
botao_exportar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

janela.mainloop()

