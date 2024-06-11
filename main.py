from PyQt5.QtWidgets import *
from PySide2 import QtWidgets
from PySide2.QtTextToSpeech import QTextToSpeech, QVoice
from PyQt5 import QtWidgets,uic,QtCore
from PyQt5.QtWidgets import *
from PySide2 import QtWidgets
from playsound import playsound
from PySide2.QtGui import QIcon
from PyQt5.QtCore import QThread,pyqtSignal
import time 
import sys
from ui_main import Ui_MainWindow ## importing the class that contains the GUI from the UI python file


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Study Helper')
        self.setWindowIcon(QIcon('icon.png'))

        ########### Connecting pages with menu buttons #############        
        self.ui.homeBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.ui.notesBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        self.ui.todoBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page3))
        self.ui.timerBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page4))

        ########### Connecting buttons with function #############        
        self.ui.sayButton.clicked.connect(self.say)
        self.ui.remove_button.clicked.connect(self.remove_task)
        self.ui.add_button.clicked.connect(self.add_task)
        self.ui.start.clicked.connect(self.start_timer)

################# Text to speech functions ######################
        self.engine = None
        engineNames = QTextToSpeech.availableEngines()
        if len(engineNames) > 0:
            engineName = engineNames[0]
            self.engine = QTextToSpeech(engineName)
            self.engine.stateChanged.connect(self.stateChanged)
            self.voices = []
            for voice in self.engine.availableVoices():
                self.voices.append(voice)
                self.ui.voiceCombo.addItem(voice.name())
        else:
            self.setWindowTitle('no engines available')
            self.ui.sayButton.setEnabled(False)

    def say(self):
        self.ui.sayButton.setEnabled(False)
        self.engine.setVoice(self.voices[self.ui.voiceCombo.currentIndex()])
        self.engine.setVolume(float(self.ui.volumeSlider.value()) / 100)
        self.engine.say(self.ui.text.text())

    def stateChanged(self, state):
        if (state == QTextToSpeech.State.Ready):
            self.ui.sayButton.setEnabled(True)

################# To-do list functions ######################
    def add_task(self):
        task = self.ui.add_task_input.text()
        if task:
            due_date = self.ui.due_date.date().toString('dd/MM/yyyy')
            task_text = f" Task: {task} - Due: {due_date}"
            self.ui.todo_list.addItem(task_text)
            self.ui.add_task_input.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a task.')

    def remove_task(self):
        selected_item = self.ui.todo_list.currentItem()
        if selected_item:
            self.ui.todo_list.takeItem(self.ui.todo_list.row(selected_item))
        else:
            QMessageBox.warning(self, 'Warning', 'Select a task to remove.')

################# Timer functions ######################        
    def start_timer(self):
        total_seconds=int(self.ui.secs.text())+int(self.ui.hour.text())*3600+int(self.ui.mint.text())*60
        self.thread=Timethread(int(total_seconds))
        self.thread.start()
        self.thread.signal.connect(self.change_timer)

    def change_timer(self,val):
        print(val)
        self.ui.countDown.setText(str(val))
        
class Timethread(QThread):
    signal=pyqtSignal(str)
    def __init__(self,limit):
        super(Timethread,self).__init__()
        self.limit_seconds=limit
    def run(self):
        i=int(self.limit_seconds)
        while i>0:
            self.signal.emit(str(i))
            time.sleep(1)
            print(i)
            i-=1
            if i==0:
                playsound("sound.mp3")
                break
        self.signal.emit("Time is up!")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()