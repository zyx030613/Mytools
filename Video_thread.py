# -*- coding: utf-8 -*-
from PyQt4 import QtCore

import time





# 继承 QThread 类
class DoThread(QtCore.QThread):
	"""docstring for BigWorkThread"""
	# 声明一个信号，同时返回一个list，同理什么都能返回啦
	finishSignal = QtCore.pyqtSignal(list)

	# 构造函数里增加形参
	def __init__(self, args, parent=None):
		#threading.Thread.__init__(self)
		super(DoThread, self).__init__(parent)
		#QtCore.QThread.__init__(self, parent)
		# 储存参数
		self.args = args
		#self.flag = 1
		self.mutex = QtCore.QMutex()
	'''
	def __del__(self):
		self.wait()
	'''
	def stop(self):
		try:
			self.mutex.unlock()
			self.stopped =True
		finally:
			self.mutex.unlock()


		#self.wait()
	# 重写 run() 函数，在里面干大事。
	def run(self):
		# 大事
		# msg_box = QMessageBox(QMessageBox.Warning, u"恭喜：", u"转换完毕！")
		# msg_flase = QMessageBox(QMessageBox.Warning, u"注意：", u"出问题了，检查一下输入值吧！")
		#print 'time is : %s' %self.args
		#print type(self.args)
		time_delay=int(self.args)
		time.sleep(time_delay)
		self.finishSignal.emit(['timedelay ok'])
	#def stop(self):
		#print 'setting flag false!'
		#self.flag=0

		# 大事干完了，发送一个信号告诉主线程窗口

