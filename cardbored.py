from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtWidgets import QApplication,QComboBox,QMessageBox,QFileDialog,QMainWindow,QLabel,QWidget,QHBoxLayout,QVBoxLayout,QPushButton,QLineEdit,QSlider,QTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import re

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,400)

        self.setWindowTitle("Cardbored")
        box=QWidget()
        self.setCentralWidget(box)
        layout=QHBoxLayout(box)
        buttonlayout=QVBoxLayout()

        layout.setContentsMargins(12,12,12,12)

        new=QPushButton('[New file]')
        new.clicked.connect(self.new)

        save=QPushButton('[Save]')
        save.clicked.connect(self.save)

        saveas=QPushButton('[Save as]')
        saveas.clicked.connect(self.savedas)

        fontsize= QComboBox()
        fontsize.addItems(['8','10','14','18','24','32','46','64','72','80','92','100','250','500','750','1000'])
        fontsize.setCurrentText('14')

        about=QPushButton('[About]')
        about.clicked.connect(self.about)
        
        exit=QPushButton('[Exit]')
        exit.clicked.connect(self.exitbtn)


        buttonlayout.setSpacing(4)
        for button in (new,save,saveas,exit,about):
            button.setMinimumSize(140,40)

        self.lineedit = QPlainTextEdit()

        buttonlayout.addWidget(new)
        buttonlayout.addWidget(save)
        buttonlayout.addWidget(saveas)
        buttonlayout.addWidget(about)
        buttonlayout.addWidget(exit)
        buttonlayout.addWidget(fontsize)
        layout.addLayout(buttonlayout)
        layout.addWidget(self.lineedit)
        buttonlayout.setSpacing(12)
        buttonlayout.addStretch()

        self.lineedit.setFont(QFont("Monospace",18))
        self.lineedit.setPlaceholderText("Start typing...(plz)")
        fontsize.currentTextChanged.connect(self.sizechange)
        self.lineedit.textChanged.connect(self.changedw)


    def new(self):
        question = QMessageBox.question(
            self,
            "New file",
            "Are you sure you want to create a new file?\nOld file will not be saved!",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if question == QMessageBox.StandardButton.Yes:
            self.lineedit.setPlainText("")
            self.setWindowTitle("Cardbored")

    def save(self):
        txt= self.lineedit.toPlainText()
        txt=re.sub(r'[!,.";:<>\]]','',txt)
        name = txt[:10].strip()
        with open(f"{name}.txt","w") as file:
            file.write(txt)
        QMessageBox.information(self,"Saved","File saved sucessfully.")

    def exitbtn(self):
        question = QMessageBox.question(
            self,
            "Confirm",
            "Are you sure you want to exit?\nNote will not be saved!",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if question == QMessageBox.StandardButton.Yes:
            self.close()

    def changedw(self):
        self.setWindowTitle("* Cardbored")

    def about(self):
        QMessageBox.information(self,"About","Cardbored (Alpha version)\nA barebones text editor.\n\nGithub: https://github.com/snowballero/cardbored-app")

    def savedas(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Note as: ",
            "",
            "Text Files(*.txt);;All Files (*)"
        )
        if path:
            with open(path,"w",encoding="utf-8") as file:
                file.write(self.lineedit.toPlainText())
            QMessageBox.information(
                self,
                "Saved Sucessfully",
                "File was saved sucessfully"
            )
    
    def sizechange(self,item):
        if item == '8':
            self.lineedit.setFont(QFont("Monospace",8))

        if item == '10':
            self.lineedit.setFont(QFont("Monospace",10))

        if item == '14':
            self.lineedit.setFont(QFont("Monospace",14))

        if item == '18':
            self.lineedit.setFont(QFont("Monospace",18))

        if item == '24':
            self.lineedit.setFont(QFont("Monospace",24))

        if item == '32':
            self.lineedit.setFont(QFont("Monospace",32))

        if item == '46':
            self.lineedit.setFont(QFont("Monospace",46))
        
        if item == '64':
            self.lineedit.setFont(QFont("Monospace",64))

        if item == '72':
            self.lineedit.setFont(QFont("Monospace",72))

        if item == '80':
            self.lineedit.setFont(QFont("Monospace",80))

        if item == '92':
            self.lineedit.setFont(QFont("Monospace",92))

        if item == '100':
            self.lineedit.setFont(QFont("Monospace",100))

        if item == '250':
            self.lineedit.setFont(QFont("Monospace",250))

        if item == '500':
            self.lineedit.setFont(QFont("Monospace",500))

        if item == '750':
            self.lineedit.setFont(QFont("Monospace",750))

        if item == '1000':
            self.lineedit.setFont(QFont("Monospace",1000))
            
STYLE="""
    QMainWindow, QWidget{
        background-color: #1c1d1f;
        color: #d9d9d9;
        font-family: "Monospace";
    }
    QPushButton{
        color: #dbdbdb;
        border-radius:4px;
        background-color: #2b2b2b;
        font-size: 14px;
    }
    QPushButton:hover{
        background-color: #404040;
    }
    QMessageBox QPushButton{
        min-height:35px;
        min-width: 80px;
    }
    QComboBox{
        font-size:15px;
    }
    QComboBox:hover{
        background-color:#303030;
    }
    """


app = QApplication()
app.setStyleSheet(STYLE)
window= Window()
window.show()
app.exec()