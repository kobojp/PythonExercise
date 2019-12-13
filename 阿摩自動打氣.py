from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#自動登入阿摩
url = 'https://yamol.tw/'
email = '帳號'
password = '密碼'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# try:
def login():
    element = WebDriverWait(driver, 10)
    mylogin = element.until(EC.presence_of_element_located((By.XPATH, '//a[@href="mylogin.php"]')))
    mylogin.click()

    exEmail = element.until(EC.presence_of_element_located((By.ID, 'exampleInputEmail')))
    exEmail.send_keys(email)

    exPassword = element.until(EC.presence_of_element_located((By.ID, 'exampleInputPassword')))
    exPassword.send_keys(password)

    confirmlogin =  element.until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-primary btn-lg"]')))
    confirmlogin.click()

    #換到好友頁面 筆記 阿摩晚上12點刷新
    url = 'https://yamol.tw/gas_tools.php'
    driver.get(url)

    #抓筆數 
    quantity =  element.until(EC.presence_of_element_located((By.XPATH, '//span[@class="pagination_counts"]')))
    #quantity.text
    print(quantity.text)

    #pump_up =  element.until(EC.presence_of_element_located((By.XPATH, '//a[@class="gasbtn btn btn-primary"]')))
    try:
        for i in range(1,int(quantity.text)): #為什麼不使用element.until 因為點擊太快了 會導致錯誤並不能全部點選完畢
            upup = driver.find_element_by_xpath('//a[@class="gasbtn btn btn-primary"]')
            upup.click()
            sleep(2)
    except:
        print('打氣完成')