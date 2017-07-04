# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created: Fri Jun 16 15:47:56 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
import sys
from os import path
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def resourse_path(self,relative_path):
        if hasattr(sys,"_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = path.abspath(".")
        return path.join(base_path,relative_path)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640,320)

        self.font = "font: 9pt \"微软雅黑\";"
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        #MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        palett1 = QtGui.QPalette()
        palett1.setBrush(QtGui.QPalette.Background,
                         QtGui.QBrush(QtGui.QPixmap(self.resourse_path('resourse/back_2.png'))))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setPalette(palett1)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resourse_path('resourse/3.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)




        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 600, 280))
        self.widget.setObjectName(_fromUtf8("widget"))
        #self.widget.setVisible(False)
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        #self.gridLayout.setSpacing(0)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        ################################################################
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setVisible(False)
        self.widget2.setGeometry(QtCore.QRect(20, 300, 600, 280))
        self.widget2.setObjectName(_fromUtf8("widget2"))

        self.gridLayout2 = QtGui.QGridLayout(self.widget2)
        self.gridLayout2.setMargin(0)
        #self.gridLayout.setSpacing(0)
        self.gridLayout2.setHorizontalSpacing(15)
        self.gridLayout2.setVerticalSpacing(10)
        self.gridLayout2.setObjectName(_fromUtf8("gridLayout2"))


        self.textBrowser = QtGui.QTextBrowser(self.widget)
        #self.textBrowser.setGeometry(QtCore.QRect(380, 10, 240, 200))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 4, 5, 2)
        '''#端口开关间隔
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        #反复开关端口
        self.pushButton_6 = QtGui.QPushButton(self.widget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 6, 3, 1, 1)
        '''
        ########################################
        self.pushButton_7 = QtGui.QPushButton(self.widget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 7, 3, 1, 1)
        #全部停止
        self.pushButton_stopall = QtGui.QPushButton(self.widget)
        self.pushButton_stopall.setObjectName(_fromUtf8("pushButton_stopall"))
        self.gridLayout.addWidget(self.pushButton_stopall, 7, 1, 1, 1)

        self.lineEdit_4 = QtGui.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        #录像间隔数字
        self.lineEdit_5 = QtGui.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        ###新增 断连视频按钮
        self.pushButton_recv = QtGui.QPushButton(self.widget)
        self.pushButton_recv.setObjectName(_fromUtf8("pushButton_recv"))
        self.gridLayout.addWidget(self.pushButton_recv, 6, 3, 1, 1)

        #断连label
        self.label_recv = QtGui.QLabel(self.widget)
        self.label_recv.setObjectName(_fromUtf8("label_recv"))
        self.gridLayout.addWidget(self.label_recv, 6, 0, 1, 1)
        #断连间隔输入
        self.lineEdit_recv = QtGui.QLineEdit(self.widget)
        self.lineEdit_recv.setObjectName(_fromUtf8("lineEdit_recv"))
        self.gridLayout.addWidget(self.lineEdit_recv, 6, 1, 1, 1)
        #无用，占位置
        self.label_no = QtGui.QLabel(self.widget)
        self.label_no.setObjectName(_fromUtf8("label_no"))
        self.gridLayout.addWidget(self.label_no, 7, 0, 1, 1)


        #CGI修改间隔label
        self.label_cgi_time = QtGui.QLabel(self.widget2)
        self.label_cgi_time.setObjectName(_fromUtf8("label_cgi_time"))
        self.gridLayout2.addWidget(self.label_cgi_time, 0, 0, 1, 1)
        #CGI 修改间隔
        self.lineEdit_cgi_timeinput = QtGui.QLineEdit(self.widget2)
        self.lineEdit_cgi_timeinput.setObjectName(_fromUtf8("lineEdit_cgi_timeinput"))
        self.gridLayout2.addWidget(self.lineEdit_cgi_timeinput, 0, 1, 1, 1)
        #CGI Button
        self.pushButton_cgi = QtGui.QPushButton(self.widget2)
        self.pushButton_cgi.setObjectName(_fromUtf8("pushButton_cgi"))
        self.gridLayout2.addWidget(self.pushButton_cgi, 0, 2, 1, 1)

        #站位
        self.label_99 = QtGui.QLabel(self.widget2)
        self.label_99.setObjectName(_fromUtf8("label_99"))
        self.gridLayout2.addWidget(self.label_99, 0, 3, 1, 1)
        #站位
        self.label_98 = QtGui.QLabel(self.widget2)
        self.label_98.setObjectName(_fromUtf8("label_98"))
        self.gridLayout2.addWidget(self.label_98, 0, 4, 1, 1)

        # CGI 修改地址
        self.lineEdit_cgi_address = QtGui.QLineEdit(self.widget2)
        self.lineEdit_cgi_address.setObjectName(_fromUtf8("lineEdit_cgi_address"))
        #self.gridLayout.addWidget(self.lineEdit_cgi_address, 9, 0, 1, 1)
        self.gridLayout2.addWidget(self.lineEdit_cgi_address,1, 1, 1,2)
        # CGI show
        self.pushButton_cgi_show = QtGui.QPushButton(self.widget)
        self.pushButton_cgi_show.setObjectName(_fromUtf8("pushButton_cgi_show"))
        self.gridLayout.addWidget(self.pushButton_cgi_show, 7, 4, 1, 1)
        # CGI hide
        self.pushButton_cgi_hide = QtGui.QPushButton(self.widget)
        self.pushButton_cgi_hide.setObjectName(_fromUtf8("pushButton_cgi_hide"))
        self.gridLayout.addWidget(self.pushButton_cgi_hide, 7, 4, 1, 1)
        self.pushButton_cgi_hide.setVisible(False)

        '''
        #通道选择下拉框
        self.comboBox_chn= QtGui.QComboBox(self.centralwidget)
        #self.comboBox_chn.addItem('20D')
        #self.comboBox_chn.addItem('35')
        #self.comboBox_chn.addItem('36')
        #self.comboBox_chn.addItem('98M')
        self.comboBox_chn.move(105, 270)
        #主副码流选择下拉框
        self.comboBox_maliu = QtGui.QComboBox(self.centralwidget)
        self.comboBox_maliu.addItem(u'1主码流')
        self.comboBox_maliu.addItem(u'2副码流')
        #self.comboBox_maliu.addItem(u'2副码流')
        self.comboBox_maliu.move(195, 270)
        '''
        '''
        #CGI1输入label
        self.label_cgi = QtGui.QLabel(self.widget)
        self.label_cgi.setObjectName(_fromUtf8("label_cgi"))
        self.gridLayout.addWidget(self.label_cgi, 9, 0, 1, 1)
        '''
        ############

        #CGI1输入输入
        self.TextEdit_cgi1 = QtGui.QTextEdit(self.widget2)
        self.TextEdit_cgi1.setAlignment(QtCore.Qt.AlignLeft)
        #self.TextEdit_cgi1.setGeometry(QtCore.QRect(20, 500, 300, 220))
        self.TextEdit_cgi1.setObjectName(_fromUtf8("TextEdit_cgi1"))
        self.gridLayout2.addWidget(self.TextEdit_cgi1, 2, 1, 1, 2)
        #self.TextEdit_cgi1.wordWrap
        #CGI2输入输入
        self.TextEdit_cgi2 = QtGui.QTextEdit(self.widget2)
        #self.TextEdit_cgi2.setGeometry(QtCore.QRect(360, 500, 300, 220))
        self.TextEdit_cgi2.setObjectName(_fromUtf8("TextEdit_cgi2"))
        self.gridLayout2.addWidget(self.TextEdit_cgi2, 2, 3, 1, 2)

        #self.gridLayout.addWidget(self.lineEdit_cgi1, 10, 1, 5, 1)
        '''
        ###Media
        self.media = Phonon.MediaObject(self)
        self.video=Phonon.VideoWidget(self)
        self.video.setGeometry(QtCore.QRect(380, 20, 355, 200))
        '''

        '''
        #录像打包有效时长
        self.lineEdit_5 = QtGui.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        '''
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 4, 3, 1, 1)
        '''#端口开关间隔数字
        self.lineEdit_6 = QtGui.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout.addWidget(self.lineEdit_6, 6, 1, 1, 1)
        '''
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.widget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 2, 3, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        #录像打包间隔
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)


        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.changemain(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changemain_old(self, MainWindow1):
        MainWindow1.resize(640, 320)

    def changemain(self,MainWindow):
        MainWindow.resize(640, 600)
        #MainWindow.
        #self.widget2.setVisible(True)


    def retranslateUi(self, MainWindow):
        self.cgi_add='/CGI/Streaming/channels/1/type/1'
        self.cgi1="""<?xml version="1.0" encoding="UTF-8"?>
<StreamingChannel>
<id>1</id>
<channelName>MainStream</channelName>
<Video>
<videoCodecType opt="H.264B,H.264M,H.264H,MotionJPEG,H.265">H.264H</videoCodecType>
<videoResolutionWidth opt="1080,960,720,1920,1280,1280,640,704">1920</videoResolutionWidth>
<videoResolutionHeight opt="1920,1280,1280,1080,960,720,480,576">1080</videoResolutionHeight>
<fixedQuality>good</fixedQuality>
<maxFrameRate opt="25,20,15,10,5,1">25</maxFrameRate>
<H264Profile>High</H264Profile>
<GovLength>50</GovLength>
<SVC>true</SVC>
<np-Mode>PAL</np-Mode>
<priorityMode>FramRate</priorityMode>
<corridorMode>OFF</corridorMode>
<channelType>LocalChannel</channelType>
<enctypeType>NoEnctype</enctypeType>
<password></password>
<electronicImageStab>ON</electronicImageStab>
<smoothing>-1</smoothing>
<SPlus265>false</SPlus265>
<videoQualityControlType>VBR</videoQualityControlType>
<vbrUpperCap>4096</vbrUpperCap>
<vbrLowerCap>128</vbrLowerCap>
<constantBitRate>4096</constantBitRate>
</Video>
<Audio>
<enabled>true</enabled>
</Audio>
</StreamingChannel>"""
        self.cgi2="""<?xml version="1.0" encoding="UTF-8"?>
<StreamingChannel>
<id>1</id>
<channelName>MainStream</channelName>
<Video>
<videoCodecType opt="H.264B,H.264M,H.264H,MotionJPEG,H.265">H.264H</videoCodecType>
<videoResolutionWidth opt="1080,960,720,1920,1280,1280,640,704">1280</videoResolutionWidth>
<videoResolutionHeight opt="1920,1280,1280,1080,960,720,480,576">720</videoResolutionHeight>
<fixedQuality>good</fixedQuality>
<maxFrameRate opt="25,20,15,10,5,1">25</maxFrameRate>
<H264Profile>High</H264Profile>
<GovLength>50</GovLength>
<SVC>true</SVC>
<np-Mode>PAL</np-Mode>
<priorityMode>FramRate</priorityMode>
<corridorMode>OFF</corridorMode>
<channelType>LocalChannel</channelType>
<enctypeType>NoEnctype</enctypeType>
<password></password>
<electronicImageStab>ON</electronicImageStab>
<smoothing>-1</smoothing>
<SPlus265>false</SPlus265>
<videoQualityControlType>VBR</videoQualityControlType>
<vbrUpperCap>4096</vbrUpperCap>
<vbrLowerCap>128</vbrLowerCap>
<constantBitRate>4096</constantBitRate>
</Video>
<Audio>
<enabled>true</enabled>
</Audio>
</StreamingChannel>"""
        MainWindow.setWindowTitle(_translate("MainWindow", "通用测试工具", None))
        #self.label_6.setText(_translate("MainWindow", "端口开关间隔", None))
        #self.pushButton_6.setText(_translate("MainWindow", "反复开关端口", None))
        self.pushButton_stopall.setText(_translate("MainWindow", "全部停止", None))
        self.pushButton_7.setText(_translate("MainWindow", "全部消警", None))
        self.lineEdit_4.setText(_translate("MainWindow", "120", None))
        self.lineEdit_5.setText(_translate("MainWindow", "30", None))
        self.lineEdit_recv.setText(_translate("MainWindow", "5", None))
        self.pushButton_recv.setText(_translate("MainWindow", "开始断连", None))
        self.pushButton_4.setText(_translate("MainWindow", "反复开关手动", None))
        #self.lineEdit_6.setText(_translate("MainWindow", "60", None))
        self.lineEdit_3.setText(_translate("MainWindow", "1111", None))
        self.pushButton_5.setText(_translate("MainWindow", "Telnet开启", None))
        self.pushButton_3.setText(_translate("MainWindow", "开始重启", None))
        self.pushButton_2.setText(_translate("MainWindow", "注销", None))
        self.label_recv.setText(_translate("MainWindow", "视频断连间隔", None))
        self.label_5.setText(_translate("MainWindow", "录像打包间隔", None))
        self.label_4.setText(_translate("MainWindow", "重启间隔", None))
        self.label_3.setText(_translate("MainWindow", "密码", None))
        self.pushButton.setText(_translate("MainWindow", "登录", None))
        self.lineEdit.setText(_translate("MainWindow", "192.168.18.131", None))
        self.label.setText(_translate("MainWindow", "IP", None))
        self.label_2.setText(_translate("MainWindow", "帐号", None))
        self.lineEdit_2.setText(_translate("MainWindow", "admin", None))
        self.label_cgi_time.setText(_translate("MainWindow", "CGI修改间隔", None))
        self.lineEdit_cgi_timeinput.setText(_translate("MainWindow", "10", None))
        self.pushButton_cgi.setText(_translate("MainWindow", "开始切换", None))
        self.lineEdit_cgi_address.setText(_translate("MainWindow", self.cgi_add, None))
        self.TextEdit_cgi1.setText(_translate("MainWindow", self.cgi1, None))
        self.TextEdit_cgi2.setText(_translate("MainWindow", self.cgi2, None))
        self.pushButton_cgi_show.setText(_translate("MainWindow", "显示CGI输入框", None))
        self.pushButton_cgi_hide.setText(_translate("MainWindow", "隐藏", None))
        #self.label_cgi.setText(_translate("MainWindow", "CGI", None))
        self.label_99.setText(_translate("MainWindow", "      ", None))
        self.label_98.setText(_translate("MainWindow", "      ", None))
