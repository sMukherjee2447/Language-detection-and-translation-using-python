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

# print('language path list:', langauge_path_list)
language_name_list = []
for path in langauge_path_list:
    base_name = os.path.basename(path)
    base_name = os.path.splitext(base_name)[0]
    language_name_list.append(base_name)

print('Names list:', language_name_list)

font_list = []
font = 2

for font in range(110):
    font+=2
    font_list.append(str(font))

# print('Font List: ', font_list)

all_languages_codes =   {
  	'ab': 'Abkhazian',
  	'abk': 'Abkhazian',
  	'aa': 'Afar',
  	'aar': 'Afar',
  	'af': 'Afrikaans',
  	'afr': 'Afrikaans',
  	'sq': 'Albanian',
  	'alb/sqi*': 'Albanian',
  	'am': 'Amharic',
  	'amh': 'Amharic',
  	'ar': 'Arabic',
  	'ara': 'Arabic',
  	'an': 'Aragonese',
  	'arg': 'Aragonese',
  	'hy': 'Armenian',
  	'arm/hye*': 'Armenian',
  	'as': 'Assamese',
  	'asm': 'Assamese',
  	'ae': 'Avestan',
  	'ave': 'Avestan',
  	'ay': 'Aymara',
  	'aym': 'Aymara',
  	'az': 'Azerbaijani',
  	'aze': 'Azerbaijani',
  	'ba': 'Bashkir',
  	'bak': 'Bashkir',
  	'eu': 'Basque',
  	'baq/eus*': 'Basque',
  	'be': 'Belarusian',
  	'bel': 'Belarusian',
  	'bn': 'Bengali',
  	'ben': 'Bengali',
  	'bh': 'Bihari',
  	'bih': 'Bihari',
  	'bi': 'Bislama',
  	'bis': 'Bislama',
  	'bs': 'Bosnian',
  	'bos': 'Bosnian',
  	'br': 'Breton',
  	'bre': 'Breton',
  	'bg': 'Bulgarian',
  	'bul': 'Bulgarian',
  	'my': 'Burmese',
  	'bur/mya*': 'Burmese',
  	'ca': 'Catalan',
  	'cat': 'Catalan',
  	'ch': 'Chamorro',
  	'cha': 'Chamorro',
  	'ce': 'Chechen',
  	'che': 'Chechen',
  	'zh': 'Chinese',
  	'zh-cn': 'Chinese (Simplified)',
  	'zh-tw': 'Chinese (Traditional)',
  	'chi/zho*': 'Chinese',
  	'cu': 'Church Slavic; Slavonic; Old Bulgarian',
  	'chu': 'Church Slavic; Slavonic; Old Bulgarian',
  	'cv': 'Chuvash',
  	'chv': 'Chuvash',
  	'kw': 'Cornish',
  	'cor': 'Cornish',
  	'co': 'Corsican',
  	'cos': 'Corsican',
  	'hr': 'Croatian',
  	'scr/hrv*': 'Croatian',
  	'cs': 'Czech',
  	'cze/ces*': 'Czech',
  	'da': 'Danish',
  	'dan': 'Danish',
  	'dv': 'Divehi; Dhivehi; Maldivian',
  	'div': 'Divehi; Dhivehi; Maldivian',
  	'nl': 'Dutch',
  	'dut/nld*': 'Dutch',
  	'dz': 'Dzongkha',
  	'dzo': 'Dzongkha',
  	'en': 'English',
  	'eng': 'English',
  	'eo': 'Esperanto',
  	'epo': 'Esperanto',
  	'et': 'Estonian',
  	'est': 'Estonian',
  	'fo': 'Faroese',
  	'fao': 'Faroese',
  	'fj': 'Fijian',
  	'fij': 'Fijian',
  	'fi': 'Finnish',
  	'fin': 'Finnish',
  	'fr': 'French',
  	'fre/fra*': 'French',
  	'gd': 'Gaelic; Scottish Gaelic',
  	'gla': 'Gaelic; Scottish Gaelic',
  	'gl': 'Galician',
  	'glg': 'Galician',
  	'ka': 'Georgian',
  	'geo/kat*': 'Georgian',
  	'de': 'German',
  	'ger/deu*': 'German',
  	'el': 'Greek, Modern (1453-)',
  	'gre/ell*': 'Greek, Modern (1453-)',
  	'gn': 'Guarani',
  	'grn': 'Guarani',
  	'gu': 'Gujarati',
  	'guj': 'Gujarati',
  	'ht': 'Haitian; Haitian Creole',
  	'hat': 'Haitian; Haitian Creole',
  	'ha': 'Hausa',
  	'hau': 'Hausa',
  	'he': 'Hebrew',
  	'heb': 'Hebrew',
  	'hz': 'Herero',
  	'her': 'Herero',
  	'hi': 'Hindi',
  	'hin': 'Hindi',
  	'ho': 'Hiri Motu',
  	'hmo': 'Hiri Motu',
  	'hu': 'Hungarian',
  	'hun': 'Hungarian',
  	'is': 'Icelandic',
  	'ice/isl*': 'Icelandic',
  	'io': 'Ido',
  	'ido': 'Ido',
  	'id': 'Indonesian',
  	'ind': 'Indonesian',
  	'ia': 'Interlingua (International Auxiliary Language Association)',
  	'ina': 'Interlingua (International Auxiliary Language Association)',
  	'ie': 'Interlingue',
  	'ile': 'Interlingue',
  	'iu': 'Inuktitut',
  	'iku': 'Inuktitut',
  	'ik': 'Inupiaq',
  	'ipk': 'Inupiaq',
  	'ga': 'Irish',
  	'gle': 'Irish',
  	'it': 'Italian',
  	'ita': 'Italian',
  	'ja': 'Japanese',
  	'jpn': 'Japanese',
  	'jv': 'Javanese',
  	'jav': 'Javanese',
  	'kl': 'Kalaallisut',
  	'kal': 'Kalaallisut',
  	'kn': 'Kannada',
  	'kan': 'Kannada',
  	'ks': 'Kashmiri',
  	'kas': 'Kashmiri',
  	'kk': 'Kazakh',
  	'kaz': 'Kazakh',
  	'km': 'Khmer',
  	'khm': 'Khmer',
  	'ki': 'Kikuyu; Gikuyu',
  	'kik': 'Kikuyu; Gikuyu',
  	'rw': 'Kinyarwanda',
  	'kin': 'Kinyarwanda',
  	'ky': 'Kirghiz',
  	'kir': 'Kirghiz',
  	'kv': 'Komi',
  	'kom': 'Komi',
  	'ko': 'Korean',
  	'kor': 'Korean',
  	'kj': 'Kuanyama; Kwanyama',
  	'kua': 'Kuanyama; Kwanyama',
  	'ku': 'Kurdish',
  	'kur': 'Kurdish',
  	'lo': 'Lao',
  	'lao': 'Lao',
  	'la': 'Latin',
  	'lat': 'Latin',
  	'lv': 'Latvian',
  	'lav': 'Latvian',
  	'li': 'Limburgan; Limburger; Limburgish',
  	'lim': 'Limburgan; Limburger; Limburgish',
  	'ln': 'Lingala',
  	'lin': 'Lingala',
  	'lt': 'Lithuanian',
  	'lit': 'Lithuanian',
  	'lb': 'Luxembourgish; Letzeburgesch',
  	'ltz': 'Luxembourgish; Letzeburgesch',
  	'mk': 'Macedonian',
  	'mac/mkd*': 'Macedonian',
  	'mg': 'Malagasy',
  	'mlg': 'Malagasy',
  	'ms': 'Malay',
  	'may/msa*': 'Malay',
  	'ml': 'Malayalam',
  	'mal': 'Malayalam',
  	'mt': 'Maltese',
  	'mlt': 'Maltese',
  	'gv': 'Manx',
  	'glv': 'Manx',
  	'mi': 'Maori',
  	'mao/mri*': 'Maori',
  	'mr': 'Marathi',
  	'mar': 'Marathi',
  	'mh': 'Marshallese',
  	'mah': 'Marshallese',
  	'mo': 'Moldavian',
  	'mol': 'Moldavian',
  	'mn': 'Mongolian',
  	'mon': 'Mongolian',
  	'na': 'Nauru',
  	'nau': 'Nauru',
  	'nv': 'Navaho, Navajo',
  	'nav': 'Navaho, Navajo',
  	'nd': 'Ndebele, North',
  	'nde': 'Ndebele, North',
  	'nr': 'Ndebele, South',
  	'nbl': 'Ndebele, South',
  	'ng': 'Ndonga',
  	'ndo': 'Ndonga',
  	'ne': 'Nepali',
  	'nep': 'Nepali',
  	'se': 'Northern Sami',
  	'sme': 'Northern Sami',
  	'no': 'Norwegian',
  	'nor': 'Norwegian',
  	'nb': 'Norwegian Bokmal',
  	'nob': 'Norwegian Bokmal',
  	'nn': 'Norwegian Nynorsk',
  	'nno': 'Norwegian Nynorsk',
  	'ny': 'Nyanja; Chichewa; Chewa',
  	'nya': 'Nyanja; Chichewa; Chewa',
  	'oc': 'Occitan (post 1500); Provencal',
  	'oci': 'Occitan (post 1500); Provencal',
  	'or': 'Oriya',
  	'ori': 'Oriya',
  	'om': 'Oromo',
  	'orm': 'Oromo',
  	'os': 'Ossetian; Ossetic',
  	'oss': 'Ossetian; Ossetic',
  	'pi': 'Pali',
  	'pli': 'Pali',
  	'pa': 'Panjabi',
  	'pan': 'Panjabi',
  	'fa': 'Persian',
  	'per/fas*': 'Persian',
  	'pl': 'Polish',
  	'pol': 'Polish',
  	'pt': 'Portuguese',
  	'por': 'Portuguese',
  	'ps': 'Pushto',
  	'pus': 'Pushto',
  	'qu': 'Quechua',
  	'que': 'Quechua',
  	'rm': 'Raeto-Romance',
  	'roh': 'Raeto-Romance',
  	'ro': 'Romanian',
  	'rum/ron*': 'Romanian',
  	'rn': 'Rundi',
  	'run': 'Rundi',
  	'ru': 'Russian',
  	'rus': 'Russian',
  	'sm': 'Samoan',
  	'smo': 'Samoan',
  	'sg': 'Sango',
  	'sag': 'Sango',
  	'sa': 'Sanskrit',
  	'san': 'Sanskrit',
  	'sc': 'Sardinian',
  	'srd': 'Sardinian',
  	'sr': 'Serbian',
  	'scc/srp*': 'Serbian',
  	'sn': 'Shona',
  	'sna': 'Shona',
  	'ii': 'Sichuan Yi',
  	'iii': 'Sichuan Yi',
  	'sd': 'Sindhi',
  	'snd': 'Sindhi',
  	'si': 'Sinhala; Sinhalese',
  	'sin': 'Sinhala; Sinhalese',
  	'sk': 'Slovak',
  	'slo/slk*': 'Slovak',
  	'sl': 'Slovenian',
  	'slv': 'Slovenian',
  	'so': 'Somali',
  	'som': 'Somali',
  	'st': 'Sotho, Southern',
  	'sot': 'Sotho, Southern',
  	'es': 'Spanish; Castilian',
  	'spa': 'Spanish; Castilian',
  	'su': 'Sundanese',
  	'sun': 'Sundanese',
  	'sw': 'Swahili',
  	'swa': 'Swahili',
  	'ss': 'Swati',
  	'ssw': 'Swati',
  	'sv': 'Swedish',
  	'swe': 'Swedish',
  	'tl': 'Tagalog',
  	'tgl': 'Tagalog',
  	'ty': 'Tahitian',
  	'tah': 'Tahitian',
  	'tg': 'Tajik',
  	'tgk': 'Tajik',
  	'ta': 'Tamil',
  	'tam': 'Tamil',
  	'tt': 'Tatar',
  	'tat': 'Tatar',
  	'te': 'Telugu',
  	'tel': 'Telugu',
  	'th': 'Thai',
  	'tha': 'Thai',
  	'bo': 'Tibetan',
  	'tib/bod*': 'Tibetan',
  	'ti': 'Tigrinya',
  	'tir': 'Tigrinya',
  	'to': 'Tonga (Tonga Islands)',
  	'ton': 'Tonga (Tonga Islands)',
  	'ts': 'Tsonga',
  	'tso': 'Tsonga',
  	'tn': 'Tswana',
  	'tsn': 'Tswana',
  	'tr': 'Turkish',
  	'tur': 'Turkish',
  	'tk': 'Turkmen',
  	'tuk': 'Turkmen',
  	'tw': 'Twi',
  	'twi': 'Twi',
  	'ug': 'Uighur',
  	'uig': 'Uighur',
  	'uk': 'Ukrainian',
  	'ukr': 'Ukrainian',
  	'ur': 'Urdu',
  	'urd': 'Urdu',
  	'uz': 'Uzbek',
  	'uzb': 'Uzbek',
  	'vi': 'Vietnamese',
  	'vie': 'Vietnamese',
  	'vo': 'Volapuk',
  	'vol': 'Volapuk',
  	'wa': 'Walloon',
  	'wln': 'Walloon',
  	'cy': 'Welsh',
  	'wel/cym*': 'Welsh',
  	'fy': 'Western Frisian',
  	'fry': 'Western Frisian',
  	'wo': 'Wolof',
  	'wol': 'Wolof',
  	'xh': 'Xhosa',
  	'xho': 'Xhosa',
  	'yi': 'Yiddish',
  	'yid': 'Yiddish',
  	'yo': 'Yoruba',
  	'yor': 'Yoruba',
  	'za': 'Zhuang; Chuang',
  	'zha': 'Zhuang; Chuang',
  	'zu': 'Zulu',
  	'zul': 'Zulu'
  }

class PyShine_OCR_APP(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('QT_Designer_1.ui',self)
        self.Image = None
        self.language = 'eng'
        self.langu = 'eng'
        self.ui.pushButton.clicked.connect(self.open)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle,self)
        self.ui.label.setMouseTracking(True)
        self.ui.label.installEventFilter(self)
        self.ui.label.setAlignment(PyQt5.QtCore.Qt.AlignTop)
        self.ui.pushButton_3.clicked.connect(self.detect_language)
        self.ui.pushButton_4.clicked.connect(self.translate)
        self.ui.pushButton_2.clicked.connect(self.clear)
        
        # self.ui.toolButton_2.clicked.connect(self.open_file)

        self.comboBox_2.addItems(language_name_list)

        self.comboBox_2.currentIndexChanged['QString'].connect(self.update_now)
        self.comboBox_2.setCurrentIndex(language_name_list.index(self.language))
        
        keys = []
        values = []

        items = all_languages_codes.items()

        for item in items:
            keys.append(item[0]), values.append(item[1])
        self.comboBox_3.addItems(keys)

        self.comboBox_3.currentIndexChanged['QString'].connect(self.update_translation)
        self.comboBox_3.setCurrentIndex(keys.index(self.langu))

        self.font_size = '20'
        self.text = ''
        self.comboBox.addItems(font_list)
        self.comboBox.currentIndexChanged['QString'].connect(self.update_font_size)
        self.comboBox.setCurrentIndex(font_list.index(self.font_size))

        self.ui.textBrowser_2.setFontPointSize(int(self.font_size))
        self.setAcceptDrops(True)

    def update_now(self,value):
        self.language = value
        print("Language selected as: ",self.language)

    def update_translation(self, value):
        self.langu = value
        print("Translation language selected as: ",self.langu)

    def update_font_size(self,value):
        self.font_size = value
        self.ui.textBrowser_2.setFontPointSize(int(self.font_size))
        self.ui.textBrowser_2.setText(str(self.text))

        self.ui.textBrowser.setFontPointSize(int(self.font_size))
        self.ui.textBrowser_3.setFontPointSize(int(self.font_size))

    def clear(self):
        self.ui.textBrowser_2.setText("")
        self.ui.textBrowser.setText("")
        self.ui.textBrowser_3.setText("")


    def open(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')
        self.image = cv2.imread(str(filename[0]))
        frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0], frame.strides[0],QImage.Format_RGB888)
        self.ui.label.setPixmap(QPixmap.fromImage(image))

    def image_to_text(self,crop_cvimage):
        gray = cv2.cvtColor(crop_cvimage,cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray,1)
        crop = Image.fromarray(gray)
        text = pytesseract.image_to_string(crop, lang=self.language)
        print('Text:',text)
        return text

    def detect_language(self,text):
        all_languages_codes =   {
            'ab': 'Abkhazian',
            'abk': 'Abkhazian',
            'aa': 'Afar',
            'aar': 'Afar',
            'af': 'Afrikaans',
            'afr': 'Afrikaans',
            'sq': 'Albanian',
            'alb/sqi*': 'Albanian',
            'am': 'Amharic',
            'amh': 'Amharic',
            'ar': 'Arabic',
            'ara': 'Arabic',
            'an': 'Aragonese',
            'arg': 'Aragonese',
            'hy': 'Armenian',
            'arm/hye*': 'Armenian',
            'as': 'Assamese',
            'asm': 'Assamese',
            'ae': 'Avestan',
            'ave': 'Avestan',
            'ay': 'Aymara',
            'aym': 'Aymara',
            'az': 'Azerbaijani',
            'aze': 'Azerbaijani',
            'ba': 'Bashkir',
            'bak': 'Bashkir',
            'eu': 'Basque',
            'baq/eus*': 'Basque',
            'be': 'Belarusian',
            'bel': 'Belarusian',
            'bn': 'Bengali',
            'ben': 'Bengali',
            'bh': 'Bihari',
            'bih': 'Bihari',
            'bi': 'Bislama',
            'bis': 'Bislama',
            'bs': 'Bosnian',
            'bos': 'Bosnian',
            'br': 'Breton',
            'bre': 'Breton',
            'bg': 'Bulgarian',
            'bul': 'Bulgarian',
            'my': 'Burmese',
            'bur/mya*': 'Burmese',
            'ca': 'Catalan',
            'cat': 'Catalan',
            'ch': 'Chamorro',
            'cha': 'Chamorro',
            'ce': 'Chechen',
            'che': 'Chechen',
            'zh': 'Chinese',
            'zh-cn': 'Chinese (Simplified)',
            'zh-tw': 'Chinese (Traditional)',
            'chi/zho*': 'Chinese',
            'cu': 'Church Slavic; Slavonic; Old Bulgarian',
            'chu': 'Church Slavic; Slavonic; Old Bulgarian',
            'cv': 'Chuvash',
            'chv': 'Chuvash',
            'kw': 'Cornish',
            'cor': 'Cornish',
            'co': 'Corsican',
            'cos': 'Corsican',
            'hr': 'Croatian',
            'scr/hrv*': 'Croatian',
            'cs': 'Czech',
            'cze/ces*': 'Czech',
            'da': 'Danish',
            'dan': 'Danish',
            'dv': 'Divehi; Dhivehi; Maldivian',
            'div': 'Divehi; Dhivehi; Maldivian',
            'nl': 'Dutch',
            'dut/nld*': 'Dutch',
            'dz': 'Dzongkha',
            'dzo': 'Dzongkha',
            'en': 'English',
            'eng': 'English',
            'eo': 'Esperanto',
            'epo': 'Esperanto',
            'et': 'Estonian',
            'est': 'Estonian',
            'fo': 'Faroese',
            'fao': 'Faroese',
            'fj': 'Fijian',
            'fij': 'Fijian',
            'fi': 'Finnish',
            'fin': 'Finnish',
            'fr': 'French',
            'fre/fra*': 'French',
            'gd': 'Gaelic; Scottish Gaelic',
            'gla': 'Gaelic; Scottish Gaelic',
            'gl': 'Galician',
            'glg': 'Galician',
            'ka': 'Georgian',
            'geo/kat*': 'Georgian',
            'de': 'German',
            'ger/deu*': 'German',
            'el': 'Greek, Modern (1453-)',
            'gre/ell*': 'Greek, Modern (1453-)',
            'gn': 'Guarani',
            'grn': 'Guarani',
            'gu': 'Gujarati',
            'guj': 'Gujarati',
            'ht': 'Haitian; Haitian Creole',
            'hat': 'Haitian; Haitian Creole',
            'ha': 'Hausa',
            'hau': 'Hausa',
            'he': 'Hebrew',
            'heb': 'Hebrew',
            'hz': 'Herero',
            'her': 'Herero',
            'hi': 'Hindi',
            'hin': 'Hindi',
            'ho': 'Hiri Motu',
            'hmo': 'Hiri Motu',
            'hu': 'Hungarian',
            'hun': 'Hungarian',
            'is': 'Icelandic',
            'ice/isl*': 'Icelandic',
            'io': 'Ido',
            'ido': 'Ido',
            'id': 'Indonesian',
            'ind': 'Indonesian',
            'ia': 'Interlingua (International Auxiliary Language Association)',
            'ina': 'Interlingua (International Auxiliary Language Association)',
            'ie': 'Interlingue',
            'ile': 'Interlingue',
            'iu': 'Inuktitut',
            'iku': 'Inuktitut',
            'ik': 'Inupiaq',
            'ipk': 'Inupiaq',
            'ga': 'Irish',
            'gle': 'Irish',
            'it': 'Italian',
            'ita': 'Italian',
            'ja': 'Japanese',
            'jpn': 'Japanese',
            'jv': 'Javanese',
            'jav': 'Javanese',
            'kl': 'Kalaallisut',
            'kal': 'Kalaallisut',
            'kn': 'Kannada',
            'kan': 'Kannada',
            'ks': 'Kashmiri',
            'kas': 'Kashmiri',
            'kk': 'Kazakh',
            'kaz': 'Kazakh',
            'km': 'Khmer',
            'khm': 'Khmer',
            'ki': 'Kikuyu; Gikuyu',
            'kik': 'Kikuyu; Gikuyu',
            'rw': 'Kinyarwanda',
            'kin': 'Kinyarwanda',
            'ky': 'Kirghiz',
            'kir': 'Kirghiz',
            'kv': 'Komi',
            'kom': 'Komi',
            'ko': 'Korean',
            'kor': 'Korean',
            'kj': 'Kuanyama; Kwanyama',
            'kua': 'Kuanyama; Kwanyama',
            'ku': 'Kurdish',
            'kur': 'Kurdish',
            'lo': 'Lao',
            'lao': 'Lao',
            'la': 'Latin',
            'lat': 'Latin',
            'lv': 'Latvian',
            'lav': 'Latvian',
            'li': 'Limburgan; Limburger; Limburgish',
            'lim': 'Limburgan; Limburger; Limburgish',
            'ln': 'Lingala',
            'lin': 'Lingala',
            'lt': 'Lithuanian',
            'lit': 'Lithuanian',
            'lb': 'Luxembourgish; Letzeburgesch',
            'ltz': 'Luxembourgish; Letzeburgesch',
            'mk': 'Macedonian',
            'mac/mkd*': 'Macedonian',
            'mg': 'Malagasy',
            'mlg': 'Malagasy',
            'ms': 'Malay',
            'may/msa*': 'Malay',
            'ml': 'Malayalam',
            'mal': 'Malayalam',
            'mt': 'Maltese',
            'mlt': 'Maltese',
            'gv': 'Manx',
            'glv': 'Manx',
            'mi': 'Maori',
            'mao/mri*': 'Maori',
            'mr': 'Marathi',
            'mar': 'Marathi',
            'mh': 'Marshallese',
            'mah': 'Marshallese',
            'mo': 'Moldavian',
            'mol': 'Moldavian',
            'mn': 'Mongolian',
            'mon': 'Mongolian',
            'na': 'Nauru',
            'nau': 'Nauru',
            'nv': 'Navaho, Navajo',
            'nav': 'Navaho, Navajo',
            'nd': 'Ndebele, North',
            'nde': 'Ndebele, North',
            'nr': 'Ndebele, South',
            'nbl': 'Ndebele, South',
            'ng': 'Ndonga',
            'ndo': 'Ndonga',
            'ne': 'Nepali',
            'nep': 'Nepali',
            'se': 'Northern Sami',
            'sme': 'Northern Sami',
            'no': 'Norwegian',
            'nor': 'Norwegian',
            'nb': 'Norwegian Bokmal',
            'nob': 'Norwegian Bokmal',
            'nn': 'Norwegian Nynorsk',
            'nno': 'Norwegian Nynorsk',
            'ny': 'Nyanja; Chichewa; Chewa',
            'nya': 'Nyanja; Chichewa; Chewa',
            'oc': 'Occitan (post 1500); Provencal',
            'oci': 'Occitan (post 1500); Provencal',
            'or': 'Oriya',
            'ori': 'Oriya',
            'om': 'Oromo',
            'orm': 'Oromo',
            'os': 'Ossetian; Ossetic',
            'oss': 'Ossetian; Ossetic',
            'pi': 'Pali',
            'pli': 'Pali',
            'pa': 'Panjabi',
            'pan': 'Panjabi',
            'fa': 'Persian',
            'per/fas*': 'Persian',
            'pl': 'Polish',
            'pol': 'Polish',
            'pt': 'Portuguese',
            'por': 'Portuguese',
            'ps': 'Pushto',
            'pus': 'Pushto',
            'qu': 'Quechua',
            'que': 'Quechua',
            'rm': 'Raeto-Romance',
            'roh': 'Raeto-Romance',
            'ro': 'Romanian',
            'rum/ron*': 'Romanian',
            'rn': 'Rundi',
            'run': 'Rundi',
            'ru': 'Russian',
            'rus': 'Russian',
            'sm': 'Samoan',
            'smo': 'Samoan',
            'sg': 'Sango',
            'sag': 'Sango',
            'sa': 'Sanskrit',
            'san': 'Sanskrit',
            'sc': 'Sardinian',
            'srd': 'Sardinian',
            'sr': 'Serbian',
            'scc/srp*': 'Serbian',
            'sn': 'Shona',
            'sna': 'Shona',
            'ii': 'Sichuan Yi',
            'iii': 'Sichuan Yi',
            'sd': 'Sindhi',
            'snd': 'Sindhi',
            'si': 'Sinhala; Sinhalese',
            'sin': 'Sinhala; Sinhalese',
            'sk': 'Slovak',
            'slo/slk*': 'Slovak',
            'sl': 'Slovenian',
            'slv': 'Slovenian',
            'so': 'Somali',
            'som': 'Somali',
            'st': 'Sotho, Southern',
            'sot': 'Sotho, Southern',
            'es': 'Spanish; Castilian',
            'spa': 'Spanish; Castilian',
            'su': 'Sundanese',
            'sun': 'Sundanese',
            'sw': 'Swahili',
            'swa': 'Swahili',
            'ss': 'Swati',
            'ssw': 'Swati',
            'sv': 'Swedish',
            'swe': 'Swedish',
            'tl': 'Tagalog',
            'tgl': 'Tagalog',
            'ty': 'Tahitian',
            'tah': 'Tahitian',
            'tg': 'Tajik',
            'tgk': 'Tajik',
            'ta': 'Tamil',
            'tam': 'Tamil',
            'tt': 'Tatar',
            'tat': 'Tatar',
            'te': 'Telugu',
            'tel': 'Telugu',
            'th': 'Thai',
            'tha': 'Thai',
            'bo': 'Tibetan',
            'tib/bod*': 'Tibetan',
            'ti': 'Tigrinya',
            'tir': 'Tigrinya',
            'to': 'Tonga (Tonga Islands)',
            'ton': 'Tonga (Tonga Islands)',
            'ts': 'Tsonga',
            'tso': 'Tsonga',
            'tn': 'Tswana',
            'tsn': 'Tswana',
            'tr': 'Turkish',
            'tur': 'Turkish',
            'tk': 'Turkmen',
            'tuk': 'Turkmen',
            'tw': 'Twi',
            'twi': 'Twi',
            'ug': 'Uighur',
            'uig': 'Uighur',
            'uk': 'Ukrainian',
            'ukr': 'Ukrainian',
            'ur': 'Urdu',
            'urd': 'Urdu',
            'uz': 'Uzbek',
            'uzb': 'Uzbek',
            'vi': 'Vietnamese',
            'vie': 'Vietnamese',
            'vo': 'Volapuk',
            'vol': 'Volapuk',
            'wa': 'Walloon',
            'wln': 'Walloon',
            'cy': 'Welsh',
            'wel/cym*': 'Welsh',
            'fy': 'Western Frisian',
            'fry': 'Western Frisian',
            'wo': 'Wolof',
            'wol': 'Wolof',
            'xh': 'Xhosa',
            'xho': 'Xhosa',
            'yi': 'Yiddish',
            'yid': 'Yiddish',
            'yo': 'Yoruba',
            'yor': 'Yoruba',
            'za': 'Zhuang; Chuang',
            'zha': 'Zhuang; Chuang',
            'zu': 'Zulu',
            'zul': 'Zulu'
        }
        detected_lang = detect(self.text)
        print("The ISO639-1 code the detected langauge is:", detected_lang)
        
        lemmatizer_names = ["Language Code", "self.text"]
        format_text = '{:24}' * (len(lemmatizer_names) + 1)
        sentence = [all_languages_codes.get(detected_lang), detected_lang]

        str =" "
        s = str.join(sentence)

        print ("Language for the given text is: ", s)
        self.ui.textBrowser.setText(s)
        return s

    def translate(self, text):
        translator = google_translator() ##initialing the module 
        translated_lang=translator.translate(self.text, lang_tgt = self.langu)
        print("Translated Text-->>",translated_lang)
        self.ui.textBrowser_3.setText(str(translated_lang))

    def open_file(self):
        self.ui = uic.loadUi('help.ui',self)


    def eventFilter(self,source,event):
        width = 0
        height = 0
        if (event.type() == QEvent.MouseButtonPress and source is self.ui.label):
            self.org = self.mapFromGlobal(event.globalPos())
            self.left_top = event.pos()
            self.rubberBand.setGeometry(QRect(self.org,QSize()))
            self.rubberBand.show()
        elif (event.type() == QEvent.MouseMove and source is self.ui.label):
            if self.rubberBand.isVisible():
                self.rubberBand.setGeometry(QRect(self.org,self.mapFromGlobal(event.globalPos())).normalized())
        
        elif(event.type() == QEvent.MouseButtonRelease and source is self.ui.label):
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
                self.ui.textBrowser_2.setText(str(self.text)) 
            else:
                self.rubberBand.hide()
        else:
            return 0
        return QWidget.eventFilter(self,source,event)



app = QtWidgets.QApplication(sys.argv)
mainWindow = PyShine_OCR_APP()
mainWindow.show()
sys.exit(app.exec_())