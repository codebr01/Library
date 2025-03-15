from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox
import requests

class LoginPage(object):
    def setupUi(self, MainWindow):
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
        self.label.setGeometry(QtCore.QRect(170, 80, 431, 51))
        self.label.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.botaoEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEntrar.setGeometry(QtCore.QRect(300, 390, 201, 51))
        self.botaoEntrar.setStyleSheet("QPushButton {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.botaoEntrar.setObjectName("botaoEntrar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 210, 171, 51))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEditUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUsuario.setGeometry(QtCore.QRect(270, 221, 371, 31))
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 279, 171, 51))
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEditSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSenha.setGeometry(QtCore.QRect(270, 290, 371, 31))
        self.lineEditSenha.setStyleSheet("QLineEdit {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid #5E5A5A;\n"
"}\n"
"")
        self.lineEditSenha.setObjectName("lineEditSenha")
        self.botaoVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVoltar.setGeometry(QtCore.QRect(670, 530, 111, 41))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botaoEntrar.clicked.connect(self.fazer_login)

    def fazer_login(self):
        email = self.lineEditUsuario.text()  # Obtém o email digitado
        senha = self.lineEditSenha.text()    # Obtém a senha digitada

        if not email or not senha:
            QMessageBox.warning(self.centralwidget, "Erro", "Email e senha são obrigatórios.")
            return

        # Dados para enviar ao Firebase Authentication
        data = {
            'email': email,
            'password': senha,
            'returnSecureToken': True
        }

        try:
            # URL do Firebase Authentication para login
            url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCrA-HjV6iqiKvnIqFCqTGRH5GvdgPzYSQ'

            # Enviar a requisição POST para o Firebase
            response = requests.post(url, json=data)

            if response.status_code == 200:
                QMessageBox.information(self.centralwidget, "Sucesso", "Login realizado com sucesso!")
                self.abrir_tela_principal()  # Redireciona para a tela principal
            else:
                error_message = response.json().get('error', {}).get('message', 'Erro desconhecido')
                QMessageBox.critical(self.centralwidget, "Erro", f"Erro ao fazer login: {error_message}")
        except Exception as e:
            QMessageBox.critical(self.centralwidget, "Erro", f"Erro ao conectar com o servidor: {e}")
            

    def abrir_tela_principal(self):
            self.MainWindow.hide()
        
            from books.templates.telas.dashboard_page import Ui_MainWindow as DashboardPage
            self.dashboard_window = QtWidgets.QMainWindow()
            self.dashboard_page = DashboardPage()
            self.dashboard_page.setupUi(self.dashboard_window)
            self.dashboard_page.MainWindow = self.dashboard_window  # Armazena a instância de QMainWindow
            self.dashboard_window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Faça seu Login"))
        self.botaoEntrar.setText(_translate("MainWindow", "ENTRAR"))
        self.label_2.setText(_translate("MainWindow", "Usuário"))
        self.label_3.setText(_translate("MainWindow", "Senha"))
        self.botaoVoltar.setText(_translate("MainWindow", "Voltar"))


