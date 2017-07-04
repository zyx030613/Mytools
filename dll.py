# coding=utf-8
import ctypes
import time, os

os.path.abspath('.')
from ctypes import *

iServerPort = 0
iClientPort = 6699
iWnd = 0

cProxy = ""
# ctypes.POINTER(c_char("/0")*2)
# cProxyn =cProxy()
# cIP = c_char_p(b'192.168.18.138')
# cUserName = c_char_p(b'Admin')
# cUserName1 = cUserName
# cPassword = c_char_p(b'1111')
pcProductID = ""
iPort = c_int(3000)


# if __name__ == '__main__':
class Dll():
    def __init__(self):

        pass

    def Setup(self, dll_path, ip, user, passwd):
        os.chdir(dll_path)
        self.cIP = c_char_p(ip)
        self.cUserName = c_char_p(user)
        self.cPassword = c_char_p(passwd)
        self.dll = ctypes.windll.LoadLibrary('NVSSDK.dll')
        dllTest = self.dll.NetClient_Startup_V4
        # print(dllTest)
        dllTest.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        # _iServerPort,ctypes.c_int_iClientPort,ctypes.c_int_iWnd
        # dllTest.Serverport = ctypes.c_int_iServerPort
        # 发送SDK初始化
        nSet = dllTest(iServerPort, iClientPort, iWnd)
        # print'Logon ID is: ',nSet
        time.sleep(0.5)
        # print GetLastError()
        pass

    def Logon(self):
        # 加载
        # self.Setup(dll_path, ip, user, passwd)
        # ppp=os.path.split(os.path.realpath(__file__))[0]
        # print ppp+'\\'+'NVSSDK.dll'
        # 登录
        dllLogOn = self.dll.NetClient_Logon
        # dllLogOn.argtypes = [c_char_p,c_char_p,c_char_p,c_char_p,c_char_p,c_int]
        # print (cProxy,cUserName,cPassword,iPort)
        # 发送登录信息
        self.dllLogOnSet = dllLogOn(cProxy, self.cIP, self.cUserName, self.cPassword, pcProductID, iPort)
        time.sleep(1)

        dllLogOn.restype = ctypes.c_int
        print 'Logon id is: ', self.dllLogOnSet
        # print (dllLogOn.restype())

        dllGetLogonStatus = self.dll.NetClient_GetLogonStatus
        dllGetLogonStatus.argtypes = [c_int]
        dllGetSet = dllGetLogonStatus(self.dllLogOnSet)
        time.sleep(0.5)
        print 'Logon Status is: ', dllGetSet, u'(0和1都正常)'
        if dllGetSet == 0:
            return self.dllLogOnSet
        else:
            return None

    def LogOff(self, id):
        dllLogoff = self.dll.NetClient_Logoff
        dllLogoff.restype = ctypes.c_int
        dllLogoff_post = dllLogoff(id)
        print 'log off state is :', dllLogoff_post
        return dllLogoff_post

    def TelnetOpen(self, id):
        try:
            dllChangeTel = self.dll.NetClient_SetCommonEnable
            dllChangeTel.restype = ctypes.c_int
            dllTelSet = dllChangeTel(id, 0x12014, 0x7FFFFFFF, 1)
            print u'开启成功！'
            return dllTelSet
        except Exception as e:
            print (Exception, e)
            print u'开启telnet报错啦，把错误信息发给zyx吧!!'

    def Reboot(self, id):
        try:
            dllReboot = self.dll.NetClient_Reboot
            dllReboot.restype = ctypes.c_int
            dllReboot.argtypes = [c_int]
            dllReboot_post = dllReboot(id)
            print 'Reboot state is :', dllReboot_post
            return dllReboot_post
        except Exception as e:
            print (Exception, e)
            print u'重启报错啦，把错误信息发给zyx吧!!'

    def GetChnNum(self, id):
        try:
            self.dll_getchnnum = self.dll.NetClient_GetChannelNum
            self.dll_getchnnum.restype = POINTER(ctypes.c_int)
            self.dll_getchnnum.argtypes = [ctypes.c_int, POINTER(ctypes.c_int)]

            b = c_int()
            p2p = ctypes.POINTER(ctypes.c_int)(b)
            dllrecordset = self.dll_getchnnum(id, p2p)
            self.chn_nums = b.value - 1
            return self.chn_nums
        except Exception as f:
            print (Exception, f)
            print u'获取通道数报错啦，把错误信息发给zyx吧!!'
            # print type(b.value)

    def Manual(self, id, chn, state):
        try:
            self.dll_Manual = self.dll.NetClient_NetFileManualRecord
            self.dll_Manual.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
            self.dll_Manual_post = self.dll_Manual(id, chn, state)
            print 'Manual state is :', self.dll_Manual_post
            return self.dll_Manual_post
        except Exception as g:
            print (Exception, g)
            print u'手动录像修改报错啦，把错误信息发给zyx吧!!'

    # def AlarmInEnable(self,):
    def AlarmClear(self, id, chn, state):
        # state=255
        try:
            self.dll_AlarmClear = self.dll.NetClient_SetAlarmClear
            self.dll_AlarmClear.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
            self.dll_AlarmClear_post = self.dll_AlarmClear(id, chn, state)
            print 'AlarmClear state is :', self.dll_AlarmClear_post
            return self.dll_AlarmClear_post
        except Exception as h:
            print (Exception, h)
            print u'消警报错啦，把错误信息发给zyx吧!!'

    '''
    class ClientInfo(Structure):
        _pack =1
        _fields=[('id',c_int,0),
                 ('chn',c_int,0),
                 ('netfile',c_int,0),
                 ('remoteip',c_int,0),
                 ('netmode',c_int,1),
                 ('timeout',c_int,20),
                 ('ttl',c_int,0),
                 ('buffcount',c_int,1),
                 ('delaynum',c_int,1),
                 ('delaytime',c_int,0),
                 ('streamno',c_int,0),
                 ('flag',c_int,0),
                 ('position',c_int,0),
                 ('speed',c_int,1)]
    '''

    def GetVideoStart(self, id, chn):
        self.dll_StartRecv = self.dll.NetClient_StartRecv

        class CLIENTINFO(Structure):
            _fields_ = [('m_iServerID', c_int),
                        ('m_iChannelNo', c_int),
                        ('m_cNetFile', c_char*255),
                        ('m_cRemoteIP', c_char*16),
                        ('m_iNetMode', c_int),
                        ('m_iTimeout', c_int),
                        ('m_iTTL', c_int),
                        ('m_iBufferCount', c_int),
                        ('m_iDelayNum', c_int),
                        ('m_iDelayTime', c_int),
                        ('m_iStreamNO', c_int),
                        ('m_iFlag', c_int),
                        ('m_iPosition', c_int),
                        ('m_iSpeed', c_int)]

        cltInfo = CLIENTINFO()
        client_pointer = pointer(cltInfo)

        cltInfo.m_iServerID = id
        cltInfo.m_iChannelNo = chn
        #cltInfo.m_cNetFile = ' '
        #cltInfo.m_cRemoteIP = ' '
        cltInfo.m_iNetMode = 1
        #cltInfo.m_iTimeout = 0
        #cltInfo.m_iTTL = 0
        #cltInfo.m_iBufferCount = 0
        #cltInfo.m_iDelayNum = 0
        #cltInfo.m_iDelayTime = 0
        cltInfo.m_iStreamNO = 0
        #cltInfo.m_iFlag = 0
        #cltInfo.m_iPosition = 0
        #cltInfo.m_iSpeed = 1


        # client_pointer=byref(client)
        #client_pointer = pointer(client)
        print sizeof(CLIENTINFO)
        #print client_pointer.contents
        # print isinstance(string_at(addressof(client_pointer)),'utf-8')

        # 定义C里面使用的回调函数
        # chuidiao=WINFUNCTYPE(ctypes.c_uint,ctypes.c_char_p,ctypes.c_int,ctypes.c_int)
        # c_huidiao =chuidiao(hanshu_c)
        #huidiao = 0
        back = c_uint()
        back_id = ctypes.POINTER(ctypes.c_uint)(back)
        self.dll_StartRecv.argtypes = [POINTER(ctypes.c_uint), POINTER(CLIENTINFO), ctypes.c_void_p]
        self.dll_StartRecv.restype = c_int
        self.dll_StartRecv_post = self.dll_StartRecv(back_id, client_pointer, 0)
        # self.dll_StartCap(id)
        print back.value
        print self.dll_StartRecv_post
        # print addressof(self.dll_StartRecv_post)
        #a = GetLastError()
        return back.value


    def GetVideoStop(self,conid):
        self.dll_StopRecv = self.dll.NetClient_StopRecv
        self.dll_StopRecv.argtypes = [ctypes.c_uint]
        self.dll_StopRecv_post=self.dll.NetClient_StopRecv(conid)
        print 'Back of stop video code is : %s' %self.dll_StopRecv_post
        return self.dll_StopRecv_post
    ###连接视频参数未调通，只能做视频通断
    def GetVideo(self,recv,win):
        class RECT(Structure):
            _fields_ = [('left', c_long),
                        ('top', c_long),
                        ('right', c_long),
                       ('bottom', c_long)]

        rect_new = RECT()
        rect_new.left=0
        rect_new.top=0
        rect_new.right=0
        rect_new.bottom=0

        self.getvideo=self.dll.NetClient_StartPlay
        #self.getvideo.argtypes = [c_uint,c_int,RECT,c_uint]
        print 'recv is: %s' %recv
        self.getvideo_post = self.getvideo(recv,win,rect_new,1)
        b = GetLastError()
        print 'Error code is',b
        print self.getvideo_post
        #return self.getvideo_post



# pathnow=os.getcwd() + '\\dll\\'
# Logon('192.168.18.131',pathnow)
#Dll.GetVideoStart(0,0)
