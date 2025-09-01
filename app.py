from textual.app import App, SystemCommand
from textual.binding import Binding
from textual.screen import Screen
from view import (TelaInicial, TelaCadastrarLivros, TelaCadastrarLeitores)

class AppBiblioteca(App):
    '''
    Classe principala da aplicação.
    '''

    '''Montamos as telas da app'''
    SCREENS = {
        "inicial": TelaInicial,
        "cadastrar_livros": TelaCadastrarLivros,
        "cadastrar_leitores": TelaCadastrarLeitores,
    }

    '''Criamos as associações entre comandos de teclado e funções da app'''
    BINDINGS = [
        Binding("escape", "ir_para_inicial", "Início"),
        Binding("ctrl+n", "cadastrar_livro", "Cadastrar Livro"),
        Binding("ctrl+l", "cadastrar_leitores", "Cadastrar Livro"),
    ]

    '''Montamos a tela inicial'''
    def on_mount(self):
        self.push_screen("inicial")


    '''
        Callbacks que farão a troca das telas.
        Foram definidos na estrutura BINDINGS
        assinatura dos métodos segue o formato:
            action_nome_da_acao
        São chamados pelo framework.        
    '''

    def action_ir_para_inicial(self):
        self.switch_screen("inicial")

    def action_cadastrar_livro(self):
        self.switch_screen("cadastrar_livros")

    def action_cadastrar_leitores(self):
        self.switch_screen("cadastrar_leitores")

    '''
        Exemplo tirado da documentação
        mostrando como utilizar o menu de comandos
        disponiblilizado pelo framework.
    '''

    def get_system_commands(self, screen: Screen):
        yield from super().get_system_commands(screen)
        yield SystemCommand("Bell", "Ring the bell", self.bell)    

if __name__ == "__main__":
    AppBiblioteca().run()
