from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox
import requests


class EditarLivroPage(object):
    def setupUi(self, MainWindow, livro_id):
        self.MainWindow = MainWindow

        self.livro_id = livro_id
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #D9D9D9;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 130, 441, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEditTitulo = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditAutor = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditPaginas = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineEditAno = QtWidgets.QLineEdit(self.layoutWidget)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 521, 51))
        self.label.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.botaoVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVoltar.setGeometry(QtCore.QRect(660, 510, 111, 41))
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
        self.botaoSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSalvar.setGeometry(QtCore.QRect(290, 420, 201, 51))
        self.botaoSalvar.setStyleSheet("QPushButton {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.botaoSalvar.setObjectName("botaoSalvar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.botaoSalvar.clicked.connect(self.salvar_alteracoes)
        self.botaoVoltar.clicked.connect(self.voltar_dashboard)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Titulo"))
        self.label_2.setText(_translate("MainWindow", "Autor"))
        self.label_3.setText(_translate("MainWindow", "Páginas"))
        self.label_5.setText(_translate("MainWindow", "Ano"))
        self.label.setText(_translate("MainWindow", "Edite dados do livro"))
        self.botaoVoltar.setText(_translate("MainWindow", "Voltar"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))


    def carregar_dados_livro(self):
        try:
            # Buscar os dados do livro no servidor Django
            url = f'http://127.0.0.1:8000/read_books/{self.livro_id}/'  # Certifique-se de que a rota está correta
            response = requests.get(url)
    
            if response.status_code == 200:
                livro = response.json()
                # Preencher os campos com os dados do livro
                self.lineEditTitulo.setText(livro['titulo'])
                self.lineEditAutor.setText(livro['autor'])
                self.lineEditPaginas.setText(str(livro['paginas']))
                self.lineEditAno.setText(str(livro['ano']))
            else:
                QMessageBox.critical(self.MainWindow, "Erro", f"Erro ao carregar dados do livro: {response.text}")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Erro", f"Erro ao conectar com o servidor: {e}")

    def salvar_alteracoes(self):
            titulo = self.lineEditTitulo.text()
            autor = self.lineEditAutor.text()
            paginas = self.lineEditPaginas.text()
            ano = self.lineEditAno.text()
    
            data = {
                'titulo': titulo,
                'autor': autor,
                'paginas': paginas,
                'ano': ano
            }
    
            try:
                # Enviar os dados atualizados para o servidor Django
                url = f'http://127.0.0.1:8000/update_book/{self.livro_id}/'
                response = requests.put(url, json=data)
    
                if response.status_code == 200:
                    QMessageBox.information(self.MainWindow, "Sucesso", "Livro atualizado com sucesso!")
                    self.voltar_dashboard()
                else:
                    error_message = response.json().get('error', 'Erro desconhecido')
                    QMessageBox.critical(self.MainWindow, "Erro", f"Erro ao atualizar livro: {error_message}")
            except Exception as e:
                QMessageBox.critical(self.MainWindow, "Erro", f"Erro ao conectar com o servidor: {e}")
    def voltar_dashboard(self):
        self.MainWindow.close()