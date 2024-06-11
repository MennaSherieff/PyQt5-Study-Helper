import sys
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, QDate, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import newresources_rc   ######### to convert resources to py code: pycc5 uiFile -o pyFile

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(652, 403)
        MainWindow.setStyleSheet(u"background: white\n" "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 161, 421))
        self.widget.setStyleSheet(u"background: #faedcd")
############################       Menu       ############################
        self.menu = QWidget(self.widget)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(20, 10, 121, 381))
        self.menu.setStyleSheet(u"*{background: #faedcd;}\n"
"QPushButton{border:none; text-align: left; padding:5px; color:#3a2618; font-weight: 470;}\n"
"QPushButton:hover{border-radius: 8px; background:#e0afa0;}")
        self.verticalLayout_4 = QVBoxLayout(self.menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
############################       Menu Buttins      ############################
        self.homeBtn = QPushButton(self.menu)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(62)
        self.homeBtn.setFont(font)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8-home-page-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(18,18))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setAutoExclusive(True)
        self.verticalLayout_3.addWidget(self.homeBtn)

        self.notesBtn = QPushButton(self.menu)
        self.notesBtn.setObjectName(u"notesBtn")
        self.notesBtn.setFont(font)
        self.notesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.notesBtn.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8-notepad-50 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.notesBtn.setIcon(icon1)
        self.notesBtn.setIconSize(QSize(18,18))
        self.notesBtn.setCheckable(True)
        self.notesBtn.setAutoExclusive(True)
        self.verticalLayout_3.addWidget(self.notesBtn)

        self.todoBtn = QPushButton(self.menu)
        self.todoBtn.setObjectName(u"todoBtn")
        font1 = QFont()
        font1.setFamily(u"MS Reference Sans Serif")
        font1.setPointSize(7)
        font1.setBold(True)
        font1.setWeight(62)
        self.todoBtn.setFont(font1)
        self.todoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.todoBtn.setFocusPolicy(Qt.NoFocus)
        self.todoBtn.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8-to-do-list-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.todoBtn.setIcon(icon2)
        self.todoBtn.setIconSize(QSize(18,18))
        self.todoBtn.setCheckable(True)
        self.todoBtn.setAutoExclusive(True)
        self.verticalLayout_3.addWidget(self.todoBtn)

        self.timerBtn = QPushButton(self.menu)
        self.timerBtn.setObjectName(u"timerBtn")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(62)
        self.timerBtn.setFont(font2)
        self.timerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.timerBtn.setFocusPolicy(Qt.NoFocus)
        self.timerBtn.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-timer-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/icons8-timer-50.png", QSize(), QIcon.Normal, QIcon.On)
        self.timerBtn.setIcon(icon3)
        self.timerBtn.setIconSize(QSize(18,18))
        self.timerBtn.setCheckable(True)
        self.timerBtn.setAutoExclusive(True)
        self.verticalLayout_3.addWidget(self.timerBtn)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exitBtn = QPushButton(self.menu)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setFont(font2)
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setFocusPolicy(Qt.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8-exit-50 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon4)
        self.exitBtn.setIconSize(QSize(18,18))
        self.exitBtn.setCheckable(False)
        self.exitBtn.setAutoExclusive(True)
        self.verticalLayout_4.addWidget(self.exitBtn)

############################       StackedWidget       ############################
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 0, 491, 401))
        font3 = QFont()
        font3.setFamily(u"Microsoft YaHei Light")
        font3.setPointSize(10)
        self.stackedWidget.setFont(font3)

############################       Page1: Home       ############################    
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setStyleSheet(u"QPushButton{border:none; }")
        self.pushButton = QPushButton(self.page1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 471, 381))
        icon5 = QIcon()
        icon5.addFile(u"icons/undraw_Augmented_reality_re_f0qd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(600, 500))
        self.label = QLabel(self.page1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 121, 51))
        self.label.setStyleSheet(u"font-family: Arial, Helvetica, sans-serif;\n"
"font-size: 30px;\n"
"background: transparent;\n"
"")
        self.label_2 = QLabel(self.page1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 40, 131, 61))
        self.label_2.setStyleSheet(u"font-family: Arial, Helvetica, sans-serif;\n"
"font-size: 40px;\n"
"background: transparent;\n"
"color: #F9A826;")
        self.label_3 = QLabel(self.page1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 360, 131, 31))
        self.label_3.setStyleSheet(u"font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"font-size: 15px;\n"
"background: #F9A826;\n"
"opacity: 0.4;\n"
"border: none;\n"
"border-radius: 8px;\n"
"color: white;\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page1)

############################       Page2: Txt to speech       ############################    
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.text = QLineEdit(self.page2)
        self.text.setStyleSheet("background-color: #f7f7f7; padding: 5px; margin: 3px; font-size: 15px; border-radius: 10px; border: 1px solid #ddd;")
        self.text.setClearButtonEnabled(True)
        self.text.setPlaceholderText('Type ... ')
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(10, 10, 471, 281))
        self.sayButton = QPushButton('Play', self.page2)
        self.sayButton.setObjectName(u"sayButton")
        self.sayButton.setGeometry(QRect(10, 355, 471, 40))
        self.sayButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sayButton.setStyleSheet("background-color: #754043; color: white; font-size: 16px; border: none; padding: 35px; border-radius: 5px;")
        self.text.returnPressed.connect(self.sayButton.animateClick)
        self.voiceCombo = QComboBox(self.page2)
        self.voiceCombo.setObjectName(u"voiceCombo")
        self.voiceCombo.setGeometry(QRect(10, 300, 471, 22))
        self.voiceCombo.setStyleSheet("font-size: 14px; border: 1px solid #ddd; border-radius: 5px;")
        self.volumeSlider = QSlider(self.page2)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setGeometry(QRect(10, 330, 471, 20))
        self.volumeSlider.setOrientation(Qt.Horizontal)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        self.stackedWidget.addWidget(self.page2)

############################       Page3: To-Do List       ############################    
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.layout = QVBoxLayout(self.page3)
        self.todo_list = QListWidget(self.page3)
        self.todo_list.setStyleSheet("background-color: #f7f7f7; font-size: 16px; border: 1px solid #ddd;")
        self.layout.addWidget(self.todo_list)
        self.task_layout = QHBoxLayout(self.page3)
        self.add_task_input = QLineEdit(self.page3)
        self.add_task_input.setPlaceholderText('Add a new task')
        self.add_task_input.setStyleSheet("font-size: 14px; border: 1px solid #ddd; border-radius: 5px;")
        self.add_button = QPushButton('Add Task')
        self.add_button.setStyleSheet("background-color: #754043; color: white; font-size: 14px; border: none; padding: 8px 12px; border-radius: 5px;")
        self.task_layout.addWidget(self.add_task_input)
        self.task_layout.addWidget(self.add_button)
        self.layout.addLayout(self.task_layout)       
        self.options_layout = QHBoxLayout(self.page3)
        self.due_date = QDateEdit(self.page3)
        self.due_date.setDate(QDate.currentDate())
        self.due_date.setCalendarPopup(True)
        self.due_date.setStyleSheet("font-size: 14px; border: 1px solid #ddd; border-radius: 5px;")
        self.options_layout.addWidget(self.due_date)
        self.remove_button = QPushButton('Remove Task')
        self.remove_button.setStyleSheet("background-color: #ab8476; color: white; font-size: 14px; border: none; padding: 8px 12px; border-radius: 5px;")
        self.options_layout.addWidget(self.remove_button)
        self.layout.addLayout(self.options_layout)
        self.stackedWidget.addWidget(self.page3)
############################       Page4: Timer       ############################    
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.timerlayout = QFormLayout(self.page4)
        self.hour = QLineEdit(self.page4)
        font = QFont()
        self.hour.setFont(font)
        self.hour.setStyleSheet("background-color: #f7f7f7; border: 1px solid #ddd; border-radius: 5px;")
        self.timerlayout.addRow('Hours:', self.hour)
        self.mint = QLineEdit(self.page4)
        font = QFont()
        self.mint.setFont(font)
        self.mint.setStyleSheet("background-color: #f7f7f7; border: 1px solid #ddd; border-radius: 5px;")
        self.timerlayout.addRow('Minutes:',self.mint)
        self.secs = QLineEdit(self.page4)
        font = QFont()
        self.secs.setFont(font)
        self.secs.setStyleSheet("background-color: #f7f7f7; border: 1px solid #ddd; border-radius: 5px;")
        self.timerlayout.addRow('Seconds:', self.secs)
        self.start = QPushButton('Start', self.page4)
        self.start.setStyleSheet("background-color: #754043; color: white; font-size: 15px; border: none; padding: 8px 12px; border-radius: 7px;")
        self.timerlayout.addRow(self.start)
        self.countDown= QLabel(self.page4)
        self.countDown.setStyleSheet("text-align: center; border: 1px solid #ddd; border-radius: 5px;")
        self.timerlayout.addRow(self.countDown)
        self.stop = QPushButton('Stop', self.page4)
        self.stop.setStyleSheet("background-color: #754043; color: white; font-size: 15px; border: none; padding: 8px 12px; border-radius: 7px;")
        self.timerlayout.addRow(self.stop)


        self.stackedWidget.addWidget(self.page4)        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.notesBtn.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.todoBtn.setText(QCoreApplication.translate("MainWindow", u"To-Do List", None))
        self.timerBtn.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Study", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Helper", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  Get Started", None))
    # retranslateUi
        

