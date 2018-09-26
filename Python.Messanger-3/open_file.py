import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QLabel, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QPixmap, QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.lbl = QLabel(self)


        openFile = QAction(QIcon('open_folder.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Открыть файл')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Файл')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):
        fnames = QFileDialog.getOpenFileName(self, 'Hello')
        fname = fnames[0]
        pixmap = QPixmap(fname)
        self.lbl.resize(640,640)
        self.lbl.setPixmap(pixmap)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())