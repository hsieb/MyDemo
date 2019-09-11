from PyQt5 import QtWidgets 
from test import Ui_Form
from PyQt5.QtCore import *
import sys, os, time
import pytesseract
from PIL import Image, ImageGrab
from aip import AipOcr 
import json
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#百度文字识别api
APP_ID = '15664093'
API_KEY = 'mQKptwKja1AzI6P6pHfUKYu0'
SECRET_KEY = 'X3iFz46Z3l7BWZ4OsVfLtwM6C5xBbYYs'


aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath): 
    with open(filePath, 'rb') as fp: 
        return fp.read()

class ReadPic():
    def init(self,filePath):
        options = {}
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        return aipOcr.webImage(get_file_content(filePath),options)

class ScreenShot():
    
    def work(self,a,b,c,d):
            img = ImageGrab.grab([a,b,c,d])
            img.save("D:/python36/workspace/test/kangkang.png")

class MyThread(QThread):  
  
    sec_changed_signal = pyqtSignal(int) # 信号类型：int
    brguge=webdriver.Chrome()#声明驱动对象
    brguge.get('https://www.woxunbudao.cn/')
    input=brguge.find_element_by_class_name('form-control')  
    def __init__(self, sec=1000, parent=None):  
        super().__init__(parent)
        self.sec = sec # 默认1000秒
  
    def run(self):
        while True:
            print(self.input.get_attribute('value'))
            if not self.input.get_attribute('value').strip()=='':
                self.input.clear()
                
            self.filePath = "kangkang.png"
            self.result= ReadPic().init(self.filePath)
            
            for i in range(len(self.result['words_result'])):
                self.input.send_keys(self.result['words_result'][i]['words'])
            self.wait=WebDriverWait(self.brguge,1)#等待元素加载出来
            print(self.brguge.current_url)#输出搜索的路径
                            
            self.sec_changed_signal.emit(1)#发送信号
            time.sleep(4)#线程挂起4s
            #self.input.clear()


class MyWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self): 
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.label.setText("915.372.1151.396  435，370，572，392")
        self.thread = MyThread() # 创建一个线程 
        self.thread.sec_changed_signal.connect(self.showF) # 线程发过来的信号挂接到槽：update
    def showTime(self):
        # 获取系统现在的时间
        time = QDateTime.currentDateTime()
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        # 在标签上显示时间
        self.label.setText(timeDisplay)
    def showF(self):
        a = int(self.lineEdit.text())
        b = int(self.lineEdit_2.text())
        c = int(self.lineEdit_3.text())
        d = int(self.lineEdit_4.text())
        ScreenShot().work(a,b,c,d)
        
    def slot_quit(self):
        sys.exit(app.exec_())
    def slot_start(self):
        self.thread.start()
    def slot_stop(self):
        self.thread.terminate()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv) 
    myshow=MyWindow() 
    myshow.show() 
    sys.exit(app.exec_())
