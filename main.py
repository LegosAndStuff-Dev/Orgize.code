import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import qrc
from ui_main import MainDashboard
from ui_config import Ui_ConfigUI


class Ui_MainWindow(object):
    def OpenConfigUi(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ConfigUI()
        self.ui.setupUi(self.window, self.app)

        self.window.show()
        
        MainWindow.hide()

    def OpenMainUi(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = MainDashboard()
        self.ui.setupUi(self.window, self.app)

        self.window.show()

        MainWindow.hide()

    def setupUi(self, MainWindow):
        #MainWindow
        MainWindow.setObjectName("Orgize.Code")
        MainWindow.resize(767, 416)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 85);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #left Frame
        self.LeftFrame = QtWidgets.QFrame(self.centralwidget)
        self.LeftFrame.setGeometry(QtCore.QRect(164, 88, 97, 169))
        self.LeftFrame.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(43, 43, 43);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 40px;")
        self.LeftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftFrame.setObjectName("LeftFrame")

        #Left Frame -circle
        self.CircleFrameLeft = QtWidgets.QFrame(self.LeftFrame)
        self.CircleFrameLeft.setGeometry(QtCore.QRect(23, 10, 51, 51))
        self.CircleFrameLeft.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(0, 153, 255);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 25px;\n")
        self.CircleFrameLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CircleFrameLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircleFrameLeft.setObjectName("CircleFrameLeft")

        #Left Frame -circle -image
        self.CompterGraphics = QtWidgets.QGraphicsView(self.CircleFrameLeft)
        self.CompterGraphics.setGeometry(QtCore.QRect(8, 8, 33, 31))
        self.CompterGraphics.setStyleSheet("background-image: url(:/icon/Image/Icons/icons8-google-code-30.png);\n"
                                            "image: url(:/icon/Image/Icons/icons8-settings-30.png);\n"
                                            "background-color: rgb(0, 153, 255);\n"
                                            "border-style: solid;\n"
                                            "border-color: rgb(0, 153, 255);\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 40px;")
        self.CompterGraphics.setObjectName("CompterGraphics")

        #Left Frame -button
        self.OpenMain = QtWidgets.QPushButton(self.LeftFrame)
        self.OpenMain.setGeometry(QtCore.QRect(11, 80, 75, 23))
        self.OpenMain.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(0, 153, 255);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 10px;")
        self.OpenMain.setObjectName("OpenMain")
        self.OpenMain.clicked.connect(self.OpenMainUi)



        #Right Frame
        self.RightFrame = QtWidgets.QFrame(self.centralwidget)
        self.RightFrame.setGeometry(QtCore.QRect(508, 88, 97, 169))
        self.RightFrame.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(43, 43, 43);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 40px;")
        self.RightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightFrame.setObjectName("RightFrame")

        #Right Frame -circle
        self.CircleFrameRight = QtWidgets.QFrame(self.RightFrame)
        self.CircleFrameRight.setGeometry(QtCore.QRect(23, 10, 51, 51))
        self.CircleFrameRight.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(0, 153, 255);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 25px;\n")
        self.CircleFrameRight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CircleFrameRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircleFrameRight.setObjectName("CircleFrameRight")

        #Right Frame -circle -image
        self.SettingsGraphic = QtWidgets.QGraphicsView(self.CircleFrameRight)
        self.SettingsGraphic.setGeometry(QtCore.QRect(8, 8, 33, 31))
        self.SettingsGraphic.setStyleSheet("background-image: url(:/icon/Image/Icons/icons8-settings-30.png);\n"
                                            "background-color: rgb(0, 153, 255);\n"
                                            "border-style: solid;\n"
                                            "border-color: rgb(0, 153, 255);\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 40px;")
        self.SettingsGraphic.setObjectName("SettingsGraphic")

        #Right Frame -button
        self.OpenConfig = QtWidgets.QPushButton(self.RightFrame)
        self.OpenConfig.setGeometry(QtCore.QRect(11, 80, 75, 23))
        self.OpenConfig.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(0, 153, 255);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 10px;")

        self.OpenConfig.setObjectName("OpenConfig")
        self.OpenConfig.clicked.connect(self.OpenConfigUi)


        #Wave
        self.Wave = QtWidgets.QGraphicsView(self.centralwidget)
        self.Wave.setGeometry(QtCore.QRect(-152, 128, 957, 317))
        self.Wave.setStyleSheet("background-image: url(:/wave/Image/Wave/wave_2.png);\n"
                                "border-style: solid;\n"
                                "border-color: rgb(43, 43, 43);\n")
        self.Wave.setObjectName("Wave")
        
        #Raise
        self.Wave.raise_()
        self.LeftFrame.raise_()
        self.RightFrame.raise_()

        #Other Stuff
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orgize.Code"))
        self.OpenMain.setText(_translate("MainWindow", "Open"))
        self.OpenConfig.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
