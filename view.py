from textual.screen import Screen
from textual.widgets import (Header, Footer, Static)
from model import (biblioteca, Livro, Leitor, Emprestimo)

'''
Aqui temos o 'esqueleto' das telas da app.
Sua tarefa é montar cada Screen com os componentes
de interface necessários para realizar os use cases
de Cadastro e Consulta de livros e leitores.

Observe que você já tem à disposição do controller
o ponto de entrada da model da app, que é o objeto
biblioteca.

Ex.

biblioteca.cadastrar_leitor(um_leitor)
'''

class TelaInicial(Screen):
    def compose(self):
        yield Header(show_clock=True)  # Exibe o cabeçalho com relógio
        yield Static("Bem-vindo à Biblioteca")
        yield Footer()  # Exibe o rodapé padrão

class TelaCadastrarLivros(Screen):
    def compose(self):
        yield Header(show_clock=True)  # Exibe o cabeçalho com relógio        
        yield Footer()  # Exibe o rodapé padrão
        yield Static("Esta é a tela de cadastro de livros.")

class TelaCadastrarLeitores(Screen):
    def compose(self):
        yield Header(show_clock=True)  # Exibe o cabeçalho com relógio        
        yield Footer()  # Exibe o rodapé padrão
        yield Static("Esta é a tela de cadastro de leitores.")
