from time import sleep, strftime

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestBooking:
    def test_F_001(self):
        driver=webdriver.Chrome()
        driver.get('file:///E:/0725%E5%B7%A5%E8%B4%B8%E7%BB%83%E4%B9%A0/web/index.html#')
        driver.maximize_window()
        sleep(3)
        selecta=driver.find_element(By.XPATH,'//*[@id="booking-form"]/div[1]/div[1]/div/select')
        sel=Select(selecta)
        sel.select_by_value('BJS')
        timef = strftime('%Y%m%d%H%M%S')
        driver.get_screenshot_as_file('./screenshots/F_001_{}.png'.format(timef))
        allure.attach(driver.get_screenshot_as_png(),'截图',allure.attachment_type.PNG)
        driver.quit()
