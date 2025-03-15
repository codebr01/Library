from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
from PyQt5.QtWidgets import QMessageBox
from requests.exceptions import JSONDecodeError
from json.decoder import JSONDecodeError 

class AdicionarLivroPage(object):
    def setupUi(self, MainWindow, main_window):

        self.MainWindow = MainWindow
        self.main_window = main_window

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #D9D9D9;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 521, 51))
        self.label.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.botaoCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCadastrar.setGeometry(QtCore.QRect(300, 430, 201, 51))
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
        self.botaoVoltar.setGeometry(QtCore.QRect(670, 520, 111, 41))
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 140, 441, 251))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEditTitulo = QtWidgets.QLineEdit(self.widget)
        self.lineEditTitulo.setStyleSheet("QLineEdit {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid #5E5A5A;\n"
"}\n"
"")
        self.lineEditTitulo.setText("")
        self.lineEditTitulo.setObjectName("lineEditTitulo")
        self.gridLayout.addWidget(self.lineEditTitulo, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditAutor = QtWidgets.QLineEdit(self.widget)
        self.lineEditAutor.setStyleSheet("QLineEdit {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid #5E5A5A;\n"
"}\n"
"")
        self.lineEditAutor.setText("")
        self.lineEditAutor.setObjectName("lineEditAutor")
        self.gridLayout.addWidget(self.lineEditAutor, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditPaginas = QtWidgets.QLineEdit(self.widget)
        self.lineEditPaginas.setStyleSheet("QLineEdit {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid #5E5A5A;\n"
"}\n"
"")
        self.lineEditPaginas.setText("")
        self.lineEditPaginas.setObjectName("lineEditPaginas")
        self.gridLayout.addWidget(self.lineEditPaginas, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineEditAno = QtWidgets.QLineEdit(self.widget)
        self.lineEditAno.setStyleSheet("QLineEdit {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid #5E5A5A;\n"
"}\n"
"")
        self.lineEditAno.setText("")
        self.lineEditAno.setObjectName("lineEditAno")
        self.gridLayout.addWidget(self.lineEditAno, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botaoCadastrar.clicked.connect(self.cadastrar_livro)
        self.botaoVoltar.clicked.connect(self.voltar_dashboard) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Adicione um novo livro ao Library"))
        self.botaoCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.botaoVoltar.setText(_translate("MainWindow", "Voltar"))
        self.label_4.setText(_translate("MainWindow", "Titulo"))
        self.label_2.setText(_translate("MainWindow", "Autor"))
        self.label_3.setText(_translate("MainWindow", "Páginas"))
        self.label_5.setText(_translate("MainWindow", "Ano"))

    def cadastrar_livro(self):
        titulo = self.lineEditTitulo.text()
        autor = self.lineEditAutor.text()
        paginas = self.lineEditPaginas.text()
        ano = self.lineEditAno.text()

        data = {'titulo': titulo, 'autor': autor, 'paginas': paginas, 'ano': ano}
        try:
            # Obter o token CSRF do cookie
            session = requests.Session()
            session.get('http://127.0.0.1:8000/insert_book/')  # Faz uma requisição GET inicial para obter o cookie
            csrftoken = session.cookies.get('csrftoken')

            headers = {'X-CSRFToken': csrftoken} if csrftoken else {} # Adiciona o token ao header se existir.

            response = session.post('http://127.0.0.1:8000/insert_book/', json=data, headers=headers)

            if response.status_code == 201:
                QMessageBox.information(None, 'Sucesso', 'Livro cadastrado com sucesso!')
                self.lineEditTitulo.clear()
                self.lineEditAutor.clear()
                self.lineEditPaginas.clear()
                self.lineEditAno.clear()
            else:
                try:
                    error_message = response.json()
                except JSONDecodeError:
                    error_message = response.text
                QMessageBox.critical(None, 'Erro', f'Erro ao cadastrar livro: {error_message}')

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, 'Erro de Rede', f'Erro ao conectar com o servidor: {e}')

    def voltar_dashboard(self):
            self.main_window.show()
            self.MainWindow.close()  