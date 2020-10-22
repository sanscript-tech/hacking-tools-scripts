# basic modules needed
import zipfile
import argparse
from os import path
import sys
# import PyQt5 modules
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

filename_list = [] 
filename = ""

class MainWindow(qtw.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())
        
        layout1 = qtw.QHBoxLayout()
        label1 = qtw.QLabel("Directory: ")
        self.enter1 = qtw.QLineEdit()
        button1 = qtw.QPushButton("F")

        button1.clicked.connect(self.openfile)

        layout1.addWidget(label1)
        layout1.addWidget(self.enter1)
        layout1.addWidget(button1)

        layout2 = qtw.QHBoxLayout()
        label2 = qtw.QLabel("Save location: ")
        self.enter2 = qtw.QLineEdit()
        button2 = qtw.QPushButton("F")

        button2.clicked.connect(self.savefile)
        
        layout2.addWidget(label2)
        layout2.addWidget(self.enter2)
        layout2.addWidget(button2)

        convert = qtw.QPushButton("convert")
        convert.clicked.connect(self.convert)

        self.layout().addLayout(layout1)
        self.layout().addLayout(layout2)
        self.layout().addWidget(convert)
        self.layout().addWidget(qtw.QPushButton("close",clicked=self.close))
        self.show()

    def openfile(self):
        global filename_list
        filename_list,other = qtw.QFileDialog.getOpenFileUrls()
        text=""
        for i in filename_list:
            text += f"{i.path()},"

        self.enter1.setText(text)

    def savefile(self):
        global filename
        filename,other = qtw.QFileDialog.getSaveFileName()
        self.enter2.setText(filename)

    def convert(self):
        global filename_list,filename
        if filename:
            with zipfile.ZipFile(filename,'w') as myzip:
                for urls in filename_list:
                    myzip.write(urls.path())
            qtw.QMessageBox.information(self,"Success!","Successfully converted")
            self.enter1.clear()
            self.enter2.clear()
        else:
            qtw.QMessageBox.critical(self,"Error","No File Included")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
