# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setEnabled(True)
        self.heading.setGeometry(QtCore.QRect(410, 10, 341, 71))
        self.heading.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.heading.setFont(font)
        self.heading.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.heading.setMouseTracking(True)
        self.heading.setAutoFillBackground(True)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(160, 150, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 310, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.subred_drop = QtWidgets.QComboBox(self.centralwidget)
        self.subred_drop.setGeometry(QtCore.QRect(719, 305, 305, 55))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.subred_drop.setFont(font)
        self.subred_drop.setObjectName("subred_drop")
        items = ["" for x in subreddits]
        self.subred_drop.addItems(items)
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(710, 150, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(450, 400, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(self.search)
        self.post_label = QtWidgets.QLabel(self.centralwidget)
        self.post_label.setGeometry(QtCore.QRect(70, 510, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.post_label.setFont(font)
        self.post_label.setObjectName("post_label")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(70, 560, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.author_label = QtWidgets.QLabel(self.centralwidget)
        self.author_label.setGeometry(QtCore.QRect(70, 610, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.author_label.setFont(font)
        self.author_label.setObjectName("author_label")
        self.likes_label = QtWidgets.QLabel(self.centralwidget)
        self.likes_label.setGeometry(QtCore.QRect(70, 660, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.likes_label.setFont(font)
        self.likes_label.setObjectName("likes_label")
        self.comments_label = QtWidgets.QLabel(self.centralwidget)
        self.comments_label.setGeometry(QtCore.QRect(70, 710, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comments_label.setFont(font)
        self.comments_label.setObjectName("comments_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "r/stats"))
        self.add_button.setText(_translate("MainWindow", "Add Subreddit"))
        self.label.setText(_translate("MainWindow", "Get recent top comment of: r/"))
        for index, subreddit in enumerate(subreddits):
        	self.subred_drop.setItemText(index, _translate("MainWindow", subreddit))
        self.remove_button.setText(_translate("MainWindow", "Remove Subreddit"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.post_label.setText(_translate("MainWindow", "#:"))
        self.title_label.setText(_translate("MainWindow", "Title:"))
        self.author_label.setText(_translate("MainWindow", "Author:"))
        self.likes_label.setText(_translate("MainWindow", "Likes:"))
        self.comments_label.setText(_translate("MainWindow", "Comments:"))

    def search(self):
    	import reddit_scrape as rs
    	subreddit = self.subred_drop.currentText()
    	post = rs.scrape(subreddit)
    	self.post_label.setText("#: " + str(post[0]))
    	self.post_label.adjustSize()
    	self.title_label.setText("Title: " + post[1][0:30] + " ... " + post[1][-40:-(len(subreddit)+8)])
    	self.title_label.adjustSize()
    	self.author_label.setText("Author: " + post[2])
    	self.author_label.adjustSize()
    	self.likes_label.setText("Likes: " + str(post[3]))
    	self.likes_label.adjustSize()
    	self.comments_label.setText("Comments: " + post[4])
    	self.comments_label.adjustSize()

if __name__ == "__main__":
    import sys
    global subreddits
    subreddits = ["datascience", "MachineLearning", "pewdiepie"]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
