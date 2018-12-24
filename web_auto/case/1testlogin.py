#coding：utf-8
from selenium import webdriver
import  time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def setUp(self):
        self.driver.get(r"http://10.155.20.210/pms/index.php?m=user&f=login&referer=L3Btcy9pbmRleC5waHA=")
        time.sleep(2)

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
        self.driver.find_element_by_css_selector("input#account").send_keys("wangyajuan")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("wangyajuan")
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)
        t1=self.judge()
        print('t1=%s' % t1)
        self.assertTrue(t1=='王雅娟')

    def testlogon_2(self):     #登录密码错误
        self.driver.find_element_by_css_selector("input#account").send_keys("wangyajuan")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("122")
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)
        t2=self.judge()
        print('t2=%s'%t2)
        self.assertTrue(t2 == 'dfg')

    def tearDown(self):
        self.alteraccept()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


