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
    ALERT_NAME_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[1]/div[1]/div/div')
    ALERT_LASTNAME_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[1]/div[2]/div/div')
    ALERT_LOGIN_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[1]/div[3]/div') # Такой логин не подойдет ... К сожалению, логин занят
    ALERT_PASS_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[2]/div[1]/div/div') # Необходимо выбрать пароль
    ALERT_PASS_CONF_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[2]/div[2]/div/div') # Необходимо ввести пароль еще раз
    ALERT_PHONE_ERR = (By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div/div') # Пожалуйста, укажите номер телефона




