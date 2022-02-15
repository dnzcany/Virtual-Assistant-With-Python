from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLayout,QPushButton,QApplication,QLineEdit,QLabel,QTextEdit
from PyQt5.QtGui import QFont,QPixmap,QIcon
import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Deno")
        self.setStyleSheet("Background-color:purple")
        self.setGeometry(720,100,550,600)


        label = QLabel("Welcome to Deno",self)
        label.setStyleSheet("color:black")
        label.setFont(QFont("Arial",20))
        label.move(145,80)

        label = QLabel("""           This application was made by DCY for voice command,if you want watch a Youtube videos 
    please saying VİDEO NAME+PLAY.İf you want a what time is now,please saying WHAT TİME İS İT.Enjoy! :)""", self)
        label.setStyleSheet("color:black")
        label.setFont(QFont("Arial", 8))
        label.move(0, 200)

        self.button = QPushButton("Search",self)
        self.button.setStyleSheet("Background-color:Grey")
        self.button.setFont(QFont("Arial",20))
        self.button.move(225,340)
        self.button.resize(100,50)

        self.button.clicked.connect(self.click)
        self.show()

    def click(self):
        dinleyici = sr.Recognizer()
        engine = pyttsx3.init()
        newVoiceRate = 140
        engine.setProperty('rate', newVoiceRate)

        def talk(text):
            engine.say(text)
            engine.runAndWait()

        def takecommand():
            try:
                with sr.Microphone() as source:

                    ses = dinleyici.listen(source)
                    command = dinleyici.recognize_google(ses, language='en')
                    print(command)
            except:
                pass
            return command

        def rundeno():
            command = takecommand()
            print(command)
            if 'play' in command:
                sarki = command.replace('play', '')
                talk("playing" + sarki)
                print("playing" + sarki)
                pywhatkit.playonyt(sarki)

            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
                print('Current time is ' + time)
            else:
                talk('Please say the command again.')

        while True:
            rundeno()



























app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())