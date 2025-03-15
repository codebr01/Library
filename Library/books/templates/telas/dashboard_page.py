from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox
from urllib.parse import urlencode
from PyQt5.QtWidgets import QMainWindow

from books.templates.telas.editar_livro_page import EditarLivroPage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 600)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #D9D9D9;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botaoCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCadastrar.setGeometry(QtCore.QRect(320, 500, 201, 51))
        self.botaoCadastrar.setStyleSheet("QPushButton {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.botaoCadastrar.setObjectName("botaoCadastrar")
        self.botaoVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVoltar.setGeometry(QtCore.QRect(660, 520, 111, 41))
        self.botaoVoltar.setStyleSheet("QPushButton {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.botaoVoltar.setObjectName("botaoVoltar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 431, 51))
        self.label.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEditUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUsuario.setGeometry(QtCore.QRect(300, 130, 371, 41))
        self.lineEditUsuario.setStyleSheet("QLineEdit {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid #5E5A5A;\n"
"}\n"
"")
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.botaoCadastrar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCadastrar_2.setGeometry(QtCore.QRect(160, 130, 121, 41))
        self.botaoCadastrar_2.setStyleSheet("QPushButton {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.botaoCadastrar_2.setObjectName("botaoCadastrar_2")
        self.listaLivros = QtWidgets.QListWidget(self.centralwidget)
        self.listaLivros.setGeometry(QtCore.QRect(170, 180, 501, 291))
        self.listaLivros.setObjectName("listaLivros")
        self.botaoVoltar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVoltar_2.setGeometry(QtCore.QRect(30, 260, 111, 41))
        self.botaoVoltar_2.setStyleSheet("QPushButton {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.botaoVoltar_2.setObjectName("botaoVoltar_2")
        self.botaoVoltar_3 = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVoltar_3.setGeometry(QtCore.QRect(30, 350, 111, 41))
        self.botaoVoltar_3.setStyleSheet("QPushButton {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.botaoVoltar_3.setObjectName("botaoVoltar_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.livro_selecionado_id = None

        # Conectar o sinal itemClicked da lista de livros

        self.listaLivros.itemClicked.connect(self.selecionar_livro)

        self.botaoVoltar_2.clicked.connect(self.abrir_editar_livro)

        self.botaoCadastrar_2.clicked.connect(self.buscar_livros)
        self.botaoVoltar_3.clicked.connect(self.remover_livro)

        self.botaoCadastrar.clicked.connect(self.abrir_tela_cadastrar_livro)
        
        self.carregar_livros()
  

    def selecionar_livro(self, item):
        # Extrair o ID do livro selecionado do texto do item
        texto = item.text()
        self.livro_selecionado_id = texto.split("*ID: ")[1].split("\n")[0]
        print(f"Livro selecionado: ID {self.livro_selecionado_id}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botaoCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.botaoVoltar.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "Seja Bem Vindo ao Library"))
        self.botaoCadastrar_2.setText(_translate("MainWindow", "BUSCAR"))
        self.botaoVoltar_2.setText(_translate("MainWindow", "Editar"))
        self.botaoVoltar_3.setText(_translate("MainWindow", "Remover"))
    

    def carregar_livros(self):
        self.buscar_livros()

        

    def buscar_livros(self):
        autor = self.lineEditUsuario.text()
        params = {}
        if autor:
            params['autor'] = autor
        url = 'http://127.0.0.1:8000/read_books/'
        if params:
            url += '?' + urlencode(params)

        self.listaLivros.clear()
        response = requests.get(url)

        if response.status_code == 200:
            livros = response.json()
            for livro in livros:
                item = QListWidgetItem(f"{15 * '----'}\n*ID: {livro['id']}\n*Title: {livro['titulo']}\n*Author: {livro['autor']}\n*Num Pages: {livro['paginas']}\n*Year: {livro['ano']}\n{15 * '----'}")
                item.setData(QtCore.Qt.UserRole, livro['id'])  # Armazena o ID do livro no item
                self.listaLivros.addItem(item)
        else:
            print(f'Erro ao carregar livros: {response.json()}')
    
    def remover_livro(self):
            if not self.livro_selecionado_id:
                QMessageBox.warning(self.centralwidget, "Aviso", "Nenhum livro selecionado.")
                return
    
            try:
                # Enviar uma requisição DELETE para o servidor Django
                url = f'http://127.0.0.1:8000/delete_book/{self.livro_selecionado_id}/'
                response = requests.delete(url)
    
                if response.status_code == 200:
                    QMessageBox.information(self.centralwidget, "Sucesso", "Livro removido com sucesso!")
                    self.carregar_livros()  # Recarregar a lista de livros
                else:
                    error_message = response.json().get('error', 'Erro desconhecido')
                    QMessageBox.critical(self.centralwidget, "Erro", f"Erro ao remover livro: {error_message}")
            except Exception as e:
                QMessageBox.critical(self.centralwidget, "Erro", f"Erro ao conectar com o servidor: {e}")

    
    def abrir_editar_livro(self):
                if not self.livro_selecionado_id:
                    QMessageBox.warning(self.centralwidget, "Aviso", "Nenhum livro selecionado.")
                    return
        
                # Criar uma nova janela para a tela de edição
                self.editar_livro_window = QMainWindow()
                self.editar_livro_page = EditarLivroPage()
                self.editar_livro_page.setupUi(self.editar_livro_window, self.livro_selecionado_id)
        
                # Carregar os dados do livro na tela de edição
                self.editar_livro_page.carregar_dados_livro()
        
                # Exibir a janela de edição
                self.editar_livro_window.show()

    def abrir_tela_cadastrar_livro(self):
                from books.templates.telas.adicionar_livro_page import AdicionarLivroPage
                self.cadastrar_livro_window = QtWidgets.QMainWindow()
                self.cadastrar_livro_page = AdicionarLivroPage()
                self.cadastrar_livro_page.setupUi(self.cadastrar_livro_window, self.MainWindow) #pass self.MainWindow
                self.cadastrar_livro_window.show()
    

                
