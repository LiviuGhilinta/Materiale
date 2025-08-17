import sys
import random
import tkinter as tk
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout,QLineEdit,QHBoxLayout,QProgressBar
from PyQt5.QtCore import QTimer,QTime, Qt,pyqtSignal,QSize
from PyQt5.QtGui import QFont,QFontDatabase,QPixmap,QIcon,QPainter,QColor,QPen


class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alegeti tipul masinii")
        self.masina_mica = QPushButton(self)
        self.masina_mare = QPushButton(self)
        self.label1 = QLabel("Alegeti tipul masinii!",self)
        self.label2 = QLabel(self)
        self.xbutton = QPushButton("x",self)
        self.initUI()

    def initUI(self):
        image = QPixmap("Imagine_Fundal.png")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(370,350)
        self.label2.setPixmap(image)
        self.label2.setScaledContents(True)
        self.label2.setGeometry(0,0,370,350)
        hbox = QHBoxLayout()
        hbox.addWidget(self.masina_mica)
        hbox.addWidget(self.masina_mare)
        hbox.addWidget(self.xbutton)
        self.xbutton.setGeometry(330,10,30,30)
        self.xbutton.setStyleSheet("font-size: 30px;"
                                   "font-weight : bold;" \
                                   "font-size : 25px;"
                                   "background-color : transparent")
        self.xbutton.clicked.connect(self.close)
        hbox.setAlignment(Qt.AlignCenter)
        
        self.label1.setGeometry(60,60,270,30)
        self.label1.setStyleSheet("font-size:25px;" \
                                  "font-family : Congenial;" \
                                  "color : white;"
                                  "font-weight : bold;" 
                                )
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.raise_()

        self.masina_mare.setGeometry(208,125,150,150)
        self.masina_mica.setGeometry(33,125,150,150)
        self.masina_mica.setIcon((QIcon('Mmic.png')))
        self.masina_mica.setIconSize(QSize(144,145))
        self.masina_mica.setStyleSheet("text-align : top center;" \
                                       "padding : 10;" \
                                       )
        self.masina_mica.raise_()
        self.masina_mare.raise_()    

        self.masina_mare.setIcon((QIcon('Mmare.png')))
        self.masina_mare.setIconSize(QSize(144,145))
        self.masina_mare.setStyleSheet("text-align : top center;" \
                                       "padding : 10 px;" \
                                      )        
        

        self.masina_mica.clicked.connect(self.masinam)
        self.masina_mare.clicked.connect(self.masinama)
        self.new_window = None
    def masinam(self):
        if self.new_window is None:
            self.new_window = SelfWash_Masini_Mici() 
        self.new_window.show()
        self.close()
    def masinama(self):
        if self.new_window is None:
            self.new_window = SelfWash_Masini_Mari()
        self.new_window.show()
        self.close()    


class SecondScreen(QWidget):
    timpTrimis = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Introduceti suma")
        self.line_edit = QLineEdit(self)
        self.ok_button = QPushButton("Ok",self)
        self.Introduceti = QLabel("Introduceti Suma!",self)
        self.label = QLabel(self)
        self.fundal = QLabel(self)    
        self.initUI()

    def initUI(self):
        self.setFixedSize(450,200)
        pixmap =QPixmap("Imagine_Fundal2.png")
        self.fundal.setPixmap(pixmap)
        self.fundal.setScaledContents(True)
        self.fundal.setGeometry(0,0,450,200)
        self.setGeometry(635,450,450,200)
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.Introduceti)
        vbox2.addWidget(self.line_edit)
        vbox2.addWidget(self.label)
        self.Introduceti.raise_()
        self.line_edit.raise_()
        self.label.raise_()
        self.ok_button.raise_()
        self.Introduceti.setGeometry(170,70,300,30)
        self.line_edit.setGeometry(70,100,300,30)
        self.line_edit.setAlignment(Qt.AlignCenter)
        hbox = QHBoxLayout()
        hbox.addWidget(self.ok_button)
        self.line_edit.setAlignment
        self.ok_button.setGeometry(370,100,55,30)      

        self.Introduceti.setStyleSheet("font-size:20px")   
        self.line_edit.setStyleSheet("font-size: 20px")
        self.ok_button.setStyleSheet("font-size:20px")
        
        self.label.setGeometry(90,120,300,50)
        self.label.setStyleSheet("font-size:20px;")
        self.label.raise_()        

        self.ok_button.clicked.connect(self.go_back)    
        self.back = None
    def go_back(self):
        try:
            self.bani = int(self.line_edit.text())
            if self.bani < 0:
                self.label.setText("N-am auzit de bancnote negative!")
                return    
        except ValueError:
            self.label.setText("Introduceti doar Bancnote!")
            return   
        self.timp = self.bani * 40
        self.timpTrimis.emit(self.timp)
        print(self.timp)
        self.close()  
        
        


class SelfWash_Masini_Mici(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00",self)
        self.fundal = QLabel(self)
        self.introduceti_suma = QPushButton("Suma",self)
        self.apa = QPushButton("Apa",self)
        self.spuma = QPushButton("Spuma",self)
        self.ceara = QPushButton("Ceara",self)
        self.osmozata = QPushButton("Apa_Osmozata",self)
        self.stop = QPushButton("Stop",self)
        self.timer = QTimer(self)
        self.program = QLabel("Info : Bine ati venit! ",self)
        self.program_prestabilit = QPushButton("Program Prestabilit",self)
        self.xbutton =QPushButton("Close",self)
        self.Info = QPushButton("Apasa-ma",self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SelfWash")
        self.setGeometry(600,5,30,30)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(700,1020)
        pixmap = QPixmap("Imagine_Fundal2.png")
        self.fundal.setPixmap(pixmap)
        self.fundal.setScaledContents(True)
        self.fundal.setGeometry(0,0,700,1020)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setGeometry(600,100,200,200)
        vbox.addWidget(self.program)
        vbox.addWidget(self.introduceti_suma)
        vbox.addWidget(self.program_prestabilit)        
        vbox.addWidget(self.apa)
        vbox.addWidget(self.spuma)
        vbox.addWidget(self.ceara)
        vbox.addWidget(self.osmozata)
        vbox.addWidget(self.stop)
        vbox.addWidget(self.Info)
        vbox.addWidget(self.xbutton)
        
        self.time_label.raise_()
        self.program.raise_()
        self.introduceti_suma.raise_()
        self.apa.raise_()
        self.ceara.raise_()
        self.osmozata.raise_()
        self.stop.raise_()
        self.program_prestabilit.raise_()
        self.Info.raise_()

        
        self.xbutton.setStyleSheet("background-color :  #fa1c0c;" \
                                    "font-weight : bold;"
                                    "border : 3px solid;"
                                    "border-color : black;"
                                     "padding : 5 "  \
                                    )
        self.Info.setStyleSheet("background-color : green;" \
                                "font-family : Calibri;" \
                                "font-size: 20px;" \
                                "font-weight : bold;"
                                "padding : 10;"
                                "border : 3px solid;" \
                                "border-color : black;"
                                )
        self.program.setStyleSheet("background-color :transparent ;"
                                   "color : black;"
                                   "font-size : 20px;"
                                   "font-weight : bold;")
        self.stop.setStyleSheet("background-color : red ")
        self.setStyleSheet(
            '''
            QPushButton{
                        font-size : 20px;
                        padding : 30px;
                        font-family : calibri;
                        background-color : #94ffd8;
                        border : 1px solid;
                        border-radius : 15px;
                        font-weight : bold;
            }
            QLabel {
                        background-color : black;
                        color : red;
                        border-radius :30px;
                        
            }
            '''
        )
    
        font_id = QFontDatabase.addApplicationFont("Seven-Segment.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.update_display)

        self.introduceti_suma.setDisabled(True)
        self.program_prestabilit.setDisabled(True)
        self.apa.setDisabled(True)
        self.spuma.setDisabled(True)
        self.ceara.setDisabled(True)
        self.osmozata.setDisabled(True)
        self.stop.setDisabled(True)

        self.introduceti_suma.clicked.connect(self.open_new_window)
        self.new_window = None
        self.program_prestabilit.clicked.connect(self.open_prestabilit)
        self.apa.clicked.connect(self.spalare_apa)
        self.spuma.clicked.connect(self.spuma_)
        self.ceara.clicked.connect(self.ceara_)
        self.osmozata.clicked.connect(self.apa_osm)
        self.stop.clicked.connect(self.oprire)
        self.xbutton.clicked.connect(sys.exit)
        self.Info.clicked.connect(self.Infos)

    def Infos(self):
        self.Info.setText("Info")
        self.introduceti_suma.setDisabled(False)
        self.program_prestabilit.setDisabled(False)
        self.apa.setDisabled(False)
        self.spuma.setDisabled(False)
        self.ceara.setDisabled(False)
        self.osmozata.setDisabled(False)
        self.stop.setDisabled(False)
        self.newwindow = Info_Programe()
        self.newwindow.show()

    def open_new_window(self):
        if self.new_window is None:
            self.new_window = SecondScreen()
            self.new_window.timpTrimis.connect(self.update_time)
        self.new_window.show()
    def update_time(self,timp):
        self.seconds = int(timp%60)
        self.minutes = int(timp/60)
        self.hours = int(timp/3600)
        self.time_label.setText(f"{str(self.minutes)}:{str(self.seconds)}")
        print(f"{self.hours},{self.minutes},{self.seconds}")
        self.time = QTime(self.hours,self.minutes,self.seconds)
        if timp:
            self.program.setText("Info : Alegeti un program")
        

        self.program_prestabilit = None
        self.Info = None
    def open_prestabilit(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                return
            else:
                if self.minutes >=6 and self.seconds >= 40:
                    if self.program_prestabilit is None:
                        self.program_prestabilit = Program_Prestabilit()
                        self.opennewwindow = Info_Prestabilit()
                    self.program_prestabilit.show()
                    self.opennewwindow.show()
                else:
                    self.program.setText("Pentru programul prestabilit trebuie sa introduceti minim 10 RON!")
                    return    
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;"
                                       "font-weight : bold;")        

    def spalare_apa(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                return
            else:
                self.introduceti_suma.setDisabled(True)
                self.timer.start(1000)
                self.program.setText("Info:Programul selectat : Apa cu Presiune!")
                self.program.setStyleSheet("color : black;" \
                                            "background-color : transparent;" \
                                            "font-size:20px;"
                                            "font-weight : bold;")
                
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;"
                                       "font-weight : bold;")
    def spuma_(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                self.introduceti_suma.setDisabled(False)
                return
            else:
                self.introduceti_suma.setDisabled(True)
                self.timer.start(1000)
                self.program.setText("Info:Programul selectat : Spuma!")
                self.program.setStyleSheet("color : black;" \
                                            "background-color : transparent;" \
                                            "font-size:20px;"
                                            "font-weight : bold;")
                
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;"
                                       "font-weight : bold;")

    def ceara_(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                self.introduceti_suma.setDisabled(False)
                return
            else:
                self.introduceti_suma.setDisabled(True)
                self.timer.start(1000)
                self.program.setText("Info:Programul selectat : Ceara!")
                self.program.setStyleSheet("color : black;" \
                                            "background-color : transparent;" \
                                            "font-size:20px;"
                                            "font-weight : bold;")
                
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;")

    def apa_osm(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                self.introduceti_suma.setDisabled(False)
                return
            else:
                self.introduceti_suma.setDisabled(True)
                self.timer.start(1000)
                self.program.setText("Info:Programul selectat : Apa Osmozata!")
                self.program.setStyleSheet("color : black;" \
                                            "background-color : transparent;" \
                                            "font-size:20px;"
                                            "font-weight : bold;")
                
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;"
                                       "font-weight : bold;"
                                       )
        

    def oprire(self):
        self.timer.stop()
        time.sleep(3)
        self.timer.start(1000)    

    
    def format_time(self,time):
        self.minutes = time.minute()
        self.seconds = time.second()
        print(self.minutes,self.seconds)
        return f"{self.minutes:02}:{self.seconds : 02}"

    def update_display(self):
        if self.time.minute() == 0 and self.time.second() == 0 and self.time.hour() == 0:
            self.timer.stop()
            self.time_label.setText("00:00")
            self.program.setText("Info : Bine ati venit")
            self.newwindow2 = Finish()
            self.newwindow2.show()
            self.introduceti_suma.setDisabled(False)
        else:    
            self.time = self.time.addSecs(-1)
            self.time_label.setText(self.format_time(self.time))    
     
class Finish(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel("Programul s-a incheiat! Va multumim!",self)
        self.setFixedSize(350,50)
        self.setWindowTitle("Inchide-ma!!")
        self.setStyleSheet("background-color : #f9f6c2;")
        self.label1.setStyleSheet("font-size: 20px;")
                            


class SelfWash_Masini_Mari(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00",self)
        self.fundal = QLabel(self)
        self.introduceti_suma = QPushButton("Suma",self)
        self.apa = QPushButton("Apa",self)
        self.spuma = QPushButton("Spuma",self)
        self.ceara = QPushButton("Ceara",self)
        self.osmozata = QPushButton("Apa_Osmozata",self)
        self.stop = QPushButton("Stop",self)
        self.timer = QTimer(self)
        self.program = QLabel("Info : Bine ati venit! ",self)
        self.program_prestabilit = QPushButton("Program Prestabilit",self)
        self.xbutton =QPushButton("Close",self)
        self.Info = QPushButton("Apasa-ma",self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SelfWash")
        self.setGeometry(600,5,30,30)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(700,1020)
        pixmap = QPixmap("Imagine_Fundal2.png")
        self.fundal.setPixmap(pixmap)
        self.fundal.setScaledContents(True)
        self.fundal.setGeometry(0,0,700,1020)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setGeometry(600,100,200,200)
        vbox.addWidget(self.program)
        vbox.addWidget(self.introduceti_suma)
        vbox.addWidget(self.program_prestabilit)        
        vbox.addWidget(self.apa)
        vbox.addWidget(self.spuma)
        vbox.addWidget(self.ceara)
        vbox.addWidget(self.osmozata)
        vbox.addWidget(self.stop)
        vbox.addWidget(self.Info)
        vbox.addWidget(self.xbutton)
        
        self.time_label.raise_()
        self.program.raise_()
        self.introduceti_suma.raise_()
        self.apa.raise_()
        self.ceara.raise_()
        self.osmozata.raise_()
        self.stop.raise_()
        self.program_prestabilit.raise_()
        self.Info.raise_()

        
        self.xbutton.setStyleSheet("background-color :  #fa1c0c;" \
                                    "font-weight : bold;"
                                    "border : 3px solid;"
                                    "border-color : black;"
                                     "padding : 5 "  \
                                    )
        self.Info.setStyleSheet("background-color : green;" \
                                "font-family : Calibri;" \
                                "font-size: 20px;" \
                                "font-weight : bold;"
                                "padding : 10;"
                                "border : 3px solid;" \
                                "border-color : black;"
                                )
        self.program.setStyleSheet("background-color :transparent ;"
                                   "color : black;"
                                   "font-size : 20px;"
                                   "font-weight : bold;")
        self.stop.setStyleSheet("background-color : red ")
        self.setStyleSheet(
            '''
            QPushButton{
                        font-size : 20px;
                        padding : 30px;
                        font-family : calibri;
                        background-color : #94ffd8;
                        border : 1px solid;
                        border-radius : 15px;
                        font-weight : bold;
            }
            QLabel {
                        background-color : black;
                        color : red;
                        border-radius :30px;
                        
            }
            '''
        )
    
        font_id = QFontDatabase.addApplicationFont("Seven-Segment.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.update_display)

        self.introduceti_suma.setDisabled(True)
        self.program_prestabilit.setDisabled(True)
        self.apa.setDisabled(True)
        self.spuma.setDisabled(True)
        self.ceara.setDisabled(True)
        self.osmozata.setDisabled(True)
        self.stop.setDisabled(True)

        self.introduceti_suma.clicked.connect(self.open_new_window)
        self.new_window = None
        self.program_prestabilit.clicked.connect(self.open_prestabilit)
        self.apa.clicked.connect(self.spalare_apa)
        self.spuma.clicked.connect(self.spuma_)
        self.ceara.clicked.connect(self.ceara_)
        self.osmozata.clicked.connect(self.apa_osm)
        self.stop.clicked.connect(self.oprire)
        self.xbutton.clicked.connect(sys.exit)
        self.Info.clicked.connect(self.Infos)

    def Infos(self):
        self.Info.setText("Info")
        self.introduceti_suma.setDisabled(False)
        self.program_prestabilit.setDisabled(False)
        self.apa.setDisabled(False)
        self.spuma.setDisabled(False)
        self.ceara.setDisabled(False)
        self.osmozata.setDisabled(False)
        self.stop.setDisabled(False)
        self.newwindow = Info_Programe()
        self.newwindow.show()

    def open_new_window(self):
        if self.new_window is None:
            self.new_window = SecondScreen()
            self.new_window.timpTrimis.connect(self.update_time)
        self.new_window.show()
    def update_time(self,timp):
        self.seconds = int(timp%60)
        self.minutes = int(timp/60)
        self.hours = int(timp/3600)
        self.time_label.setText(f"{str(self.minutes)}:{str(self.seconds)}")
        print(f"{self.hours},{self.minutes},{self.seconds}")
        self.time = QTime(self.hours,self.minutes,self.seconds)
        if timp:
            self.program.setText("Info : Alegeti un program")
        

        self.program_prestabilit = None
        self.Info = None
    def open_prestabilit(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                return
            else:
                if self.minutes >=6 and self.seconds >= 40:
                    if self.program_prestabilit is None:
                        self.program_prestabilit = Program_Prestabilit()
                        self.opennewwindow = Info_Prestabilit()
                    self.program_prestabilit.show()
                    self.opennewwindow.show()
                else:
                    self.program.setText("Pentru programul prestabilit trebuie sa introduceti minim 10 RON!")
                    return    
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;"
                                       "font-weight : bold;")        

    def spalare_apa(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                return
            else:
                self.introduceti_suma.setDisabled(True)
                self.timer.start(1000)
                self.program.setText("Info:Programul selectat : Apa cu Presiune!")
                self.program.setStyleSheet("color : black;" \
                                            "background-color : transparent;" \
                                            "font-size:20px;"
                                            "font-weight : bold;")
                
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;"
                                       "font-weight : bold;")
    def spuma_(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                self.introduceti_suma.setDisabled(False)
                return
            else:
                self.introduceti_suma.setDisabled(True)
                self.timer.start(1000)
                self.program.setText("Info:Programul selectat : Spuma!")
                self.program.setStyleSheet("color : black;" \
                                            "background-color : transparent;" \
                                            "font-size:20px;"
                                            "font-weight : bold;")
                
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;"
                                       "font-weight : bold;")

    def ceara_(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                self.introduceti_suma.setDisabled(False)
                return
            else:
                self.introduceti_suma.setDisabled(True)
                self.timer.start(1000)
                self.program.setText("Info:Programul selectat : Ceara!")
                self.program.setStyleSheet("color : black;" \
                                            "background-color : transparent;" \
                                            "font-size:20px;"
                                            "font-weight : bold;")
                
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;")

    def apa_osm(self):
        try:
            if self.seconds <1 and self.minutes<1 and self.hours<1 :
                self.introduceti_suma.setDisabled(False)
                return
            else:
                self.introduceti_suma.setDisabled(True)
                self.timer.start(1000)
                self.program.setText("Info:Programul selectat : Apa Osmozata!")
                self.program.setStyleSheet("color : black;" \
                                            "background-color : transparent;" \
                                            "font-size:20px;"
                                            "font-weight : bold;")
                
        except AttributeError:
            self.program.setText("Info : Mai intai introduceti suma de bani!")
            self.program.setStyleSheet("color : red;" \
                                       "background-color : transparent;"
                                       "font-size : 20px;"
                                       "font-weight : bold;"
                                       )
        

    def oprire(self):
        self.timer.stop()
        time.sleep(3)
        self.timer.start(1000)    

    
    def format_time(self,time):
        self.minutes = time.minute()
        self.seconds = time.second()
        print(self.minutes,self.seconds)
        return f"{self.minutes:02}:{self.seconds : 02}"

    def update_display(self):
        if self.time.minute() == 0 and self.time.second() == 0 and self.time.hour() == 0:
            self.timer.stop()
            self.time_label.setText("00:00")
            self.program.setText("Info : Bine ati venit")
            self.newwindow2 = Finish()
            self.newwindow2.show()
            self.introduceti_suma.setDisabled(False)
        else:    
            self.time = self.time.addSecs(-1)
            self.time_label.setText(self.format_time(self.time))    

class Info_Programe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Informatii")

        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        
        self.fillColor = QColor("#f9f6c2")  
        self.penColor = QColor("#000000")

        
        self.close_btn = QPushButton("x", self)
        font = QFont()
        font.setPixelSize(18)
        font.setBold(True)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("background-color: rgba(0,0,0,0); color: black;")
        self.close_btn.setFixedSize(30, 30)
        self.close_btn.clicked.connect(self.close)


        

        
        self.label1 = QLabel("Informatii legate de utilizarea Spalatoriei noastre!")
        self.label2 = QLabel("""Timer-ul va afisa timpul pe care il 
aveti la dispozitie pentru spalarea masinii!""")
        self.label3 = QLabel("""Info ℹ️ = Aici vor aparea informatiile legate de ceea ce trebuie 
sa faceti dumneavoastra, respectiv programul de spalare in 
care va aflati!""")
        self.label4 = QLabel("""Intorduceti suma = Pentru a introduce suma de bani 💰 apasati 
acest buton(1 RON = 40s timp pentru spalare)""")
        self.label5 = QLabel("""Program prestabilit = Va recomandam acest program
(Suma min. 10 RON), 
daca doriti sa va relaxati si masina dvs. sa fie spalata de catre 
noua noastra tehnologie,sa apasati butonul""")
        self.label6 = QLabel("""Apa = Acest program va pune la dispozitie Apa cu Presiune 🚿 
pentru a da murdaria/spuma jos de pe masina!""")
        self.label7 = QLabel("""Spuma = Acest program va pune la dispozitie Spuma Frisca 🧼 
pentru a ii oferi masinii dvs o spalare ca la carte!""")
        self.label8 = QLabel("""Ceara = ✨✨Acest program va pune la dispozitie Ceara
pentru a va face masina sa luceasca la fel cum a fost in prima zi✨✨! """)
        self.label9 = QLabel("""Osmozata = Acest program va pune la dispozitie Apa Osmozata 
pentru a face o clatire fara pete!""")
        self.label10 = QLabel("""Stop = ⏸ Acest buton va permite sa opriti timpul pentru 
15 secunde, dupa timer-ul incepe din nou numaratoarea!""")
        self.label11 = QLabel("""Close = Acest buton va permite sa iesiti din aceasta fereasta! """)
        

        self.setStyleSheet("""
                            QLabel {
                                font-family: Calibri;
                                font-size: 20px;
                                font-weight: bold;
                                padding : 2;
                                 }
                                            """)
        

        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(20, 50, 20, 20) 
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)
        vbox.addWidget(self.label5)
        vbox.addWidget(self.label6)
        vbox.addWidget(self.label7)
        vbox.addWidget(self.label8)
        vbox.addWidget(self.label9)
        vbox.addWidget(self.label10)
        vbox.addWidget(self.label11)
        
        

        self.setFixedSize(600,1000)
        #self.setGeometry(0,20,400,1000)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.fillColor)
        painter.setPen(QPen(self.penColor, 1))
        painter.drawRoundedRect(self.rect(), 10, 10)

    def resizeEvent(self, event):
        self.close_btn.move(self.width() - self.close_btn.width() - 5, 5)
        super().resizeEvent(event)



class Program_Prestabilit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program prestabilit")
        self.xbutton = QPushButton("x",self)
        self.label1 = QLabel("Bine ati venit!",self)
        self.label2 = QLabel("""Pentru ca ati asigurat vehiculul pe pozitie, programul va incepe. 
Va rugam sa va indepartati de vehicul si sa asteptati!""",self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.fundal = QLabel(self)
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
        self.scan = QPushButton("Scan",self)
        self.start_button = QPushButton("Start",self)
        self.StatusSpalare = QProgressBar(self)
        self.grad_de_murdarie = random.randint(5,100)
        self.initUI()

    def initUI(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(800,600)
        pixmap =QPixmap("Imagine_Fundal2.png")
        self.fundal.setPixmap(pixmap)
        self.fundal.setScaledContents(True)
        self.fundal.setGeometry(0,0,800,600)
        vbox = QVBoxLayout()
        vbox.addWidget(self.xbutton)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.StatusSpalare)
        vbox.addWidget(self.scan)
        self.StatusSpalare.setMinimum(0)
        self.StatusSpalare.setMaximum(self.grad_de_murdarie)

        self.label1.setGeometry(0,40,800,25)
        self.label2.setGeometry(0,70,800,50)
        self.label3.setGeometry(0,300,800,30)
        self.label4.setGeometry(0,150,800,20)
        self.label4.setText(f"Autovehiculul dumneavoastra este {self.grad_de_murdarie}% murdar! ")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label4.setAlignment(Qt.AlignCenter)

        self.xbutton.setGeometry(740,10,30,30)
        
        self.start_button.setGeometry(350,400,100,50)
        self.start_button.hide()
        self.label4.hide()

        self.scan.setGeometry(350,400,100,50)
        
        self.StatusSpalare.setGeometry(270, 400, 300, 25)
        self.StatusSpalare.hide()
        
        self.xbutton.clicked.connect(self.close)
        self.scan.clicked.connect(self.scanare)
        self.start_button.clicked.connect(self.timer1_start)

        self.label1.raise_()
        self.label2.raise_()
        self.label3.raise_()
        self.label4.raise_()
        self.scan.raise_()
        self.start_button.raise_()
        self.StatusSpalare.raise_() 
        self.xbutton.raise_()


        self.setStyleSheet(""" 
                            QLabel {
                                    font-size:20px;
                                    font-family : Calibri;
                                    font-weight : bold;
                                        }
                            QPushButton
                                    {
                                    background-color : #c7c5c5;
                                    font-size:20 px;
                                    font-family : Calibri;
                                    border : 1px solid;
                                    border-radius : 15px;
                                    font-weight : bold;
                                    }
                            """)

        self.xbutton.setStyleSheet("background-color : red")
        self.count = 3  


    def scanare(self):
        self.label4.show()
        self.scan.hide()
        self.start_button.show()
            
    def timer1_start(self):
        self.start_button.setDisabled(True)
        self.start_button.deleteLater()
        self.timer1.timeout.connect(self.update_countdown)
        self.timer1.start(1000)  

    def update_countdown(self):
        if self.count > -1:
            self.label3.setText(f"Programul incepe in: {self.count}")
            self.count -= 1
        elif self.count == -1:
            self.label3.setText("")
            self.timer1.stop()
            self.StatusSpalare.show()
            self.current_progress = 0
            self.timer2.timeout.connect(self.update_progress)
            self.timer2.start(1000)  

    def update_progress(self):
        if self.current_progress < self.grad_de_murdarie:
            self.current_progress += 1
            self.StatusSpalare.setValue(self.current_progress)
        else:
            self.timer2.stop()
            self.label3.setText("Spălarea a fost finalizată!")
                    
class Info_Prestabilit(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Informatii")

       
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        

       
        self.fillColor = QColor("#f9f6c2")  
        self.penColor = QColor("#000000")

        
        self.close_btn = QPushButton("x", self)
        font = QFont()
        font.setPixelSize(18)
        font.setBold(True)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("background-color: rgba(0,0,0,0); color: black;")
        self.close_btn.setFixedSize(30, 30)
        self.close_btn.clicked.connect(self.close)


        

        
        self.label1 = QLabel("Info: Acesta este un program prestabilit!")
        self.label2 = QLabel("""Pentru ca ati ales acest program, robotul nostru se va ocupa de spalarea masinii.""")
        self.label3 = QLabel("Pozitionati masina in locul marcat!")

        self.setStyleSheet("""
                            QLabel {
                                font-family: Calibri;
                                font-size: 20px;
                                font-weight: bold;
                                 }
                                            """)
        
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(20, 50, 20, 20)  
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)

        self.setFixedSize(730, 300)

    def paintEvent(self, event):
        """Desenare fundal translucid."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.fillColor)
        painter.setPen(QPen(self.penColor, 1))
        painter.drawRoundedRect(self.rect(), 10, 10)

    def resizeEvent(self, event):
        """Mutăm butonul X în colțul din dreapta sus."""
        self.close_btn.move(self.width() - self.close_btn.width() - 5, 5)
        super().resizeEvent(event)
        



if __name__ =='__main__':
    app = QApplication(sys.argv)
    FirstScreen = FirstScreen()
    FirstScreen.show()
    sys.exit(app.exec_())        