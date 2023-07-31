from tests_models import check_list_registration_form
from selenium import webdriver
from pages_models import RegPage

list_1 = ['Jan', 'Hus', 'janhus.cz', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233']
list_2 = [['', 'empty field, NEGATIVE TEST'],
          [' ', 'only spaces in field, NEGATIVE TEST'],
          ['йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', '51 simbols in field, NEGATIVE TEST'],
          ['<script>alert("XSS attack!");</script>', 'XSS injection in field, NEGATIVE TEST'],
          ['105; DROP TABLE Suppliers', 'SQL injection in field, NEGATIVE TEST'],
          ['<style>input[name=csrf_token][value=^a]</style>', 'CSS injection in field, NEGATIVE TEST'],
          ['<body>HTMLtag</body>', 'HTML injection in field, NEGATIVE TEST']]
list_3 = [['', 'empty field, NEGATIVE TEST'],
          [' ', 'only spaces in field, NEGATIVE TEST'],
          ['йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', '51 simbols in field, NEGATIVE TEST'],
          ['jan hus.cz', 'spase in login, NEGATIVE TEST'],
          ['//___&&', 'only punctuation marks in login, NEGATIVE TEST'],
          ['čšýáíéxcvě', 'utf simbols in login, NEGATIVE TEST'],
          ['jаnhus.сz', 'utf simbols in login, NEGATIVE TEST'],
          ['jan_hus.cz', 'punctuation marks in login, NEGATIVE TEST'],
          ['!janhus.cz', 'punctuation marks in login, NEGATIVE TEST'],
          ['<script>alert("XSS attack!");</script>', 'XSS injection in field, NEGATIVE TEST'],
          ['105; DROP TABLE Suppliers', 'SQL injection in field, NEGATIVE TEST'],
          ['<style>input[name=csrf_token][value=^a]</style>', 'CSS injection in field, NEGATIVE TEST'],
          ['<body>HTMLtag</body>', 'HTML injection in field, NEGATIVE TEST']]

driver_chrom = webdriver.Chrome()
q = RegPage(driver_chrom)

check_list_registration_form(q, list_1, list_2, 0)
check_list_registration_form(q, list_1, list_2, 1)
check_list_registration_form(q, list_1, list_3, 2)
driver_chrom.quit()

driver_fox = webdriver.Firefox()
q = RegPage(driver_fox)

check_list_registration_form(q, list_1, list_2, 0)
check_list_registration_form(q, list_1, list_2, 1)
check_list_registration_form(q, list_1, list_3, 2)
driver_fox.quit()

# end tests
