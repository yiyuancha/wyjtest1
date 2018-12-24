#coding：utf-8
from selenium import webdriver
import  time
import loginFanc
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def judge(self):
        try:
            t=self.driver.find_element_by_xpath("//*[@id='userMenu']/a").text
            return t
        except:
            return  ''


    def alteraccept(self):    #判断alert是否存在，存在就点确认
        try:
            time.sleep(2)
            t=self.driver.switch_to.alter()
            print(t.text)
            t.accept()
        except:
            return  "没有alter"


    def testlogin_01(self):   #登录成功
        '''登录成功的案例'''
        loginFanc.login(self.driver)
        time.sleep(2)
        t1=self.judge()
        print('t1=%s' % t1)
        self.assertTrue(t1=='王雅娟')

    def testlogon_2(self):     #登录密码错误
        loginFanc.login(self.driver,name="wangyajuan",passwd="123456")
        time.sleep(2)
        t2=self.judge()
        print('t2=%s'%t2)
        self.assertTrue(t2 == '')

    def tearDown(self):
        self.alteraccept()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


