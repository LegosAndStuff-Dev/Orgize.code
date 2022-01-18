from pydoc import cli
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QModelIndex
import qrc
import sqlite3
import json


class MainDashboard(object):
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 566)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #Current Project / Title
        self.Title = QtWidgets.QFrame(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 10, 842, 40))
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
        self.CurrentProject.setGeometry(QtCore.QRect(1, 0, 842, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CurrentProject.setFont(font)
        self.CurrentProject.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentProject.setObjectName("CurrentProject")

        
        #Left Frame
        self.LeftFrame_todo = QtWidgets.QFrame(self.centralwidget)
        self.LeftFrame_todo.setGeometry(QtCore.QRect(10, 60, 411, 491))
        self.LeftFrame_todo.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                            "border-style: solid;\n"
                                            "border-color: rgb(43, 43, 43);\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 40px;")
        self.LeftFrame_todo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftFrame_todo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftFrame_todo.setObjectName("LeftFrame_todo")

        #Left Frame -list
        self.listWidget = QtWidgets.QListWidget(self.LeftFrame_todo)
        self.listWidget.setGeometry(QtCore.QRect(40, 141, 331, 331))
        self.listWidget.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 20px;\n")
        self.listWidget.setObjectName("listWidget")\

        #Left Frame -FrameLabel
        self.FrameLabel = QtWidgets.QFrame(self.LeftFrame_todo)
        self.FrameLabel.setGeometry(QtCore.QRect(20, 15, 371, 26))
        self.FrameLabel.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;")
        self.FrameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameLabel.setObjectName("FrameLabel")

        #Left Frame -FrameLabel -title
        self.label = QtWidgets.QLabel(self.FrameLabel)
        self.label.setGeometry(QtCore.QRect(1, 0, 371, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        #Left Frame -ItemLineEdit
        self.ItemLineEdit = QtWidgets.QLineEdit(self.LeftFrame_todo)
        self.ItemLineEdit.setGeometry(QtCore.QRect(40, 60, 331, 30))
        self.ItemLineEdit.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 8px;")
        self.ItemLineEdit.setObjectName("ItemLineEdit")

        #Left Frame -AddButton
        self.AddItem = QtWidgets.QPushButton(self.LeftFrame_todo)
        self.AddItem.setGeometry(QtCore.QRect(40, 105, 90, 23))
        self.AddItem.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(0, 153, 255);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 8px;")
        self.AddItem.setObjectName("AddItem")
        self.AddItem.clicked.connect(self.AddItemEvent)

        #Left Frame -DeleteButton
        self.DeleteItem = QtWidgets.QPushButton(self.LeftFrame_todo)
        self.DeleteItem.setGeometry(QtCore.QRect(161, 105, 90, 23))
        self.DeleteItem.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 8px;")
        self.DeleteItem.setObjectName("DeleteItem")
        self.DeleteItem.clicked.connect(self.DeleteItemEvent)

        #Left FRame -ClearAllButton
        self.ClearAll = QtWidgets.QPushButton(self.LeftFrame_todo)
        self.ClearAll.setGeometry(QtCore.QRect(281, 105, 90, 23))
        self.ClearAll.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(0, 153, 255);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 8px;")
        self.ClearAll.setObjectName("ClearAll")
        self.ClearAll.clicked.connect(self.ClearAllItemEvent)


        #Right Top Frame
        self.RightFrameTop_pick = QtWidgets.QFrame(self.centralwidget)
        self.RightFrameTop_pick.setGeometry(QtCore.QRect(440, 60, 411, 161))
        self.RightFrameTop_pick.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(43, 43, 43);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 40px;")
        self.RightFrameTop_pick.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightFrameTop_pick.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightFrameTop_pick.setObjectName("RightFrameTop_pick")

        #Right Top Frame -comboBox
        self.comboBox = QtWidgets.QComboBox(self.RightFrameTop_pick)
        self.comboBox.setGeometry(QtCore.QRect(40, 60, 331, 30))
        self.comboBox.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(0, 153, 255);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 8px;")
        self.comboBox.setObjectName("comboBox")

        conn = sqlite3.connect("project.db")
        c = conn.cursor()

        c.execute("SELECT * FROM project")

        items = c.fetchall()
        none = str(items)

        if none == None:
            self.comboBox.addItem("No Repos Found")

        else:
            for item in items:
                project_name = item[0]

                self.comboBox.addItem(project_name)

        #Right Top Frame -FrameLabel
        self.RightTopFrameTitle = QtWidgets.QFrame(self.RightFrameTop_pick)
        self.RightTopFrameTitle.setGeometry(QtCore.QRect(20, 15, 371, 26))
        self.RightTopFrameTitle.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;")
        self.RightTopFrameTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightTopFrameTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightTopFrameTitle.setObjectName("RightTopFrameTitle")

        #Right Top Frame -FrameLabel -title
        self.RightTopTitle = QtWidgets.QLabel(self.RightTopFrameTitle)
        self.RightTopTitle.setGeometry(QtCore.QRect(1, 0, 371, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RightTopTitle.setFont(font)
        self.RightTopTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.RightTopTitle.setObjectName("RightTopTitle")

        #Right Top Frame -ChoseProjectButton
        self.ChooseProject = QtWidgets.QPushButton(self.RightFrameTop_pick)
        self.ChooseProject.setGeometry(QtCore.QRect(145, 110, 111, 30))
        self.ChooseProject.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 8px;")
        self.ChooseProject.setObjectName("ChooseProject")
        self.ChooseProject.clicked.connect(self.ChooseProjectEvent)


        #Right Bottom Frame
        self.RightFrameBottom_file = QtWidgets.QFrame(self.centralwidget)
        self.RightFrameBottom_file.setGeometry(QtCore.QRect(440, 240, 411, 311))
        self.RightFrameBottom_file.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                                "border-style: solid;\n"
                                                "border-color: rgb(43, 43, 43);\n"
                                                "border-width: 2px;\n"
                                                "border-radius: 40px;")
        self.RightFrameBottom_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightFrameBottom_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightFrameBottom_file.setObjectName("RightFrameBottom_file")

        #Right Bottom Frame -FrameLabel
        self.RightBottomFrameTitle = QtWidgets.QFrame(self.RightFrameBottom_file)
        self.RightBottomFrameTitle.setGeometry(QtCore.QRect(20, 15, 371, 26))
        self.RightBottomFrameTitle.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                        "border-style: solid;\n"
                                        "border-color: rgb(0, 153, 255);\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;")
        self.RightBottomFrameTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightBottomFrameTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightBottomFrameTitle.setObjectName("RightBottomFrameTitle")

        #Right Bottom Frame -FrameLabel -title
        self.RightBottomTitle = QtWidgets.QLabel(self.RightBottomFrameTitle)
        self.RightBottomTitle.setGeometry(QtCore.QRect(1, 0, 371, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RightBottomTitle.setFont(font)
        self.RightBottomTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.RightBottomTitle.setObjectName("label_5")
        

        #Right Bottom Frame -FileTreeView
        self.treeView = QtWidgets.QTreeView(self.RightFrameBottom_file)
        self.treeView.setGeometry(QtCore.QRect(30, 50, 351, 241))
        self.treeView.setStyleSheet("background-color: rgb(0, 153, 255);\n"
                                    #"color: rgb(0, 153, 255);\n"
                                    "alternate-background-color: rgb(0, 153, 255);\n"
                                    "border-style: solid;\n"
                                    "border-color: rgb(0, 153, 255);\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 10px;")
        app.setStyleSheet("QHeaderView::section { background-color: rgb(0, 153, 255) }\n"
                          "QListWidget::item:selected {\n"
                                "background-color: rgb(0, 89, 148);\n"
                                "border-style: solid;\n"
                                "border-color: rgb(0, 153, 255);\n"
                                "border-width: 2px;\n"
                                "border-radius: 10px;\n"
                            "};\n")
        self.treeView.setObjectName("treeView")
        self.model = QFileSystemModel()
        self.treeView.setModel(self.model)
        self.treeView.setColumnWidth(0, 250)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)

        currect = self.comboBox.currentText()

        conn = sqlite3.connect("project.db")
        c = conn.cursor()

        c.execute(f"SELECT * FROM project WHERE project_name='{currect}'")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            self.CurrentProject.setText(f"Error")

        else:
            for item in items:
                name = item[0]
                dir = item[1]

            self.model.setRootPath(dir)
            self.treeView.setRootIndex(self.model.index(dir))

            self.CurrentProject.setText(f"{name} Dashboard")


        #Wave
        self.Wave = QtWidgets.QGraphicsView(self.centralwidget)
        self.Wave.setGeometry(QtCore.QRect(-52, 268, 957, 317))
        self.Wave.setStyleSheet("background-image: url(:/wave/Image/Wave/wave_2.png);\n"
                                "border-style: solid;\n"
                                "border-color: rgb(43, 43, 43);\n")
        self.Wave.setObjectName("Wave")

        #Raise
        self.Wave.raise_()
        self.LeftFrame_todo.raise_()
        self.RightFrameTop_pick.raise_()
        self.RightFrameBottom_file.raise_()
        #self.Title.raise_()

        #Other
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        #Add Items to todo
        currect = self.comboBox.currentText()

        self.CurrentProject.setText(f"{currect}⠀Dashboard")

        text = self.CurrentProject.text()

        project_name = text.split("⠀Dashboard")
        project_name = project_name[0]

        conn = sqlite3.connect("todo.db")
        c = conn.cursor()

        c.execute(f"SELECT * FROM todo WHERE project_name='{project_name}'")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            pass

        else:
            for item in items:
                todo = item[1]
                self.listWidget.addItem(todo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        currect = self.comboBox.currentText()

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orgize.code"))
        self.label.setText(_translate("MainWindow", "To Do List"))
        self.AddItem.setText(_translate("MainWindow", "Add Item"))
        self.DeleteItem.setText(_translate("MainWindow", "Delete Item"))
        self.ClearAll.setText(_translate("MainWindow", "Clear All"))
        self.RightTopTitle.setText(_translate("MainWindow", "Project Chooser"))
        self.ChooseProject.setText(_translate("MainWindow", "Change Project"))
        self.RightBottomTitle.setText(_translate("MainWindow", "Current File Directory"))
        self.CurrentProject.setText(_translate("MainWindow", f"{currect}⠀Dashboard"))

    def AddItemEvent(self):
        item = self.ItemLineEdit.text()

        self.listWidget.addItem(item)

        self.ItemLineEdit.setText("")
        
        clicked = self.CurrentProject.text()

        project_name = clicked.split("⠀Dashboard")

        conn = sqlite3.connect("todo.db")
        c = conn.cursor()

        c.execute(f"INSERT INTO todo VALUES ('{project_name[0]}', '{item}')")

        conn.commit()
        conn.close()

    def DeleteItemEvent(self):
        clicked = self.listWidget.currentRow()
        item = self.listWidget.currentItem().text()

        self.listWidget.takeItem(clicked)

        project_name = self.CurrentProject.text()

        project_name = project_name.split("⠀Dashboard")

        conn = sqlite3.connect("todo.db")
        c = conn.cursor()

        c.execute(f"DELETE FROM todo WHERE project_name='{project_name[0]}' AND todo='{item}'")

        conn.commit()
        conn.close()

    def ClearAllItemEvent(self):
        self.listWidget.clear()

        project_name = self.CurrentProject.text()

        project_name = project_name.split("⠀Dashboard")

        conn = sqlite3.connect("todo.db")
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM todo WHERE project_name='{project_name[0]}'")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            pass

        else:
            for item in items:
                rowid = item[0]

                c.execute(f"DELETE FROM todo WHERE rowid={rowid}")

                conn.commit()

            conn.close()


    def ChooseProjectEvent(self):
        currect = self.comboBox.currentText()

        conn = sqlite3.connect("project.db")
        c = conn.cursor()

        c.execute(f"SELECT * FROM project WHERE project_name='{currect}'")

        items = c.fetchall()
        none = str(items)

        if none == "[]":
            self.CurrentProject.setText(f"Error")

        else:
            for item in items:
                name = item[0]
                dir = item[1]

            self.model.setRootPath(dir)
            self.treeView.setRootIndex(self.model.index(dir))

            self.CurrentProject.setText(f"{name}⠀Dashboard")

            conn.close()

            self.listWidget.clear()

            try:
                name = name.split("⠀Dashboard")
                name = name[0]

            except:
                name = name

            conn = sqlite3.connect("todo.db")
            c = conn.cursor()

            c.execute(f"SELECT * FROM todo WHERE project_name='{name}'")

            items = c.fetchall()
            none = str(items)

            if none == "[]":
                pass

            else:
                for item in items:
                    todo = item[1]

                    self.listWidget.addItem(todo)

        #self.model.setRootPath(r'C:\Users\norbe\OneDrive\Desktop\Projects')
        #self.treeView.setRootIndex(self.model.index(r'C:\Users\norbe\OneDrive\Desktop\Projects'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainDashboard()
    ui.setupUi(MainWindow, app)
    MainWindow.show()
    sys.exit(app.exec_())
