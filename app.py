import sys
import os
import typing
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QWidget
from PyQt5.QtCore import QCoreApplication

from frontend.telas.initial_page import InitialPage
from frontend.telas.login_page import LoginPage
from frontend.telas.cadastro_page import CadastroPage

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        
        Main.setObjectName('Main')
        Main.resize(800, 600)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = InitialPage()
        self.tela_login = LoginPage()
        self.tela_cadastro = CadastroPage()

        self.tela_inicial.setupUi(self.stack0)
        self.tela_login.setupUi(self.stack1)
        self.tela_cadastro.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        #Inicial Page
        self.tela_inicial.botaoEntrar.clicked.connect(self.botaoEntrarInitialPage)
        self.tela_inicial.botaoCadastrar.clicked.connect(self.botaoCadastrarInitialPage)

        #Login Page
        self.tela_login.botaoVoltar.clicked.connect(self.botaoVoltarLogin)

        #Castro Page
        self.tela_cadastro.botaoVoltar.clicked.connect(self.botaoVoltarCasdastro)

    def botaoEntrarInitialPage(self):
        self.QtStack.setCurrentIndex(1)

    def botaoCadastrarInitialPage(self):
        self.QtStack.setCurrentIndex(2)

    def botaoVoltarLogin(self):
        self.QtStack.setCurrentIndex(0)

    def botaoVoltarCasdastro(self):
        self.QtStack.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())