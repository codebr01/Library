from PyQt5 import QtCore, QtGui, QtWidgets
from books.templates.telas.cadastro_page import CadastroPage
from books.templates.telas.login_page import LoginPage

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


from books.templates.telas.login_page import LoginPage
from books.templates.telas.cadastro_page import CadastroPage

class InitialPage(object):
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
        self.label.setGeometry(QtCore.QRect(180, 110, 431, 51))
        self.label.setStyleSheet("QLabel {\n"
"    color: #514C4C;\n"
"    font-weight: bold;\n"
"    font-size: 30px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.botaoEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEntrar.setGeometry(QtCore.QRect(290, 240, 201, 51))
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
        self.botaoCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCadastrar.setGeometry(QtCore.QRect(290, 370, 201, 51))
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

        # Conectar os botões às funções de redirecionamento

        self.botaoEntrar.clicked.connect(self.abrir_tela_login)
        self.botaoCadastrar.clicked.connect(self.abrir_tela_cadastro)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Seja Bem Vindo ao Library"))
        self.botaoEntrar.setText(_translate("MainWindow", "ENTRAR"))
        self.botaoCadastrar.setText(_translate("MainWindow", "CADASTRAR"))

    def abrir_tela_login(self):
        
        self.login_window = QtWidgets.QMainWindow()
        self.login_page = LoginPage()
        self.login_page.setupUi(self.login_window)
        
        # Passar a referência da MainWindow para a LoginPage
        self.login_page.MainWindow = self.login_window
    
        # Exibir a tela de login
        self.login_window.show()

    def abrir_tela_cadastro(self):
        
        self.cadastro_window = QMainWindow()
        self.cadastro_page = CadastroPage()
        self.cadastro_page.setupUi(self.cadastro_window)

        # Exibir a tela de cadastro
        self.cadastro_window.show()