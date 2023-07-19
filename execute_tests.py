from tests_models import check_list_registration_form
from selenium import webdriver
from pages_models import RegPage

driver= webdriver.Chrome()
q = RegPage(driver)

check_list_registration_form(q)
driver.quit()

driver= webdriver.Firefox()
q = RegPage(driver)

check_list_registration_form(q)
driver.quit()

#end tests
