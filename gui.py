import os
import getpass

from video import YoutubeVideo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

user = getpass.getuser()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setStyleSheet("background-color: rgb(200, 200, 200);\n""color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.head_frame = QtWidgets.QFrame(self.centralwidget)
        self.head_frame.setGeometry(QtCore.QRect(0, 0, 600, 50))
        self.head_frame.setStyleSheet("color: rgb(0, 0, 0);")
        self.head_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.head_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head_frame.setObjectName("head_frame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.head_frame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.heading = QtWidgets.QLabel(self.head_frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.heading)

        self.link_frame = QtWidgets.QFrame(self.centralwidget)
        self.link_frame.setGeometry(QtCore.QRect(0, 50, 600, 60))
        self.link_frame.setStatusTip("")
        self.link_frame.setStyleSheet("color: rgb(0, 0, 0);")
        self.link_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.link_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.link_frame.setObjectName("link_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.link_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.link_label = QtWidgets.QLabel(self.link_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.link_label.setFont(font)
        self.link_label.setObjectName("link_label")
        self.horizontalLayout.addWidget(self.link_label)

        self.link_edit = QtWidgets.QLineEdit(self.link_frame)
        self.link_edit.setObjectName("link_edit")
        self.horizontalLayout.addWidget(self.link_edit)

        self.search = QtWidgets.QPushButton(self.link_frame)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)

        self.detail_frame = QtWidgets.QFrame(self.centralwidget)
        self.detail_frame.setGeometry(QtCore.QRect(0, 110, 600, 150))
        self.detail_frame.setStatusTip("")
        self.detail_frame.setStyleSheet("color: rgb(0, 0, 0);")
        self.detail_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detail_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detail_frame.setObjectName("detail_frame")

        self.gridLayout = QtWidgets.QGridLayout(self.detail_frame)
        self.gridLayout.setObjectName("gridLayout")

        self.title_label = QtWidgets.QLabel(self.detail_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)

        self.title_edit = QtWidgets.QLineEdit(self.detail_frame)
        self.title_edit.setReadOnly(True)
        self.title_edit.setObjectName("title_edit")
        self.gridLayout.addWidget(self.title_edit, 0, 1, 1, 5)

        self.author_label = QtWidgets.QLabel(self.detail_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.author_label.setFont(font)
        self.author_label.setObjectName("author_label")
        self.gridLayout.addWidget(self.author_label, 1, 0, 1, 1)

        self.author_edit = QtWidgets.QLineEdit(self.detail_frame)
        self.author_edit.setReadOnly(True)
        self.author_edit.setObjectName("author_edit")
        self.gridLayout.addWidget(self.author_edit, 1, 1, 1, 5)

        self.length_label = QtWidgets.QLabel(self.detail_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.length_label.setFont(font)
        self.length_label.setObjectName("length_label")
        self.gridLayout.addWidget(self.length_label, 2, 0, 1, 1)

        self.length_edit = QtWidgets.QLineEdit(self.detail_frame)
        self.length_edit.setReadOnly(True)
        self.length_edit.setObjectName("length_edit")
        self.gridLayout.addWidget(self.length_edit, 2, 1, 1, 1)

        self.view_label = QtWidgets.QLabel(self.detail_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.view_label.setFont(font)
        self.view_label.setObjectName("view_label")
        self.gridLayout.addWidget(self.view_label, 2, 2, 1, 1)

        self.view_edit = QtWidgets.QLineEdit(self.detail_frame)
        self.view_edit.setReadOnly(True)
        self.view_edit.setObjectName("view_edit")
        self.gridLayout.addWidget(self.view_edit, 2, 3, 1, 1)

        self.rating_label = QtWidgets.QLabel(self.detail_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rating_label.setFont(font)
        self.rating_label.setObjectName("rating_label")
        self.gridLayout.addWidget(self.rating_label, 2, 4, 1, 1)

        self.rating_edit = QtWidgets.QLineEdit(self.detail_frame)
        self.rating_edit.setReadOnly(True)
        self.rating_edit.setObjectName("rating_edit")
        self.gridLayout.addWidget(self.rating_edit, 2, 5, 1, 1)

        self.download_frame = QtWidgets.QFrame(self.centralwidget)
        self.download_frame.setGeometry(QtCore.QRect(0, 260, 600, 220))
        self.download_frame.setStatusTip("")
        self.download_frame.setStyleSheet("color: rgb(0, 0, 0);")
        self.download_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.download_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.download_frame.setObjectName("download_frame")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.download_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.path_label = QtWidgets.QLabel(self.download_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.gridLayout_2.addWidget(self.path_label, 0, 0, 1, 1)

        self.path_edit = QtWidgets.QLineEdit(self.download_frame)
        self.path_edit.setObjectName("path_edit")
        self.gridLayout_2.addWidget(self.path_edit, 0, 1, 1, 5)

        if os.path.isdir('/home/' + user + '/Download'):
            self.path_edit.setText('/home/' + user + '/Download')
        elif os.path.isdir('/home/' + user + '/download'):
            self.path_edit.setText('/home/' + user + '/download')
        elif os.path.isdir('/home/' + user + '/Downloads'):
            self.path_edit.setText('/home/' + user + '/Downloads')
        elif os.path.isdir('/home/' + user + '/downloads'):
            self.path_edit.setText('/home/' + user + '/downloads')
        else:
            self.path_edit.setText('/home/' + user)

        self.browse = QtWidgets.QPushButton(self.download_frame)
        self.browse.setObjectName("browse")
        self.gridLayout_2.addWidget(self.browse, 0, 6, 1, 1)

        self.stream_label = QtWidgets.QLabel(self.download_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stream_label.setFont(font)
        self.stream_label.setObjectName("stream_label")
        self.gridLayout_2.addWidget(self.stream_label, 1, 0, 1, 1)

        self.stream_combo = QtWidgets.QComboBox(self.download_frame)
        self.stream_combo.setObjectName("stream_combo")
        self.gridLayout_2.addWidget(self.stream_combo, 1, 1, 1, 6)

        self.audio_label = QtWidgets.QLabel(self.download_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.audio_label.setFont(font)
        self.audio_label.setObjectName("audio_label")
        self.gridLayout_2.addWidget(self.audio_label, 2, 0, 1, 1)

        self.audio_combo = QtWidgets.QComboBox(self.download_frame)
        self.audio_combo.setObjectName("audio_combo")
        self.gridLayout_2.addWidget(self.audio_combo, 2, 1, 1, 6)

        self.caption_label = QtWidgets.QLabel(self.download_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.caption_label.setFont(font)
        self.caption_label.setObjectName("caption_label")
        self.gridLayout_2.addWidget(self.caption_label, 3, 0, 1, 1)

        self.caption_combo = QtWidgets.QComboBox(self.download_frame)
        self.caption_combo.setObjectName("caption_combo")
        self.gridLayout_2.addWidget(self.caption_combo, 3, 1, 1, 6)

        self.download = QtWidgets.QPushButton(self.download_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download.sizePolicy().hasHeightForWidth())
        self.download.setSizePolicy(sizePolicy)
        self.download.setObjectName("download")
        self.gridLayout_2.addWidget(self.download, 4, 3, 1, 1)

        self.progress_frame = QtWidgets.QFrame(self.centralwidget)
        self.progress_frame.setGeometry(QtCore.QRect(0, 480, 600, 50))
        self.progress_frame.setStyleSheet("color: rgb(0, 0, 0);")
        self.progress_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.progress_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.progress_frame.setObjectName("progress_frame")

        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.progress_frame)
        # self.verticalLayout_2.setObjectName("verticalLayout_2")

        # self.progress_bar = QtWidgets.QProgressBar(self.progress_frame)
        # self.progress_bar.setProperty("value", 0)
        # self.progress_bar.setObjectName("progress_bar")
        # self.verticalLayout_2.addWidget(self.progress_bar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 30))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Video Downloader"))

        self.head_frame.setStatusTip(_translate("MainWindow", "Youtube Video Downloader"))
        self.heading.setStatusTip(_translate("MainWindow", "Youtube Video Downloader"))
        self.heading.setText(_translate("MainWindow", "Youtube Video Downloader"))
        self.link_label.setStatusTip(_translate("MainWindow", "Link"))
        self.link_label.setText(_translate("MainWindow", "Link:"))
        self.link_edit.setStatusTip(_translate("MainWindow", "Link"))
        self.search.setStatusTip(_translate("MainWindow", "Search"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.title_label.setStatusTip(_translate("MainWindow", "Title"))
        self.title_label.setText(_translate("MainWindow", "Title:"))
        self.title_edit.setStatusTip(_translate("MainWindow", "Title"))
        self.author_label.setStatusTip(_translate("MainWindow", "Author"))
        self.author_label.setText(_translate("MainWindow", "Author:"))
        self.author_edit.setStatusTip(_translate("MainWindow", "Author"))
        self.length_label.setStatusTip(_translate("MainWindow", "Length"))
        self.length_label.setText(_translate("MainWindow", "Length:"))
        self.length_edit.setStatusTip(_translate("MainWindow", "Length"))
        self.view_label.setStatusTip(_translate("MainWindow", "Views"))
        self.view_label.setText(_translate("MainWindow", "Views:"))
        self.view_edit.setStatusTip(_translate("MainWindow", "Views"))
        self.rating_label.setStatusTip(_translate("MainWindow", "Rating"))
        self.rating_label.setText(_translate("MainWindow", "Rating:"))
        self.rating_edit.setStatusTip(_translate("MainWindow", "Rating"))
        self.path_label.setStatusTip(_translate("MainWindow", "Path"))
        self.path_label.setText(_translate("MainWindow", "Path:"))
        self.path_edit.setStatusTip(_translate("MainWindow", "Path"))
        self.browse.setStatusTip(_translate("MainWindow", "Browse"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.stream_label.setStatusTip(_translate("MainWindow", "Stream"))
        self.stream_label.setText(_translate("MainWindow", "Streams:"))
        self.stream_combo.setStatusTip(_translate("MainWindow", "Stream"))
        self.audio_label.setStatusTip(_translate("MainWindow", "Audio"))
        self.audio_label.setText(_translate("MainWindow", "Audios:"))
        self.audio_combo.setStatusTip(_translate("MainWindow", "Audio"))
        self.caption_label.setStatusTip(_translate("MainWindow", "Caption"))
        self.caption_label.setText(_translate("MainWindow", "Captions:"))
        self.caption_combo.setStatusTip(_translate("MainWindow", "Caption"))
        self.download.setStatusTip(_translate("MainWindow", "Download"))
        self.download.setText(_translate("MainWindow", "Download"))
        # self.progress_frame.setStatusTip(_translate("MainWindow", "Progress Bar"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.search.clicked.connect(self.search_button_clicked)
        self.browse.clicked.connect(self.browse_button_clicked)
        self.download.clicked.connect(self.download_button_clicked)

    @pyqtSlot()
    def search_button_clicked(self):
        link = self.link_edit.text()
        self.video, self.video_data = YoutubeVideo.get_video(link)

        if self.video == 0:
            return

        if self.video_data == 0:
            return

        self.title_edit.setText(self.video_data['title'])
        self.author_edit.setText(self.video_data['author'])
        self.length_edit.setText(str(self.video_data['length']) + ' s')
        self.view_edit.setText(str(self.video_data['views']))
        self.rating_edit.setText(str(self.video_data['rating']))

        self.stream_combo.clear()
        for stream in self.video_data['streams']:
            self.stream_combo.addItem(str(stream))

        self.audio_combo.clear()
        for audio in self.video_data['audios']:
            self.audio_combo.addItem(str(audio))

        self.caption_combo.clear()
        for caption in self.video_data['captions']:
            self.caption_combo.addItem(str(caption))

    @pyqtSlot()
    def browse_button_clicked(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(directory='/home/' + user)
        self.path_edit.setText(path)
        print(path)

    @pyqtSlot()
    def download_button_clicked(self):
        video = self.stream_combo.currentText()
        audio = self.audio_combo.currentText()
        caption = self.caption_combo.currentText()

        video_itag = ''
        audio_itag = ''
        caption_lang = ''

        if video != '':
            video_itag = video.split('"')[1]

        if audio != '':
            audio_itag = audio.split('"')[1]

        if caption != '':
            caption_lang = caption.split('"')[3]

        YoutubeVideo.download_video(
            self.video,
            self.video_data['title'],
            self.video_data['description'],
            self.path_edit.text(),
            video_itag,
            audio_itag,
            caption_lang
        )
