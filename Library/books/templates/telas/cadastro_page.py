from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox
import requests

class CadastroPage(object):
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
        self.label.setGeometry(QtCore.QRect(170, 40, 431, 51))
        self.label.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 201, 171, 51))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEditSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSenha.setGeometry(QtCore.QRect(260, 281, 371, 31))
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
        self.lineEditEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(260, 212, 371, 31))
        self.lineEditEmail.setStyleSheet("QLineEdit {\n"
"    background-color: #736F6F;\n"
"    color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid #5E5A5A;\n"
"}\n"
"")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 270, 171, 51))
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 139, 171, 51))
        self.label_4.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEditUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUsuario.setGeometry(QtCore.QRect(260, 150, 371, 31))
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
        self.botaoCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCadastrar.setGeometry(QtCore.QRect(300, 380, 201, 51))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botaoCadastrar.clicked.connect(self.cadastrar_usuario)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Faça seu Cadastro"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Senha"))
        self.label_4.setText(_translate("MainWindow", "Usuário"))
        self.botaoVoltar.setText(_translate("MainWindow", "Voltar"))
        self.botaoCadastrar.setText(_translate("MainWindow", "Cadastrar"))

    def cadastrar_usuario(self):
        email = self.lineEditEmail.text()
        senha = self.lineEditSenha.text()

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
                # URL do Firebase Authentication para cadastro
                url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyCrA-HjV6iqiKvnIqFCqTGRH5GvdgPzYSQ'

                # Enviar a requisição POST para o Firebase
                response = requests.post(url, json=data)

                if response.status_code == 200:
                        QMessageBox.information(self.centralwidget, "Sucesso", "Usuário cadastrado com sucesso!")
                else:
                        error_message = response.json().get('error', {}).get('message', 'Erro desconhecido')
                        QMessageBox.critical(self.centralwidget, "Erro", f"Erro ao cadastrar usuário: {error_message}")
        except Exception as e:
                QMessageBox.critical(self.centralwidget, "Erro", f"Erro ao conectar com o servidor: {e}")
