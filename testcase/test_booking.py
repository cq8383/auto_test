from datetime import datetime, timedelta
from time import sleep, strftime

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestBooking:
    def __init__(self):
       self.driver = webdriver.Chrome()
       self.driver.get('file:///E:/0725%E5%B7%A5%E8%B4%B8%E7%BB%83%E4%B9%A0/web/index.html#')
       self.driver.maximize_window()

    @allure.feature("预定表单")
    @allure.story("预定表单功能测试")
    @allure.title("出发/目的城市选择功能")
    def test_F_001(self):
        with allure.step("点击出发城市下拉框"):
            sela=Select(self.driver.find_element(By.XPATH,'//*[@id="booking-form"]/div[1]/div[1]/div/select'))
        with allure.step("选择北京（BJS）"):
            sela.select_by_value('BJS')
        with allure.step("点击目的城市下拉框"):
            sel = Select(self.driver.find_element(By.XPATH, '//*[@id="booking-form"]/div[1]/div[2]/div/select'))
        with allure.step("选择上海（SHA）"):
            sel.select_by_value('SHA')
        with allure.step("检查是否选中列表"):
            assert "上海" in self.driver.page_source
            timef = strftime('%Y%m%d%H%M%S')
            self.driver.get_screenshot_as_file('./screenshots/F_001_{}.png'.format(timef))
            allure.attach(self.driver.get_screenshot_as_png(),'截图',allure.attachment_type.PNG)

    @allure.feature("预定表单")
    @allure.story("预定表单功能测试")
    @allure.title("日期输入功能")
    def test_F_002(self):
        with allure.step("点击出发日期输入框"):
            date_input = self.driver.find_element(By.XPATH, '//*[@id="departure-date"]')
        with allure.step("输入当前日期＋3天的日期"):
            future_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")  # 计算当前日期加3天的日期，格式为YYYY-MM-DD
            date_input.clear()  # 清除可能已有的值
            date_input.send_keys(future_date)
        with allure.step("检查是否输入正确日期"):
            #assert "上海" in driver.page_source
            timef = strftime('%Y%m%d%H%M%S')
            self.driver.get_screenshot_as_file('./screenshots/F_002_{}.png'.format(timef))
            allure.attach(self.driver.get_screenshot_as_png(), '截图', allure.attachment_type.PNG)

    @allure.feature("预定表单")
    @allure.story("预定表单功能测试")
    @allure.title("附加服务选择功能")
    def test_F_003(self):
        with allure.step("找到附加服务模块"):
            check_input = self.driver.find_element(By.XPATH, '//*[@id="booking-form"]/div[3]/div/label[2]/input')
        with allure.step("点击优先登机复选框"):
            check_input.click()
        with allure.step("检查优先登机复选框可正常勾选"):
            # assert "上海" in driver.page_source
            timef = strftime('%Y%m%d%H%M%S')
            self.driver.get_screenshot_as_file('./screenshots/F_003_{}.png'.format(timef))
            allure.attach(self.driver.get_screenshot_as_png(), '截图', allure.attachment_type.PNG)

    @allure.feature("预定表单")
    @allure.story("预定表单功能测试")
    @allure.title("搜索航班功能")
    def test_F_004(self):
        with allure.step("点击搜索航班按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="search-flights"]').click()
        with allure.step("等待页面跳转"):
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
        with allure.step("检查弹出 “搜索完成” 对话框"):
            # assert "上海" in driver.page_source
            timef = strftime('%Y%m%d%H%M%S')
            self.driver.get_screenshot_as_file('./screenshots/F_004_{}.png'.format(timef))
            allure.attach(self.driver.get_screenshot_as_png(), '截图', allure.attachment_type.PNG)
            self.driver.close()