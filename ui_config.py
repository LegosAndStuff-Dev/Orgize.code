import asyncio
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
import qrc
from github import Github
import json
import sqlite3
import time

class Ui_ConfigUI(object):
    def setupUi(self, ConfigUI, app):
        ConfigUI.setObjectName("ConfigUI")
        ConfigUI.resize(1297, 566)
        ConfigUI.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.centralwidget = QtWidgets.QWidget(ConfigUI)
        self.centralwidget.setObjectName("centralwidget")


        #Current Project / Title
        self.Title = QtWidgets.QFrame(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 10, 1281, 40))
        self.Title.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                            "border-style: solid;\n"
                                            "border-color: rgb(43, 43, 43);\n"
                                            "border-width: 4px;\n"
                                            "border-radius: 20px;")
        self.Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title.setObjectName("Title")

        #Title -CurrentProject
        self.CurrentProject = QtWidgets.QLabel(self.Title)
        self.CurrentProject.setGeometry(QtCore.QRect(1, 0, 1281, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CurrentProject.setFont(font)
        self.CurrentProject.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentProject.setObjectName("CurrentProject")


        #Left Top Frame
        self.LeftTopFrame = QtWidgets.QFrame(self.centralwidget)
        self.LeftTopFrame.setGeometry(QtCore.QRect(10, 60, 411, 320))
        self.LeftTopFrame.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(43, 43, 43);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 40px;")
        self.LeftTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftTopFrame.setObjectName("LeftTopFrame")

        #Left Top Frame -FrameLabel
        self.LefTopTitleFrame = QtWidgets.QFrame(self.LeftTopFrame)
        self.LefTopTitleFrame.setGeometry(QtCore.QRect(20, 15, 371, 26))
        self.LefTopTitleFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 10px;")
        self.LefTopTitleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LefTopTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LefTopTitleFrame.setObjectName("LefTopTitleFrame")

        #Left Top Frame -FrameLabel -Title
        self.LeftTopTitle = QtWidgets.QLabel(self.LefTopTitleFrame)
        self.LeftTopTitle.setGeometry(QtCore.QRect(11, 0, 351, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LeftTopTitle.setFont(font)
        self.LeftTopTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.LeftTopTitle.setObjectName("LeftTopTitle")

        #Left Top Frame -ProjectList
        self.ProjectList = QtWidgets.QTreeWidget(self.LeftTopFrame)
        self.ProjectList.setGeometry(QtCore.QRect(35, 50, 341, 251))
        self.ProjectList.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 8px;")
        self.ProjectList.setObjectName("ProjectList")

        #Left Top Frame -Test -Item

        conn = sqlite3.connect("project.db")
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM project")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            pass

        else:
            for item in items:
                item_0 = QtWidgets.QTreeWidgetItem(self.ProjectList)

                rowid = int(item[0])
                name = item[1]
                dir = item[2]

                rowid = rowid - 1

                try:
                    dir = dir.split("/Desktop")
                    dir = dir[1]

                except:
                    dir = dir[0]

                _translate = QtCore.QCoreApplication.translate
                self.ProjectList.topLevelItem(rowid).setText(0, _translate("ConfigUI", f"{name}"))
                self.ProjectList.topLevelItem(rowid).setText(1, _translate("ConfigUI", f"{dir}"))


        #Left Bottom Frame
        self.LeftBottomFrame = QtWidgets.QFrame(self.centralwidget)
        self.LeftBottomFrame.setGeometry(QtCore.QRect(10, 390, 411, 161))
        self.LeftBottomFrame.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(43, 43, 43);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 40px;")
        self.LeftBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftBottomFrame.setObjectName("LeftBottomFrame")

        #Left Bottom Frame -FrameLabel
        self.LeftBottomTitleFrame = QtWidgets.QFrame(self.LeftBottomFrame)
        self.LeftBottomTitleFrame.setGeometry(QtCore.QRect(20, 15, 371, 35))
        self.LeftBottomTitleFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 10px;")
        self.LeftBottomTitleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftBottomTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftBottomTitleFrame.setObjectName("LeftBottomTitleFrame")

        #Left Bottom Frame -FrameLabel -Title
        self.LeftBottomTitle = QtWidgets.QLabel(self.LeftBottomTitleFrame)
        self.LeftBottomTitle.setGeometry(QtCore.QRect(11, 2, 351, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LeftBottomTitle.setFont(font)
        self.LeftBottomTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.LeftBottomTitle.setObjectName("LeftBottomTitle")

        #Left Bottom Frame -GithubUsernameInput
        self.GithubUsernameInput = QtWidgets.QLineEdit(self.LeftBottomFrame)
        self.GithubUsernameInput.setGeometry(QtCore.QRect(40, 70, 331, 30))
        self.GithubUsernameInput.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 8px;")
        self.GithubUsernameInput.setObjectName("GitHubUsernameInput")
        with open("config.json", "r") as outfile:
            data = json.load(outfile)

        username = data["Config"][0]["Github_Username"]
        self.GithubUsernameInput.setText(username)

        #Left Bottom Frame  -SetGithubName -Buttom
        self.SetGithubName = QtWidgets.QPushButton(self.LeftBottomFrame)
        self.SetGithubName.setGeometry(QtCore.QRect(120, 115, 171, 23))
        self.SetGithubName.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 8px;")
        self.SetGithubName.setObjectName("SetGithubName")
        self.SetGithubName.clicked.connect(self.GithubUsernameGetEvent)

        
        #Cent Top Frame
        self.CenterFrameTop = QtWidgets.QFrame(self.centralwidget)
        self.CenterFrameTop.setGeometry(QtCore.QRect(440, 60, 411, 241))
        self.CenterFrameTop.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(43, 43, 43);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 40px;")
        self.CenterFrameTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CenterFrameTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CenterFrameTop.setObjectName("CenterFrameTop")

        #Center Top Frame -FrameLabel
        self.CenterTopTitleFrame = QtWidgets.QFrame(self.CenterFrameTop)
        self.CenterTopTitleFrame.setGeometry(QtCore.QRect(20, 15, 371, 26))
        self.CenterTopTitleFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 10px;")
        self.CenterTopTitleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CenterTopTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CenterTopTitleFrame.setObjectName("CenterTopTitleFrame")

        #Center Top Frame -FrameLabel -Title
        self.CenterTopTitle = QtWidgets.QLabel(self.CenterTopTitleFrame)
        self.CenterTopTitle.setGeometry(QtCore.QRect(11, 0, 351, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CenterTopTitle.setFont(font)
        self.CenterTopTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.CenterTopTitle.setObjectName("CenterTopTitle")

        #Center Top Frame -ManualProjectLineEdit
        self.ManualProjectLineEdit = QtWidgets.QLineEdit(self.CenterFrameTop)
        self.ManualProjectLineEdit.setGeometry(QtCore.QRect(25, 55, 361, 30))
        self.ManualProjectLineEdit.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 8px;\n")
        self.ManualProjectLineEdit.setText("")
        self.ManualProjectLineEdit.setReadOnly(False)
        self.ManualProjectLineEdit.setObjectName("ManualProjectLineEdit")
        self.ManualProjectLineEdit.setPlaceholderText("Enter Project Name")

        #Right Top Frame -Manual -AddProject -Top
        self.AddProjectTop = QtWidgets.QPushButton(self.CenterFrameTop)
        self.AddProjectTop.setGeometry(QtCore.QRect(145, 145, 121, 23))
        self.AddProjectTop.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 8px;")
        self.AddProjectTop.setObjectName("AddProjectTop")
        self.AddProjectTop.clicked.connect(self.MakeProjectTopEvent)

        #Right Top Frame -ChooseFolderTop
        self.ChooseFolderTop = QtWidgets.QPushButton(self.CenterFrameTop)
        self.ChooseFolderTop.setGeometry(QtCore.QRect(25, 100, 111, 23))
        self.ChooseFolderTop.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 8px;")
        self.ChooseFolderTop.setObjectName("ChooseFolderTop")
        self.ChooseFolderTop.clicked.connect(self.ChooseFolderTopEvent)

        #Right Top Folder -FolderOutput
        self.FolderOutputTop = QtWidgets.QLineEdit(self.CenterFrameTop)
        self.FolderOutputTop.setGeometry(QtCore.QRect(140, 100, 245, 23))
        self.FolderOutputTop.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 8px;\n"
                                        "QLineEdit[readOnly=\\\"true\\\"]")
        self.FolderOutputTop.setText("")
        self.FolderOutputTop.setReadOnly(True)
        self.FolderOutputTop.setObjectName("FolderOutputTop")


        #Right Bottom Frame
        self.CenterBottomFrame = QtWidgets.QFrame(self.centralwidget)
        self.CenterBottomFrame.setGeometry(QtCore.QRect(440, 310, 411, 241))
        self.CenterBottomFrame.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(43, 43, 43);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 40px;")
        self.CenterBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CenterBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CenterBottomFrame.setObjectName("CenterBottomFrame")

        #Right Bottom Frame -FrameLabel
        self.CenterBottomTitleFrame = QtWidgets.QFrame(self.CenterBottomFrame)
        self.CenterBottomTitleFrame.setGeometry(QtCore.QRect(20, 15, 371, 26))
        self.CenterBottomTitleFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 10px;")
        self.CenterBottomTitleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CenterBottomTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CenterBottomTitleFrame.setObjectName("CenterBottomTitleFrame")

        #Right Bottom Frame -FrameLabel -Title
        self.CenterBottomTitle = QtWidgets.QLabel(self.CenterBottomTitleFrame)
        self.CenterBottomTitle.setGeometry(QtCore.QRect(11, 0, 351, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CenterBottomTitle.setFont(font)
        self.CenterBottomTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.CenterBottomTitle.setObjectName("CenterBottomTitle")

        #Right Bottom Frame -GithubProjectAddCombo -ComboBox
        self.GithubProjectAddCombo = QtWidgets.QComboBox(self.CenterBottomFrame)
        self.GithubProjectAddCombo.setGeometry(QtCore.QRect(25, 55, 361, 30))
        self.GithubProjectAddCombo.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 8px;")
        self.GithubProjectAddCombo.setObjectName("GithubProjectAddCombo")
        self.GithubProjectAddCombo.setPlaceholderText("Choose a project")

        with open('config.json') as f:
            data = json.load(f)

        username = data["Config"][0]["Github_Username"]
        try: 
            g = Github()
            user = g.get_user(username)
            for repo in user.get_repos():
                self.GithubProjectAddCombo.addItem(repo.name)

        except:
            self.GithubProjectAddCombo.addItem("No Repos Found")

        #Right Bottom Frame -ChoseFolder
        self.ChooseFolderBottom = QtWidgets.QPushButton(self.CenterBottomFrame)
        self.ChooseFolderBottom.setGeometry(QtCore.QRect(25, 100, 111, 23))
        self.ChooseFolderBottom.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 8px;")
        self.ChooseFolderBottom.setObjectName("ChooseFolderBottom")
        self.ChooseFolderBottom.clicked.connect(self.ChooseFolderBottomEvent)

        #Right Bottom Folder -FolderOutput
        self.FolderOutputBottom = QtWidgets.QLineEdit(self.CenterBottomFrame)
        self.FolderOutputBottom.setGeometry(QtCore.QRect(140, 100, 245, 23))
        self.FolderOutputBottom.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 8px;\n"
                                                "QLineEdit[readOnly=\\\"true\\\"]")
        self.FolderOutputBottom.setText("")
        self.FolderOutputBottom.setReadOnly(True)
        self.FolderOutputBottom.setObjectName("FolderOutputBottom")

        #Right Bottom Frame -AddProject
        self.AddProjectBottom = QtWidgets.QPushButton(self.CenterBottomFrame)
        self.AddProjectBottom.setGeometry(QtCore.QRect(145, 145, 121, 23))
        self.AddProjectBottom.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(0, 153, 255);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 8px;")
        self.AddProjectBottom.setObjectName("AddProjectBottom")
        self.AddProjectBottom.clicked.connect(self.MakeProjectBottomEvent)


        #Right Top Frame
        self.RightTopFrame = QtWidgets.QFrame(self.centralwidget)
        self.RightTopFrame.setGeometry(QtCore.QRect(870, 60, 411, 241))
        self.RightTopFrame.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(43, 43, 43);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 40px;")
        self.RightTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightTopFrame.setObjectName("RightTopFrame")

        #Right Bottom FRame
        self.RightBottomFrame = QtWidgets.QFrame(self.centralwidget)
        self.RightBottomFrame.setGeometry(QtCore.QRect(870, 310, 411, 241))
        self.RightBottomFrame.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(43, 43, 43);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 40px;")
        self.RightBottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightBottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightBottomFrame.setObjectName("RightBottomFrame")


        #Wave
        self.Wave = QtWidgets.QGraphicsView(self.centralwidget)
        self.Wave.setGeometry(QtCore.QRect(-2, 278, 957, 317))
        self.Wave.setStyleSheet("background-image: url(:/wave/Image/Wave/wave_2.png);\n"
                                "border-style: solid;\n"
                                "border-color: rgb(43, 43, 43);\n")
        self.Wave.setObjectName("Wave")
        self.Wave2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.Wave2.setGeometry(QtCore.QRect(955, 278, 957, 317))
        self.Wave2.setStyleSheet("background-image: url(:/wave/Image/Wave/wave_2.png);\n"
                                "border-style: solid;\n"
                                "border-color: rgb(43, 43, 43);\n")
        self.Wave2.setObjectName("Wave2")

        
        #App Stuff
        app.setStyleSheet("QHeaderView::section { background-color: rgb(0, 153, 255) }\n"
                          "QListWidget::item:selected {\n"
                                "background-color: rgb(0, 89, 148);\n"
                                "border-style: solid;\n"
                                "border-color: rgb(0, 153, 255);\n"
                                "border-width: 2px;\n"
                                "border-radius: 10px;\n"
                            "};\n")
        
        #Raise
        self.RightTopFrame.raise_()
        self.Wave.raise_()
        self.LeftTopFrame.raise_()
        self.LeftBottomFrame.raise_()
        self.CenterFrameTop.raise_()
        self.CenterBottomFrame.raise_()
        self.RightTopFrame.raise_()
        self.RightBottomFrame.raise_()

        #Other
        ConfigUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConfigUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 22))
        self.menubar.setObjectName("menubar")
        ConfigUI.setMenuBar(self.menubar)

        self.retranslateUi(ConfigUI)
        QtCore.QMetaObject.connectSlotsByName(ConfigUI)

    def retranslateUi(self, ConfigUI):
        _translate = QtCore.QCoreApplication.translate
        ConfigUI.setWindowTitle(_translate("ConfigUI", "Orgize.code"))
        self.LeftTopTitle.setText(_translate("ConfigUI", "Project File Directories List"))
        self.ProjectList.headerItem().setText(0, _translate("ConfigUI", "Project Name"))
        self.ProjectList.headerItem().setText(1, _translate("ConfigUI", "Project DIR"))
        __sortingEnabled = self.ProjectList.isSortingEnabled()
        self.ProjectList.setSortingEnabled(False)
        self.ProjectList.setSortingEnabled(__sortingEnabled)
        self.LeftBottomTitle.setText(_translate("ConfigUI", "Github Username Config"))
        self.SetGithubName.setText(_translate("ConfigUI", "Set Github Name"))
        self.CenterTopTitle.setText(_translate("ConfigUI", "Manual Project Add"))
        self.AddProjectTop.setText(_translate("ConfigUI", "Add Project"))
        self.ChooseFolderTop.setText(_translate("ConfigUI", "Choose Folder"))
        self.CenterBottomTitle.setText(_translate("ConfigUI", "Github Project Add"))
        self.ChooseFolderBottom.setText(_translate("ConfigUI", "Choose Folder"))
        self.AddProjectBottom.setText(_translate("ConfigUI", "Add Project"))
        self.CurrentProject.setText(_translate("MainWindow", f"Config Dashboard"))

    def ChooseFolderTopEvent(self):
        self.responseTop = QFileDialog.getExistingDirectory(caption='Select a folder')

        response = self.responseTop.split("/Desktop")
        
        self.FolderOutputTop.setText(f"{response[1]}")


    def ChooseFolderBottomEvent(self):
        self.responseBottom = QFileDialog.getExistingDirectory(caption='Select a folder')
        
        response = self.responseBottom.split("/Desktop")
        
        self.FolderOutputBottom.setText(f"{response[1]}")

    def GithubUsernameGetEvent(self):
        input = self.GithubUsernameInput.text()

        print(input)

        data = {}
        data["Config"] = []

        data["Config"].append({
            "Github_Username": f"{input}"
        })

        json_object = json.dumps(data, indent = 4)
        
        with open("config.json", "w") as outfile:
            outfile.write(json_object)

        self.GithubProjectAddCombo.clear()

        with open('config.json') as f:
            data = json.load(f)

        username = data["Config"][0]["Github_Username"]

        try:
            g = Github()
            user = g.get_user(username)
            for repo in user.get_repos():
                self.GithubProjectAddCombo.addItem(repo.name)

        except:
            self.GithubProjectAddCombo.addItem("No Repos Found")


    def MakeProjectTopEvent(self):
        folder = self.FolderOutputTop.text()
        project_name = self.ManualProjectLineEdit.text()

        if folder == "" and project_name == "":
            #Right Top Frame -ErrorOutputFrame
            self.ErrorTopOutputFrame = QtWidgets.QFrame(self.RightFrameTop)
            self.ErrorTopOutputFrame.setGeometry(QtCore.QRect(45, 200, 321, 26))
            self.ErrorTopOutputFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                    "border-style: solid;\n"
                                                    "border-color: rgb(0, 153, 255);\n"
                                                    "border-width: 2px;\n"
                                                    "border-radius: 10px;")
            self.ErrorTopOutputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.ErrorTopOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.ErrorTopOutputFrame.setObjectName("ErrorTopOutputFrame")

            #Right Top Frame -ErrorOutputFrame -Error
            self.ErrorOutputTop = QtWidgets.QLabel(self.ErrorTopOutputFrame)
            self.ErrorOutputTop.setGeometry(QtCore.QRect(11, 0, 301, 26))
            font = QtGui.QFont()
            font.setPointSize(8)
            self.ErrorOutputTop.setFont(font)
            self.ErrorOutputTop.setAlignment(QtCore.Qt.AlignCenter)
            self.ErrorOutputTop.setObjectName("ErrorOutputTop")
            self.ErrorOutputTop.setText("Folder and Project Name are required.")

            self.ErrorTopOutputFrame.show()

        elif folder == "":
            #Right Top Frame -ErrorOutputFrame
            self.ErrorTopOutputFrame = QtWidgets.QFrame(self.RightFrameTop)
            self.ErrorTopOutputFrame.setGeometry(QtCore.QRect(45, 200, 321, 26))
            self.ErrorTopOutputFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                    "border-style: solid;\n"
                                                    "border-color: rgb(0, 153, 255);\n"
                                                    "border-width: 2px;\n"
                                                    "border-radius: 10px;")
            self.ErrorTopOutputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.ErrorTopOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.ErrorTopOutputFrame.setObjectName("ErrorTopOutputFrame")

            #Right Top Frame -ErrorOutputFrame -Error
            self.ErrorOutputTop = QtWidgets.QLabel(self.ErrorTopOutputFrame)
            self.ErrorOutputTop.setGeometry(QtCore.QRect(11, 0, 301, 26))
            font = QtGui.QFont()
            font.setPointSize(8)
            self.ErrorOutputTop.setFont(font)
            self.ErrorOutputTop.setAlignment(QtCore.Qt.AlignCenter)
            self.ErrorOutputTop.setObjectName("ErrorOutputTop")
            self.ErrorOutputTop.setText("Folder field is required.")

            self.ErrorTopOutputFrame.show()

        elif project_name == "":
             #Right Top Frame -ErrorOutputFrame
            self.ErrorTopOutputFrame = QtWidgets.QFrame(self.RightFrameTop)
            self.ErrorTopOutputFrame.setGeometry(QtCore.QRect(45, 200, 321, 26))
            self.ErrorTopOutputFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                    "border-style: solid;\n"
                                                    "border-color: rgb(0, 153, 255);\n"
                                                    "border-width: 2px;\n"
                                                    "border-radius: 10px;")
            self.ErrorTopOutputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.ErrorTopOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.ErrorTopOutputFrame.setObjectName("ErrorTopOutputFrame")

            #Right Top Frame -ErrorOutputFrame -Error
            self.ErrorOutputTop = QtWidgets.QLabel(self.ErrorTopOutputFrame)
            self.ErrorOutputTop.setGeometry(QtCore.QRect(11, 0, 301, 26))
            font = QtGui.QFont()
            font.setPointSize(8)
            self.ErrorOutputTop.setFont(font)
            self.ErrorOutputTop.setAlignment(QtCore.Qt.AlignCenter)
            self.ErrorOutputTop.setObjectName("ErrorOutputTop")
            self.ErrorOutputTop.setText("Project Name field is required.")

            self.ErrorTopOutputFrame.show()
            
        else:
            conn = sqlite3.connect("project.db")
            c = conn.cursor()

            c.execute(f"SELECT * FROM project WHERE project_name='{project_name}'")

            items_project = c.fetchall()
            none_project = str(items_project)

            c.execute(f"SELECT * FROM project WHERE project_dir='{self.responseTop}'")

            items_dir = c.fetchall()
            none_dir = str(items_dir)

            if none_project == "[]" and none_dir == "[]":
                print("none_all")

            elif none_dir == "[]":
                print("none_dir")

            elif none_project == "[]":
                print("none_project")

            

    def MakeProjectBottomEvent(self):
        folder = self.FolderOutputBottom.text()
        project_name = self.GithubProjectAddCombo.currentText()

        if folder == "" and project_name == "":
            #Right Top Frame -ErrorOutputFrame
            self.ErrorBottomOutputFrame = QtWidgets.QFrame(self.RightBottomFrame)
            self.ErrorBottomOutputFrame.setGeometry(QtCore.QRect(45, 200, 321, 26))
            self.ErrorBottomOutputFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                    "border-style: solid;\n"
                                                    "border-color: rgb(0, 153, 255);\n"
                                                    "border-width: 2px;\n"
                                                    "border-radius: 10px;")
            self.ErrorBottomOutputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.ErrorBottomOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.ErrorBottomOutputFrame.setObjectName("ErrorBottomOutputFrame")

            #Right Top Frame -ErrorOutputFrame -Error
            self.ErrorOutputBottom = QtWidgets.QLabel(self.ErrorBottomOutputFrame)
            self.ErrorOutputBottom.setGeometry(QtCore.QRect(11, 0, 301, 26))
            font = QtGui.QFont()
            font.setPointSize(8)
            self.ErrorOutputBottom.setFont(font)
            self.ErrorOutputBottom.setAlignment(QtCore.Qt.AlignCenter)
            self.ErrorOutputBottom.setObjectName("ErrorOutputBottom")
            self.ErrorOutputBottom.setText("Folder and Project Name are required.")

            self.ErrorBottomOutputFrame.show()

        elif folder == "":
            #Right Top Frame -ErrorOutputFrame
            self.ErrorBottomOutputFrame = QtWidgets.QFrame(self.RightBottomFrame)
            self.ErrorBottomOutputFrame.setGeometry(QtCore.QRect(45, 200, 321, 26))
            self.ErrorBottomOutputFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                    "border-style: solid;\n"
                                                    "border-color: rgb(0, 153, 255);\n"
                                                    "border-width: 2px;\n"
                                                    "border-radius: 10px;")
            self.ErrorBottomOutputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.ErrorBottomOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.ErrorBottomOutputFrame.setObjectName("ErrorTopOutputFrame")

            #Right Top Frame -ErrorOutputFrame -Error
            self.ErrorOutputBottom = QtWidgets.QLabel(self.ErrorBottomOutputFrame)
            self.ErrorOutputBottom.setGeometry(QtCore.QRect(11, 0, 301, 26))
            font = QtGui.QFont()
            font.setPointSize(8)
            self.ErrorOutputBottom.setFont(font)
            self.ErrorOutputBottom.setAlignment(QtCore.Qt.AlignCenter)
            self.ErrorOutputBottom.setObjectName("ErrorOutputBottom")
            self.ErrorOutputBottom.setText("Folder field is required.")

            self.ErrorBottomOutputFrame.show()



        elif project_name == "":
             #Right Top Frame -ErrorOutputFrame
            self.ErrorBottomOutputFrame = QtWidgets.QFrame(self.RightBottomFrame)
            self.ErrorBottomOutputFrame.setGeometry(QtCore.QRect(45, 200, 321, 26))
            self.ErrorBottomOutputFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                    "border-style: solid;\n"
                                                    "border-color: rgb(0, 153, 255);\n"
                                                    "border-width: 2px;\n"
                                                    "border-radius: 10px;")
            self.ErrorBottomOutputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.ErrorBottomOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.ErrorBottomOutputFrame.setObjectName("ErrorTopOutputFrame")

            #Right Top Frame -ErrorOutputFrame -Error
            self.ErrorOutputBottom = QtWidgets.QLabel(self.ErrorBottomOutputFrame)
            self.ErrorOutputBottom.setGeometry(QtCore.QRect(11, 0, 301, 26))
            font = QtGui.QFont()
            font.setPointSize(8)
            self.ErrorOutputBottom.setFont(font)
            self.ErrorOutputBottom.setAlignment(QtCore.Qt.AlignCenter)
            self.ErrorOutputBottom.setObjectName("ErrorOutputBottom")
            self.ErrorOutputBottom.setText("Project Name field is required.")

            self.ErrorBottomOutputFrame.show()
            
        else:
            conn = sqlite3.connect("project.db")
            c = conn.cursor()

            c.execute(f"INSERT INTO project VALUES ('{project_name}', '{self.responseBottom}')")

            conn.commit()
            conn.close()

            try:
                self.ErrorOutputTop.setText("Project Made")

            except:
                 #Right Top Frame -ErrorOutputFrame
                self.ErrorBottomOutputFrame = QtWidgets.QFrame(self.LeftBottomFrame)
                self.ErrorBottomOutputFrame.setGeometry(QtCore.QRect(45, 200, 321, 26))
                self.ErrorBottomOutputFrame.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                                        "border-style: solid;\n"
                                                        "border-color: rgb(0, 153, 255);\n"
                                                        "border-width: 2px;\n"
                                                        "border-radius: 10px;")
                self.ErrorBottomOutputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.ErrorBottomOutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.ErrorBottomOutputFrame.setObjectName("ErrorTopOutputFrame")

                #Right Top Frame -ErrorOutputFrame -Error
                self.ErrorOutputBottom = QtWidgets.QLabel(self.ErrorBottomOutputFrame)
                self.ErrorOutputBottom.setGeometry(QtCore.QRect(11, 0, 301, 26))
                font = QtGui.QFont()
                font.setPointSize(8)
                self.ErrorOutputBottom.setFont(font)
                self.ErrorOutputBottom.setAlignment(QtCore.Qt.AlignCenter)
                self.ErrorOutputBottom.setObjectName("ErrorOutputBottom")
                self.ErrorOutputBottom.setText("Project Made")

                self.ErrorBottomOutputFrame.show()

                self.ProjectList.clear()

                conn = sqlite3.connect("project.db")
                c = conn.cursor()

                c.execute("SELECT rowid, * FROM project")

                items = c.fetchall()
                none = str(items)

                if none == "[]":
                    pass

                else:
                    for item in items:
                        item_0 = QtWidgets.QTreeWidgetItem(self.ProjectList)

                        rowid = int(item[0])
                        name = item[1]
                        dir = item[2]

                        rowid = rowid - 1

                        try:
                            dir = dir.split("/Desktop")
                            dir = dir[1]

                        except:
                            dir = dir[0]

                        _translate = QtCore.QCoreApplication.translate
                        self.ProjectList.topLevelItem(rowid).setText(0, _translate("ConfigUI", f"{name}"))
                        self.ProjectList.topLevelItem(rowid).setText(1, _translate("ConfigUI", f"{dir}"))

    def test(self):
        self.ProjectList.clear()

        conn = sqlite3.connect("project.db")
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM project")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            pass

        else:
            for item in items:
                item_0 = QtWidgets.QTreeWidgetItem(self.ProjectList)

                rowid = int(item[0])
                name = item[1]
                dir = item[2]

                rowid = rowid - 1

                try:
                    dir = dir.split("/Desktop")
                    dir = dir[1]

                except:
                    dir = dir[0]

                _translate = QtCore.QCoreApplication.translate
                self.ProjectList.topLevelItem(rowid).setText(0, _translate("ConfigUI", f"{name}"))
                self.ProjectList.topLevelItem(rowid).setText(1, _translate("ConfigUI", f"{dir}"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigUI = QtWidgets.QMainWindow()
    ui = Ui_ConfigUI()
    ui.setupUi(ConfigUI, app)
    ConfigUI.show()
    sys.exit(app.exec_())
