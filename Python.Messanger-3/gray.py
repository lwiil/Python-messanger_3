from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        image = Image.open("hermione.jpg")
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()


        for i in range(width):
            for j in range(height):
                 r = pix[i, j][0]
                 g = pix[i, j][1]
                 b = pix[i, j][2]
                 S = (r + g + b) // 3
                 # if S > 200:
                 #     S = 255
                 # else:
                 #     S = 0
                 draw.point((i, j), (S, S, S))

        img_tmp = ImageQt(image.convert('RGBA'))

        hbox = QHBoxLayout(self)
        pixmap = QPixmap.fromImage(img_tmp)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Example')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())