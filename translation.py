import pytesseract
import cv2, os, sys
from PIL import Image
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import glob
from langdetect import detect
from google_trans_new import google_translator ##for language translation

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
langauge_path = 'C:\\Program Files\\Tesseract-OCR\\tessdata\\'
langauge_path_list = glob.glob(langauge_path+"*.traineddata")

language_name_list = []
for path in langauge_path_list:
    base_name = os.path.basename(path)
    base_name = os.path.splitext(base_name)[0]
    language_name_list.append(base_name)


font_list = []
font = 2

for font in range(110):
    font+=2
    font_list.append(str(font))

class OCR(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('translator.ui',self)
        self.Image = None

        self.ui.pushButton_3.clicked.connect(self.open)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle,self)
        self.ui.label_4.setMouseTracking(True)
        self.ui.label_4.installEventFilter(self)
        self.ui.label_4.setAlignment(PyQt5.QtCore.Qt.AlignTop)

        # self.ui.pushButton_4.clicked.connect(self.detect_language)
        # self.ui.pushButton.clicked.connect(self.translate)

        self.language = 'eng'
        self.comboBox.addItems(language_name_list)
        self.comboBox.currentIndexChanged['QString'].connect(self.update_now)
        self.comboBox.setCurrentIndex(language_name_list.index(self.language))

        # self.font_size = '20'
        # self.text = ''
        # self.comboBox_2.addItems(font_list)
        # self.comboBox_2.currentIndexChanged.connect(self.update_font_size)
        # self.comboBox_2.setCurrentIndex(font_list.index(self.font_size))

        # self.ui.textBrowser.setFontPointSize(int(self.font_size))
        self.setAcceptDrops(True)

        def update_now(self,value):
            self.language = value
            print("Language selected as: ",self.language)

        def open(self):
            filename = QFileDialog.getOpenFileName(self, 'Select File')
            self.image = cv2.imread(str(filename[0]))
            frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            image = QImage(frame,frame.shape[1],frame.shape[0], frame.strides[0],QImage.Format_RGB888)
            self.ui.label_4.setPixmap(QPixmap.fromImage(image))

        def image_to_text(self,crop_cvimage):
            gray = cv2.cvtColor(crop_cvimage,cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray,1)
            crop = Image.fromarray(gray)
            text = pytesseract.image_to_string(crop,lang = self.language)
            print('Text:',text)
            return text

        def eventFilter(self,source,event):
            width = 0
            height = 0
            if (event.type() == QEvent.MouseButtonPress and source is self.ui.label_4):
                self.org = self.mapFromGlobal(event.globalPos())
                self.left_top = event.pos()
                self.rubberBand.setGeometry(QRect(self.org,QSize()))
                self.rubberBand.show()
            elif (event.type() == QEvent.MouseMove and source is self.ui.label_4):
                if self.rubberBand.isVisible():
                    self.rubberBand.setGeometry(QRect(self.org,self.mapFromGlobal(event.globalPos())).normalized())
            
            elif(event.type() == QEvent.MouseButtonRelease and source is self.ui.label_4):
                if self.rubberBand.isVisible():
                    self.rubberBand.hide()
                    rect = self.rubberBand.geometry()
                    self.x1 = self.left_top.x()
                    self.y1 = self. left_top.y()
                    width = rect.width()
                    height = rect.height()
                    self.x2 = self.x1+ width
                    self.y2 = self.y1+ height
                if width >=10 and height >= 10  and self.image is not None:
                    self.crop = self.image[self.y1:self.y2, self.x1:self.x2]
                    cv2.imwrite('cropped.png',self.crop)
                    self.text = self.image_to_text(self.crop)
                    self.ui.textBrowser.setText(str(self.text))
                else:
                    self.rubberBand.hide()
            else:
                return 0
            return QWidget.eventFilter(self,source,event)

app = QtWidgets.QApplication(sys.argv)
mainWindow = OCR()
mainWindow.show()
sys.exit(app.exec_())