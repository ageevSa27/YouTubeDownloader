# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pafy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 271)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 170, 131, 21))
        self.comboBox.setVisible(False)
        self.comboBox.setObjectName("comboBox")
        self.url_line = QtWidgets.QLineEdit(self.centralwidget)
        self.url_line.setGeometry(QtCore.QRect(40, 20, 211, 21))
        self.url_line.setObjectName("url_line")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(350, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(340, 200, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_download.setFont(font)
        self.btn_download.setObjectName("btn_download")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 240, 118, 23))
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)

        self.timer = QtCore.QBasicTimer()
        self.timer.start(100, self.centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.action()

    def action(self):
        self.btn_ok.clicked.connect(self.get_url)
        self.btn_download.clicked.connect(self.download)

    def get_url(self):

        try:
            self.link = self.url_line.text()
            self.video = pafy.new(self.link)
            self.data = self.video.streams
            self.title = self.video.title

            available_streams = {}
            count = 1
            for i in self.data:
                available_streams[count] = i
                self.strs = str(available_streams[count])
                self.strs = self.strs.partition(':')
                self.comboBox.addItem(self.strs[2])
                count = + 1
            self.path = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "сохраните видео", self.title,
                                                              "MP4 Video file (.mp4, .m4v, .mp4v, .3g2, .3gp2, .3gp, .3gpp)")
            self.comboBox.setVisible(True)
        except:
            print("ищи ошибки")

    def download(self):

        self.index = self.comboBox.currentIndex()
        print(type(self.path))
        print(self.path)
        self.d = self.data[self.index].download(filepath=self.path[0] + '.mp4')
        print('daaa')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTubeDownloader"))
        self.url_line.setPlaceholderText(_translate("MainWindow", "Введите ссылку"))
        self.btn_ok.setText(_translate("MainWindow", "Ок"))
        self.btn_download.setText(_translate("MainWindow", "скачать"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
