from time import sleep, strftime

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
@allure.feature("")
class TestBooking:
    @allure.story("预定表单功能测试")
    @allure.title("出发/目的城市选择功能")
    def test_F_001(self):
        with allure.step("点击出发城市下拉框"):
            driver=webdriver.Chrome()
            driver.get('file:///E:/0725%E5%B7%A5%E8%B4%B8%E7%BB%83%E4%B9%A0/web/index.html#')
            driver.maximize_window()
            driver.implicitly_wait(10)
            sela=Select(driver.find_element(By.XPATH,'//*[@id="booking-form"]/div[1]/div[1]/div/select'))
        with allure.step("选择北京（BJS）"):
            sela.select_by_value('BJS')
        with allure.step("点击目的城市下拉框"):
            sel = Select(driver.find_element(By.XPATH, '//*[@id="booking-form"]/div[1]/div[2]/div/select'))
        with allure.step("选择上海（SHA）"):
            sel.select_by_value('SHA')
            timef = strftime('%Y%m%d%H%M%S')
            driver.get_screenshot_as_file('./screenshots/F_001_{}.png'.format(timef))
            allure.attach(driver.get_screenshot_as_png(),'截图',allure.attachment_type.PNG)
            driver.quit()
