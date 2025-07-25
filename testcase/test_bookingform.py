from datetime import datetime, timedelta
from time import sleep, strftime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestBookingForm:
    paraDatas=[{"sfz":"110101199001011234","msg":"支付成功！"
    },{"sfz":"11010119900101123","msg":"支付成功！"},{"sfz":"E12345678","msg":"支付成功！"}]
    @allure.feature("预定表单")
    @allure.story("预定表单功能测试")
    @allure.title("完整流程完整性功能")
    @pytest.mark.parametrize('data',paraDatas)
    def test_F_008(self):
        self.driver = webdriver.Chrome()
        self.driver.get('file:///E:/0725%E5%B7%A5%E8%B4%B8%E7%BB%83%E4%B9%A0/web/index.html#')
        self.driver.maximize_window()
        with allure.step("点击出发城市下拉框"):
            sela=Select(self.driver.find_element(By.XPATH,'//*[@id="booking-form"]/div[1]/div[1]/div/select'))
        with allure.step("选择北京（BJS）"):
            sela.select_by_value('BJS')
        with allure.step("点击目的城市下拉框"):
            sel = Select(self.driver.find_element(By.XPATH, '//*[@id="booking-form"]/div[1]/div[2]/div/select'))
        with allure.step("选择上海（SHA）"):
            sel.select_by_value('SHA')
        with allure.step("点击出发日期输入框"):
            date_input = self.driver.find_element(By.XPATH, '//*[@id="departure-date"]')
        with allure.step("输入当前日期＋3天的日期"):
            future_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")  # 计算当前日期加3天的日期，格式为YYYY-MM-DD
            date_input.clear()  # 清除可能已有的值
            date_input.send_keys(future_date)
        with allure.step("找到附加服务模块"):
            check_input = self.driver.find_element(By.XPATH, '//*[@id="booking-form"]/div[3]/div/label[2]/input')
        with allure.step("点击优先登机复选框"):
            check_input.click()
        with allure.step("点击搜索航班按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="search-flights"]').click()
        with allure.step("等待页面跳转"):
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
        with allure.step("点击中国国际航空 CA1833的选择按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="flights-results"]/div[3]/div[1]/div[3]/button').click()
        with allure.step("在弹出的确认对话框中点击确认"):
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
        with allure.step("填写联系人姓名 “张三”、手机号“13800138000”、邮箱“zhangsan@test.com”"):
            self.driver.find_element(By.XPATH, '//*[@id="passenger-info"]/div/div[1]/div[1]/div/div[1]/input').send_keys('张三')
            self.driver.find_element(By.XPATH, '//*[@id="passenger-info"]/div/div[1]/div[1]/div/div[2]/input').send_keys('13800138000')
            self.driver.find_element(By.XPATH, '//*[@id="passenger-info"]/div/div[1]/div[1]/div/div[3]/input').send_keys('zhangsan@test.com')
        with allure.step("填写乘客姓名拼音 “ZHANG SAN”、证件类型 “身份证”、证件号“110101199001011234”"):
            self.driver.find_element(By.XPATH, '//*[@id="passenger-info"]/div/div[1]/div[2]/div/div[2]/input').send_keys('ZHANG SAN')
            Select(self.driver.find_element(By.XPATH, '//*[@id="passenger-info"]/div/div[1]/div[2]/div/div[3]/select')).select_by_value('idcard')
            self.driver.find_element(By.XPATH, '//*[@id="passenger-info"]/div/div[1]/div[2]/div/div[4]/input').send_keys('110101199001011234')
        with allure.step("点击 “继续支付” 按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="proceed-to-payment"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
            sleep(2)
        with allure.step("选择 “信用卡 / 借记卡” 支付方式"):
            self.driver.find_element(By.XPATH, '//*[@id="payment-page"]/div/div/div[1]/div[3]/div[1]/label[1]/input').click()
        with allure.step("填写卡号 “6222021234567890123”、有效期 “12/28”、安全码 “123”"):
            self.driver.find_element(By.XPATH, '//*[@id="payment-page"]/div/div/div[1]/div[3]/div[2]/div[2]/div/input').send_keys('6222021234567890123')
            self.driver.find_element(By.XPATH, '//*[@id="payment-page"]/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/input').send_keys('12/28')
            self.driver.find_element(By.XPATH, '//*[@id="payment-page"]/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/input').send_keys('123')
        with allure.step("勾选 “同意条款”"):
            self.driver.find_element(By.XPATH, '//*[@id="payment-page"]/div/div/div[2]/div/div/div[5]/label/input').click()
            sleep(1)
        with allure.step("点击 “完成支付” 按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="complete-payment"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
            sleep(1)
        with allure.step("检查是否选中列表"):
            assert "支付成功！" == self.driver.find_element(By.XPATH,'//*[@id="success-page"]/div/h2').text
            timef = strftime('%Y%m%d%H%M%S')
            self.driver.get_screenshot_as_file('./screenshots/F_008_{}.png'.format(timef))
            allure.attach(self.driver.get_screenshot_as_png(),'截图',allure.attachment_type.PNG)
            self.driver.close()

    def test_D_001(self, data):
        self.driver = webdriver.Chrome()
        self.driver.get('file:///E:/0725%E5%B7%A5%E8%B4%B8%E7%BB%83%E4%B9%A0/web/index.html#')
        self.driver.maximize_window()
        with allure.step("点击出发城市下拉框"):
            sela = Select(self.driver.find_element(By.XPATH, '//*[@id="booking-form"]/div[1]/div[1]/div/select'))
        with allure.step("选择北京（BJS）"):
            sela.select_by_value('BJS')
        with allure.step("点击目的城市下拉框"):
            sel = Select(self.driver.find_element(By.XPATH, '//*[@id="booking-form"]/div[1]/div[2]/div/select'))
        with allure.step("选择上海（SHA）"):
            sel.select_by_value('SHA')
        with allure.step("点击出发日期输入框"):
            date_input = self.driver.find_element(By.XPATH, '//*[@id="departure-date"]')
        with allure.step("输入当前日期＋3天的日期"):
            future_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")  # 计算当前日期加3天的日期，格式为YYYY-MM-DD
            date_input.clear()  # 清除可能已有的值
            date_input.send_keys(future_date)
        with allure.step("找到附加服务模块"):
            check_input = self.driver.find_element(By.XPATH, '//*[@id="booking-form"]/div[3]/div/label[2]/input')
        with allure.step("点击优先登机复选框"):
            check_input.click()
        with allure.step("点击搜索航班按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="search-flights"]').click()
        with allure.step("等待页面跳转"):
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
        with allure.step("点击中国国际航空 CA1833的选择按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="flights-results"]/div[3]/div[1]/div[3]/button').click()
        with allure.step("在弹出的确认对话框中点击确认"):
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
        with allure.step("填写联系人姓名 “张三”、手机号“13800138000”、邮箱“zhangsan@test.com”"):
            self.driver.find_element(By.XPATH,
                                     '//*[@id="passenger-info"]/div/div[1]/div[1]/div/div[1]/input').send_keys('张三')
            self.driver.find_element(By.XPATH,
                                     '//*[@id="passenger-info"]/div/div[1]/div[1]/div/div[2]/input').send_keys(
                '13800138000')
            self.driver.find_element(By.XPATH,
                                     '//*[@id="passenger-info"]/div/div[1]/div[1]/div/div[3]/input').send_keys(
                'zhangsan@test.com')
        with allure.step("填写乘客姓名拼音 “ZHANG SAN”、证件类型 “身份证”、证件号“110101199001011234”"):
            self.driver.find_element(By.XPATH,
                                     '//*[@id="passenger-info"]/div/div[1]/div[2]/div/div[2]/input').send_keys(
                'ZHANG SAN')
            Select(self.driver.find_element(By.XPATH,
                                            '//*[@id="passenger-info"]/div/div[1]/div[2]/div/div[3]/select')).select_by_value(
                'idcard')
            self.driver.find_element(By.XPATH,
                                     '//*[@id="passenger-info"]/div/div[1]/div[2]/div/div[4]/input').send_keys(
                '110101199001011234')
        with allure.step("点击 “继续支付” 按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="proceed-to-payment"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
            sleep(2)
        with allure.step("选择 “信用卡 / 借记卡” 支付方式"):
            self.driver.find_element(By.XPATH,
                                     '//*[@id="payment-page"]/div/div/div[1]/div[3]/div[1]/label[1]/input').click()
        with allure.step("填写卡号 “6222021234567890123”、有效期 “12/28”、安全码 “123”"):
            self.driver.find_element(By.XPATH,
                                     '//*[@id="payment-page"]/div/div/div[1]/div[3]/div[2]/div[2]/div/input').send_keys(
                '6222021234567890123')
            self.driver.find_element(By.XPATH,
                                     '//*[@id="payment-page"]/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/input').send_keys(
                '12/28')
            self.driver.find_element(By.XPATH,
                                     '//*[@id="payment-page"]/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/input').send_keys(
                '123')
        with allure.step("勾选 “同意条款”"):
            self.driver.find_element(By.XPATH,
                                     '//*[@id="payment-page"]/div/div/div[2]/div/div/div[5]/label/input').click()
            sleep(1)
        with allure.step("点击 “完成支付” 按钮"):
            self.driver.find_element(By.XPATH, '//*[@id="complete-payment"]').click()
            self.driver.find_element(By.XPATH, '//*[@id="dialog-confirm"]').click()
            sleep(1)
        with allure.step("检查是否选中列表"):
            assert "支付成功！" == self.driver.find_element(By.XPATH, '//*[@id="success-page"]/div/h2').text
            timef = strftime('%Y%m%d%H%M%S')
            self.driver.get_screenshot_as_file('./screenshots/F_008_{}.png'.format(timef))
            allure.attach(self.driver.get_screenshot_as_png(), '截图', allure.attachment_type.PNG)
            self.driver.close()