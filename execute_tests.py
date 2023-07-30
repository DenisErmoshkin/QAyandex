from tests_models import check_list_registration_form
from selenium import webdriver
from pages_models import RegPage

list_1 = ['Jan', 'Hus', 'janhus.cz', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233']
list_2 = [['', 'empty field firstname, NEGATIVE TEST'],
          [' ', 'only spaces in field firstname, NEGATIVE TEST'],
          ['йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', '51 simbols in field firstname, NEGATIVE TEST'],
          ['<script>alert("XSS attack!");</script>', 'XSS injection in field firstname, NEGATIVE TEST'],
          ['105; DROP TABLE Suppliers', 'SQL injection in field firstname, NEGATIVE TEST'],
          ['<style>input[name=csrf_token][value=^a]</style>', 'CSS injection in field firstname, NEGATIVE TEST'],
          ['<body>HTMLtag</body>', 'HTML injection in field firstname, NEGATIVE TEST']]

driver_chrom = webdriver.Chrome()
q = RegPage(driver_chrom)

check_list_registration_form(q, list_1, list_2, 0)
check_list_registration_form(q, list_1, list_2, 1)
driver_chrom.quit()


driver_fox = webdriver.Firefox()
q = RegPage(driver_fox)

check_list_registration_form(q, list_1, list_2, 0)
check_list_registration_form(q, list_1, list_2, 1)
driver_fox.quit()

#end tests
