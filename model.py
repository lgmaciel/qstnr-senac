'''
Esta é nossa model.

Livro, Leitor e Emprestimo por enquanto
são simples 'pacotes de dados'

As regras de negócio estão implementadas
na Biblioteca.

Use o código, trabalhado em aula,
como exemplo para completar as operações
de CRUD do sistema.

'''
class Biblioteca:

    def __init__(self):
        self.livros = dict()
        self.leitores = dict()
        self.emprestimos = list()

    def cadastrar_livro(self, cod, titulo):
        livro = Livro()
        livro.set_cod(cod)
        livro.set_titulo(titulo)

        self.livros[livro.cod] = livro

    def consultar_livro(self, cod):
        try:
            return self.livros[cod]
        except KeyError:
            return False
    
    def excluir_livro(self, cod):
        try:
            del self.livros[cod]        
            return True
        except KeyError:
            return False
    
    def atualizar_livro(self, cod, titulo):
        # caso o código tenha mudado
        self.excluir_livro(cod)
        self.cadastrar_livro(cod, titulo)

    # FAZER: completar CRUD  do Leitor
    # Em Biblioteca:    
    # - consultar_leitor(cpf)
    # - excluir_leitor(cpf)
    # - atualizar_leitor(cpf, )
    #
    # Em Leitor:
    # - adicionar propriedade 'cpf'
    # - adicionar propriedade 'nome'
    # - adicionar setters/getters conforme necessidade
    #
    def cadastrar_leitor(self, leitor):
        self.leitores[leitor.cpf] = leitor

    def emprestar(self, livro, leitor):
        data_de_devolucao = self.calcular_data_devolucao()
        livro.set_emprestado()

        novo_emprestimo = Emprestimo(livro, leitor, data_de_devolucao)
        self.emprestimos.append(novo_emprestimo)
        return novo_emprestimo
        

    def calcular_data_devolucao(self):
        import datetime
        hoje = datetime.date.today()
        tempo_de_emprestimo = datetime.timedelta(weeks=1)
        # somamos 1 semana à data de emprestimo
        return hoje + tempo_de_emprestimo
        
class Livro:
    def __init__(self):
        self.emprestado = False

    def set_titulo(self, titulo):
        self.titulo = titulo
    def set_cod(self, cod):
        self.cod = cod
    def set_emprestado(self):
        self.emprestado = True

class Leitor:
    def __init__(self):
        self.emprestimos = list()

    def add_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

class Emprestimo:

    def __init__(self, livro, leitor, data_devolucao):
        self.livro = livro
        self.leitor = leitor
        self.data_devolucao = data_devolucao

# Inicializamos abiblioteca / conectamos à model da biblioteca
# Este objeto 'biblioteca' ficará exposto no pacote para ser
# acessado pelo controller, que por enquanto estamos implementando
# no módulo view.py.
biblioteca = Biblioteca()