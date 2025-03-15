import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
import requests
import json

from books.templates.telas.adicionar_livro_page import AdicionarLivroPage
from books.templates.telas.dashboard_page import Ui_MainWindow
from books.templates.telas.editar_livro_page import EditarLivroPage
from books.templates.telas.initial_page import InitialPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.adicionar_livro_page = AdicionarLivroPage()
        self.dashboard_page = Ui_MainWindow()

        # Passa a referência da janela principal (self) para o setupUi
        self.adicionar_livro_page.setupUi(self, self)  # self é a MainWindow
        self.dashboard_page.setupUi(self)

        self.adicionar_livro_page.botaoCadastrar.clicked.connect(self.salvar_livro)
        self.dashboard_page.botaoCadastrar_2.clicked.connect(self.carregar_livros)
        self.dashboard_page.botaoCadastrar.clicked.connect(self.abrir_adicionar_livro)

    def show(self):
        super().show()
        self.carregar_livros()

    def salvar_livro(self):
        titulo = self.adicionar_livro_page.lineEditTitulo.text()
        autor = self.adicionar_livro_page.lineEditAutor.text()
        paginas = self.adicionar_livro_page.lineEditPaginas.text()
        ano = self.adicionar_livro_page.lineEditAno.text()

        data = {'titulo': titulo, 'autor': autor, 'paginas': paginas, 'ano': ano}
        response = requests.post('http://127.0.0.1:8000/insert_book/', json=data)

        if response.status_code == 201:
            print('Livro salvo com sucesso!')
            self.carregar_livros()
        else:
            print(f'Erro ao salvar livro: {response.json()}')

    def carregar_livros(self):
        self.dashboard_page.carregar_livros()

    def abrir_adicionar_livro(self):
        self.adicionar_livro_window = QMainWindow()  # Cria uma nova janela
        self.adicionar_livro_page = AdicionarLivroPage()  # Cria uma nova instância da tela
        # Passa a referência da janela principal (self) e da janela atual (self.adicionar_livro_window)
        self.adicionar_livro_page.setupUi(self.adicionar_livro_window, self)
        self.adicionar_livro_window.show()  # Exibe a janela
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = InitialPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())