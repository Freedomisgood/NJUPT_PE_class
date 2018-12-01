# import requests
# import re
# from urllib.request import urlretrieve
# import subprocess
# from selenium.webdriver.common.keys import Keys

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException,WebDriverException
from selenium.webdriver import ActionChains

def login():
    id = input('学号：')
    passwd = input('密码：')
    #p = subprocess.Popen(['tesseract', 'captcha.jpg', 'captcha'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    url = 'http://202.119.225.34/default2.aspx'
    driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()
    ele_id = driver.find_element_by_xpath('//*[@id="txtUserName"]')
    ele_id.clear()
    ele_id.send_keys(id)


    while driver.current_url != 'http://202.119.225.34/xs_main.aspx?xh=' + id:   #如果验证码错误，则需要重新输入验证码和密码
        # 点击TextBox1后要移开焦点才能出现TextBox2
        print(driver.current_url)
        ele_psw1 = driver.find_element_by_xpath('//*[@id="Textbox1"]')
        ele_psw1.click()
        nothing = driver.find_element_by_xpath('//*[@id="form1"]/div/div[2]/img')
        nothing.click()
        ele_psw2 = driver.find_element_by_xpath('//*[@id="TextBox2"]')
        ele_psw2.clear()
        ele_psw2.send_keys(passwd)
        # captchaPic = driver.find_element_by_xpath('//*[@id="icode"]')

        captcha = input('验证码：')
        ele_captcha = driver.find_element_by_xpath('//*[@id="txtSecretCode"]')
        ele_captcha.clear()
        ele_captcha.send_keys(captcha)
        ele_confirm = driver.find_element_by_xpath('//*[@id="Button1"]')
        ele_confirm.click()
        try:    #处理完善信息的弹窗
            alert = driver.switch_to.alert
        except NoAlertPresentException:
            pass
        else:
            alert.accept()

    while True:
        try:    #处理完善信息的弹窗
            alert = driver.switch_to.alert
        except NoAlertPresentException:
            pass
        else:
            alert.accept()
        choose_class = driver.find_element_by_xpath('//*[@id="headDiv"]/ul/li[2]/a/span')
        action = ActionChains(driver)       #第二组动作，需要重新申请
        action.move_to_element(choose_class).perform()
        action.move_by_offset(50,110).click().perform()
        time.sleep(0.1)

        # print(driver.current_url)
        driver.switch_to.frame('iframeautoheight')
        mokuai = driver.find_element_by_xpath('//*[@id="kj"]')
        mokuai.click()
        time.sleep(0.1)

        mokuai3 = driver.find_element_by_xpath('//*[@id="kj"]/option[2]')
        mokuai3.click()

        try:
            driver.find_element_by_xpath('//*[@id="DataGrid2"]/tbody/tr[2]/td[10]/a')
        except NoSuchElementException:
            capacity = driver.find_element_by_xpath('//*[@id="kcmcGrid"]/tbody/tr[5]/td[7]')
            rest = driver.find_element_by_xpath('//*[@id="kcmcGrid"]/tbody/tr[5]/td[8]')
            # capacity = driver.find_element_by_xpath('//*[@id="kcmcGrid"]/tbody/tr[4]/td[7]')
            # rest = driver.find_element_by_xpath('//*[@id="kcmcGrid"]/tbody/tr[4]/td[8]')
            if int(capacity.text) == int(rest.text):
                driver.refresh()
                continue
            else:
                wangqiu = driver.find_element_by_xpath('//*[@id="kcmcGrid__ctl5_xk"]')
                wangqiu.click()
                # lanqiu = driver.find_element_by_xpath('//*[@id="kcmcGrid__ctl4_xk"]')
                # lanqiu.click()

                submit = driver.find_element_by_xpath('//*[@id="Button1"]')
                submit.click()
                print('*************已选上****************')
                break

            # alert = driver.switch_to.alert
            # alert.accept()
            # action = ActionChains(driver)
            # action.key_down(Keys.ENTER).perform()
        else:
            print('*****************已选********************')
            break


    # action = ActionChains(driver)
    # action.move_to_element_with_offset(mokuai,5,40).perform()
    # submit = driver.find_element_by_xpath('//*[@id="Button1"]')
    # time.sleep(1)
    # action.context_click(submit).perform()
    # action.move_by_offset(10,40).click().perform()
    #currentURL = driver.current_url
    # choose_class.click()
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    login()