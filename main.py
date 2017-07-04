# -*- coding: utf-8 -*-


""" 
Module implementing Dialog. 
Design by :zyx
date:2017-6-30
"""




from PyQt4.QtCore import pyqtSignature,pyqtSignal
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox
import requests
#from PyQt4.QtCore import  Qt
from sys import argv,exit
from ui import Ui_MainWindow

#import win32api,win32gui
from datetime import datetime
import PyQt4.QtGui

from dll import *

#from pc_qiubai import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
	""" 
	Class documentation goes here. 
	"""
	#global times_print
	#times_print=1
	def __init__(self, parent=None):
		""" 
		初始化界面
		"""
		QMainWindow.__init__(self, parent)
		self.setupUi(self)                 #使用QMainWindow来初始化setupUI
		#self.user="root"
		#self.password = "dvrs16"
		#self.now_days = []
		#self.times_write = 0
		#拼接exe所在路径下的dll文件夹
		self.path_pinjie = os.getcwd() + '\\dll\\'
		self.dll = Dll()
		#self.msg_err = QMessageBox(QMessageBox.Warning, u"注意: " , u"出问题了，检查一下吧！")
		self.times = 1
		self.flag_forcgi = 1
		#self.pushButton.released.connect(self.on_pushButton_released)

	def time_format(self):#获取当天时间，写入最新检查时间时使用
		now=datetime.now()
		now_for=now.strftime('%Y/%m/%d')
		return now_for

	def get_ip(self):
		self.ip= str(self.lineEdit.text())
		self.user=str(self.lineEdit_2.text())
		self.passwd=str(self.lineEdit_3.text())
		pass

	@pyqtSignature("")
	def on_pushButton_released(self):
		""" 
		Slot documentation goes here. 
		"""
		self.get_ip()

		try:
			self.dll.Setup(self.path_pinjie,self.ip, self.user,self.passwd)
			self.id=self.dll.Logon()
			# status_telback.append(str(ip_in))
			if self.id!=None:
				text_output = self.ip + ' ok'
				id_output='Logon id is: '+str(self.id)
				self.textBrowser.clear()
				self.textBrowser.append(text_output)
				self.textBrowser.append(id_output)
				self.chn_nums = self.dll.GetChnNum(self.id)
				for i in range(1,self.chn_nums+1):
					self.comboBox_chn.addItem(str(i))
			else:
				self.textBrowser.append(u'登录失败啦！检查一下！')
		except Exception as err:
			print Exception, ':', err
			#self.msg_err.exec_()

	@pyqtSignature("")
	def on_pushButton_2_clicked(self):
		try:
			print  self.ip
		except Exception:
			self.textBrowser.append(u'没有登录，请先登陆！')
		try:
			self.logoff_state=self.dll.LogOff(self.id)
			if self.logoff_state==0:
				self.textBrowser.append(u'注销成功！')
				self.id=''
			else:
				self.textBrowser.append(u'注销失败啦！登录了吗？')
		except Exception as err_logoff:
			print Exception,':',err_logoff
			#self.msg_err.exec_()

	@pyqtSignature("")
	def on_pushButton_5_clicked(self):
		try:
			print  self.ip
		except Exception:
			self.textBrowser.append(u'没有登录，请先登陆！')
		try:
			self.telnet_state=self.dll.TelnetOpen(self.id)
			if self.telnet_state == 0:
				self.textBrowser.append(u'Telnet 开启成功！')
			else:
				self.textBrowser.append(u'Telnet 开启失败！检查设备在线吗？登录了吗？')
		except Exception as err_telnet:
			print Exception,':',err_telnet


	@pyqtSignature("")
	def on_pushButton_3_released(self):
		self.flag = 1
		try:
			print  self.ip
		except Exception:
			self.textBrowser.append(u'没有登录，请先登陆！')
		self.timedelay_reboot = self.lineEdit_4.text()
		if 1:
			self.pushButton_3.setDisabled(True)

			from Video_thread import DoThread
			self.dosleep = DoThread(self.timedelay_reboot)
			self.dosleep.finishSignal.connect(self.DoReboot)
			# , Qt.QueuedConnection
			if self.flag==1:
				self.dosleep.start()
			else:
				self.dosleep.stop()



	def DoReboot(self):

		try:
			self.reboot_state = self.dll.Reboot(self.id)
				#for i in range(int(self.timedelay)):
					#i+=1
					#QThread.msleep(100)
			if self.reboot_state == 0:

				reboot_log = u'重启成功！' + ':' + str(self.times)
				self.textBrowser.append(reboot_log)
			# self.textBrowser.append(out_log)
			else:
				print self.reboot_state
				self.textBrowser.append(u'重启失败！检查设备在线吗？登录了吗？')
		except Exception as err_reboot:
			print Exception,':',err_reboot
		#time.sleep(int(self.timedelay))
		if self.flag == 1:
			self.dosleep.start()
			self.times += 1
		else:
			self.dosleep.stop()

###############################################################
		#开关手动
	@pyqtSignature("")
	def on_pushButton_4_released(self):
		self.flag = 1
		try:
			print  self.ip
		except Exception:
			self.textBrowser.append(u'没有登录，请先登陆！')
		self.timedelay_video = self.lineEdit_5.text()

		if 1:
			self.pushButton_4.setDisabled(True)

			from Video_thread import DoThread
			self.dosleep = DoThread(self.timedelay_video)
			self.dosleep.finishSignal.connect(self.DoRecord)
			# , Qt.QueuedConnection
			if self.flag==1:
				self.dosleep.start()
			else:
				self.dosleep.stop()

	def DoRecord(self):
		self.chn_nums = self.dll.GetChnNum(self.id)

		#while 1:
		dabao_log=u'成功打包了%s次' %self.times
		self.textBrowser.append(dabao_log)
		try:
			for i_chn in range(0,int(self.chn_nums)):
				man_state = 0
				self.manual=self.dll.Manual(self.id,i_chn,man_state)
				if self.manual==0:
					#print
					out_log=u'关闭手动录像成功！'+':'+str(i_chn)
					#self.textBrowser.append(out_log)
				else:
					print self.manual
					#print 'manman'
					self.textBrowser.append(u'关闭手动录像失败！检查设备在线吗？登录了吗？')
			#time.sleep(int(self.timedelay_video))
			print '%s times off !' % self.times
			time.sleep(1)
			if self.flag == 1:
				self.dosleep.start()
				self.times += 1
			else:
				self.dosleep.stop()


			for j_chn in range (0,int(self.chn_nums)+1):
				man_state=1
				self.manual = self.dll.Manual(self.id, j_chn, man_state)
				if self.manual == 0:
					# print '000000'
					out_log = u'开启手动录像成功！' + ':' + str(j_chn)
					#self.textBrowser.append(out_log)
				else:
					print self.manual
					#print 'manman'
					self.textBrowser.append(u'开启录像失败！检查设备在线吗？登录了吗？')
			print '%s times on !' % self.times

			#if self.flag == 1:
				#self.dosleep.start()
			#else:
				#self.dosleep.stop()

			#time.sleep(int(self.timedelay_video))
		except Exception as err_man:
			print Exception,':',err_man

	#消警
	@pyqtSignature("")
	def on_pushButton_7_clicked(self):
		state=255
		try:
			print  self.ip
			print self.id+1
			#print 'oneone'
		except Exception:
			self.get_ip()
			self.dll.Setup(self.path_pinjie, self.ip, self.user, self.passwd)
			self.id = self.dll.Logon()
			self.textBrowser.append(u'没有登录，自定义登陆成功！')
		try:
			self.chn_nums_alarm = self.dll.GetChnNum(self.id)
			for i_chn_alarm in range (0,int(self.chn_nums_alarm)):
				self.alarmclear=self.dll.AlarmClear(self.id,i_chn_alarm,state)
				if self.alarmclear == 0:
					out_log_alarm = u'消警成功！' + ':' + str(i_chn_alarm)
					self.textBrowser.append(out_log_alarm)
				else:
					print self.chn_nums_alarm
		except Exception as err_alarm:
			print Exception, ':', err_alarm
####################################################################################
	#断连视频
	@pyqtSignature("")
	def on_pushButton_recv_released(self):
		timedelay_getvideo = self.lineEdit_recv.text()
		self.flag=1
		try:
			print  self.ip
			#print self.id+1
			#print 'oneone'
		except Exception:
			self.get_ip()
			self.dll.Setup(self.path_pinjie, self.ip, self.user, self.passwd)
			self.id = self.dll.Logon()
			self.textBrowser.append(u'没有登录，自定义登陆成功！')
		self.chnnums=int(self.dll.GetChnNum(self.id))
		#print self.chnnums
		if 1:
			self.pushButton_recv.setDisabled(True)

			from Video_thread import DoThread
			self.dosleep = DoThread(timedelay_getvideo)
			self.dosleep.finishSignal.connect(self.DoVideo)
			# , Qt.QueuedConnection
			if self.flag==1:
				self.dosleep.start()
			else:
				self.dosleep.stop()
	def DoVideo(self):
		#print 'nonono'
		duanlian_log = u'断连成功！' + ':' + str(self.times)
		self.textBrowser.append(duanlian_log)
		self.times += 1
		try:
			for i in range(0,self.chnnums):
				print 'Now Channel is : %s' %i
				self.recv = self.dll.GetVideoStart(self.id, i)
				self.getstop=self.dll.GetVideoStop(self.recv)
				if self.getstop==0:
					pass
				else:
					print "Did't stop!! Chnnel is %s" %self.chnnums
					raise Exception

				if self.flag == 1:
					self.dosleep.start()
				else:
					self.dosleep.stop()
					#time.sleep(int(self.timedelay_getvideo))
					#self.dodo.wait()
					#self.dodo.stop()
					#self.dodo.wait()
					#self.dodo.stop()
		except Exception as err_getvideo:
			print Exception, ':', err_getvideo

	#CGI
	def on_pushButton_cgi_released(self):
		self.get_ip()
		self.timedelay_change= str(self.lineEdit_cgi_timeinput.text())
		self.get_cgi_add=str(self.lineEdit_cgi_address.text())
		self.get_cgi1=str(self.TextEdit_cgi1.toPlainText())

		self.get_cgi2=str(self.TextEdit_cgi2.toPlainText())
		self.flag = 1
		if 1:
			self.pushButton_cgi.setDisabled(True)

			from Video_thread import DoThread
			self.dosleep = DoThread(self.timedelay_change)
			self.dosleep.finishSignal.connect(self.put_res)
			# , Qt.QueuedConnection
			if self.flag==1:
				self.textBrowser.append(u'开始切换！！')
				self.dosleep.start()
			else:
				self.dosleep.stop()

	def put_res(self):
		#( self.get_cgi1, self.get_cgi2)
		ip=self.ip
		user=self.user
		passwd=self.passwd
		cgi=self.get_cgi_add
		data1=self.get_cgi1
		data2=self.get_cgi2
		self.ip_add='http://'+ip+cgi
		head = {'Accept': 'application/xml, text/xml, */*; q=0.01',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
				'Content-Type': 'application/xml;charset=utf-8', 'Accept-Encoding': 'gzip,deflate,sdch',
				'Accept-Language': 'zh-CN,zh;q=0.8', 'X-Requested-With': 'XMLHttpRequest'}
		#p = requests.put(self.ip_add, headers=head, auth=(user, passwd), data=data1)
		out_log_cgi= u'参数切换成功！' + ':' + str(self.times)

		if self.flag_forcgi==1:
			try:
				p1 = requests.put(self.ip_add, headers=head, auth=(user, passwd), data=data1)
				print p1.status_code
				p1_code=p1.status_code
				if p1_code!=200:
					out_cgi1 = u'XML 1在发送中出错，错误码是：' + str(p1_code)
					self.textBrowser.append(out_cgi1)
				self.flag_forcgi=0
			except Exception as err_cgi1:
				print Exception, ':', err_cgi1
				self.textBrowser.append(err_cgi1)
		elif self.flag_forcgi==0:
			try:
				p2 = requests.put(self.ip_add, headers=head, auth=(user, passwd), data=data2)
				print p2.status_code
				out_cgi2=u'返回码：' + str(p2.status_code)
				if p2.status_code==200:
					self.textBrowser.append(out_log_cgi)
					self.textBrowser.append(out_cgi2)
				else:
					self.textBrowser.append('Something with change!')
					self.textBrowser.append(p2.status_code)
				self.flag_forcgi = 1
				self.times+=1
			except Exception as err_cgi2:
				print Exception, ':', err_cgi2
				self.textBrowser.append(err_cgi2)
		if self.flag == 1:
			self.dosleep.start()
		else:
			self.dosleep.stop()
		#while 1:

	#显示和隐藏
	def on_pushButton_cgi_show_released(self):
		#self.changemain(self)
		self.widget2.setVisible(True)
		self.pushButton_cgi_show.clicked.connect(lambda :self.changemain(self))
		self.pushButton_cgi_show.setVisible(False)
		self.pushButton_cgi_hide.setVisible(True)
	def on_pushButton_cgi_hide_released(self):
		#self.changemain(self)
		self.widget2.setVisible(False)
		self.pushButton_cgi_hide.clicked.connect(lambda :self.changemain_old(self))
		self.pushButton_cgi_show.setVisible(True)
		self.pushButton_cgi_hide.setVisible(False)
		#self.setupUi(self)
	#停止所有并点亮
	@pyqtSignature("")
	def on_pushButton_stopall_released(self):
		#sin=pyqtSignal()

		try:
			self.flag = 0
			self.pushButton_recv.setDisabled(False)
			self.pushButton_4.setDisabled(False)
			self.pushButton_3.setDisabled(False)
			self.pushButton_cgi.setDisabled(False)
			self.dosleep.stop()
			self.times = 1
			self.textBrowser.append(u'已停止下发,再执行一次后会自动停止..')
		except Exception as err_stopall:
			print Exception, 'stop_all is :', err_stopall



if __name__ == '__main__':
	app = PyQt4.QtGui.QApplication(argv)
	msg_box = QMessageBox(QMessageBox.Warning,u"恭喜：",u"转换完毕！")
	msg_flase= QMessageBox(QMessageBox.Warning,u"注意：",u"出问题了，检查一下吧！")
	dlg = MainWindow()
	dlg.show()

	exit(app.exec_())
