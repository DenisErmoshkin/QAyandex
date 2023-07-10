import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class SuccessRegPage:
    SUCCESS_REG_PAGE_ADDRESS = "https://passport.yandex.ru/registration/avatar?retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fprepare%3Fuuid%3D42887009-0913-4ac4-8b77-a6c8635d7d56%26goal%3Dhttps%253A%252F%252Fya.ru%252F%26finish%3D%252F%252Fyandex.ru%252Fsupport%252Fcommon%252Fbrowsers-settings%252Fincognito.html&process_uuid=c6c85083-7a1f-427d-8d0e-8bb65dcc5bf4"
    HEADER = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/main/div/h2')
    BUTTON_SELECT_FOTO = (By.ID, 'attach-control')
    BUTTON_SKIP = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/main/div/div/div/div[3]/div/span/a')
    USER_ID_BADGE = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/div/a[1]/div')
    USER_ID_BAGE_CLOSE = (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div[1]/div[3]/div')


class RegPage:
    REG_PAGE_ADDRESS = "https://passport.yandex.ru/registration?from=cloud&origin=disk_main-loginmenu_ru&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fprepare%3Fuuid%3D6cca8810-61c4-4dad-a6db-a3fc2448dadf%26goal%3Dhttps%253A%252F%252Fya.ru%252F%26finish%3Dhttps%253A%252F%252Fdisk.yandex.ru%252Fclient%252Fdisk%253Fsource%253Dmain-loginmenu&process_uuid=f429ef0a-c189-4745-b372-3522397bd6b8"
    INPUT_FIRSTNAME = (By.ID, 'firstname')
    INPUT_LASTNAME = (By.ID, 'lastname')
    INPUT_LOGIN = (By.ID, 'login')
    INPUT_PASS = (By.ID, 'password')
    INPUT_PASS_CONF = (By.ID, 'password_confirm')
    INPUT_PHONE = (By.ID, 'phone')
    BUTTON_REG = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[4]/span/button')
    ALERT = (By.XPATH, '//div[@role="alert"]')
    ALERT_NAME_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[1]/div[1]/div/div')
    ALERT_LASTNAME_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[1]/div[2]/div/div')
    ALERT_LOGIN_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[1]/div[3]/div')  # Такой логин не подойдет ... К сожалению, логин занят
    ALERT_PASS_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[2]/div[1]/div/div')  # Необходимо выбрать пароль
    ALERT_PASS_CONF_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[2]/div[2]/div/div')  # Необходимо ввести пароль еще раз
    ALERT_PHONE_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div/div')  # Пожалуйста, укажите номер телефона

    def __get_locators(self, test_date):
        driver = webdriver.Chrome()
        driver.get(RegPage.REG_PAGE_ADDRESS)
        firstname = wait(driver, 10).until(EC.presence_of_element_located(RegPage.INPUT_FIRSTNAME))
        lastname = wait(driver, 10).until(EC.presence_of_element_located(RegPage.INPUT_LASTNAME))
        login = wait(driver, 10).until(EC.presence_of_element_located(RegPage.INPUT_LOGIN))
        passw = wait(driver, 10).until(EC.presence_of_element_located(RegPage.INPUT_PASS))
        pass_conf = wait(driver, 10).until(EC.presence_of_element_located(RegPage.INPUT_PASS_CONF))
        phone = wait(driver, 10).until(EC.presence_of_element_located(RegPage.INPUT_PHONE))
        button_reg = wait(driver, 10).until(EC.element_to_be_clickable(RegPage.BUTTON_REG))

        firstname.send_keys(test_date[0])
        lastname.send_keys(test_date[1])
        login.send_keys(test_date[2])
        passw.send_keys(test_date[3])
        pass_conf.send_keys(test_date[4])
        phone.send_keys(test_date[5])

        return button_reg, driver

    def negative_test_form(self, test_date):
        locator = self.__get_locators(test_date)
        # button_reg.click()
        locator[1].execute_script("arguments[0].click();", locator[0])
        # passw.send_keys(Keys.ENTER)
        time.sleep(1)
        try:
            alert = wait(locator[1], 10).until(EC.presence_of_element_located(RegPage.ALERT))
        except:
            pass
        # url = driver.current_url
        assert alert != False, 'test is failed, NO ALERT'
        # locator[1].quit()

    def positive_test_form(self, test_date):
        locator = self.__get_locators(test_date)
        # button_reg.click()
        locator[1].execute_script("arguments[0].click();", locator[0])
        # passw.send_keys(Keys.ENTER)
        time.sleep(1)
        try:
            alert = wait(locator[1], 3).until(EC.presence_of_element_located(RegPage.ALERT))
        except:
            alert = False
            pass
        # url = driver.current_url

        assert alert == False, 'test is failed, RISE ALERT'
        # print(alert)
        # locator[1].quit()


q = RegPage()
# [firstname, lastname, password, password-confirm, phone namber]
try:
    q.negative_test_form(['', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - Пустое поле для ввода имени, NEGATIVE TEST')
except:
    print('NOK - Пустое поле для ввода имени, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['  ', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - Только пробелы в поле для ввода имени, NEGATIVE TEST')
except:
    print('NOK - Только пробелы в поле для ввода имени, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - 51 символ в поле для ввода имени, NEGATIVE TEST')
except:
    print('NOK - 51 символ в поле для ввода имени, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['<script>alert("XSS atack!");</script>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - XSS инекция в поле для ввода имени, NEGATIVE TEST')
except:
    print('NOK - XSS инекция в поле для ввода имени, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['105; DROP TABLE Suppliers', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - SQL инекция в поле для ввода имени, NEGATIVE TEST')
except:
    print('NOK - SQL инекция в поле для ввода имени, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['<style>input[name=csrf_token][value=^a]</style>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - CSS инекция в поле для ввода имени, NEGATIVE TEST')
except:
    print('NOK - CSS инекция в поле для ввода имени, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['<body>HTMLtag</body>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - HTML инекция в поле для ввода имени, NEGATIVE TEST')
except:
    print('NOK - HTML инекция в поле для ввода имени, NEGATIVE TEST')
    pass
# q.positive_test_form(['qwe', 'йцу', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+420773288247'])

