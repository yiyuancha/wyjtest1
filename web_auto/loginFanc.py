import time


def login(driver,name='wangyajuan',passwd='wangyajuan'):  # 登录成功
    driver.get(r"http://10.155.20.210/pms/index.php?m=user&f=login&referer=L3Btcy9pbmRleC5waHA=")
    time.sleep(2)
    driver.find_element_by_css_selector("input#account").send_keys(name)
    driver.find_element_by_xpath("//*[@name='password']").send_keys(passwd)
    driver.find_element_by_id("submit").click()


if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Firefox()

    login(driver)