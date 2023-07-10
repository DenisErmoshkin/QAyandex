from pages_models import RegPage

q = RegPage()

# [firstname, lastname, password, password-confirm, phone namber]

try:
    q.negative_test_form(['', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - Пустое поле firstname, NEGATIVE TEST')
except:
    print('NOK - Пустое поле firstname, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['  ', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - Только пробелы в поле firstname, NEGATIVE TEST')
except:
    print('NOK - Только пробелы в поле firstname, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - 51 символ в поле firstname, NEGATIVE TEST')
except:
    print('NOK - 51 символ в поле firstname, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['<script>alert("XSS atack!");</script>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - XSS инекция в поле firstname, NEGATIVE TEST')
except:
    print('NOK - XSS инекция в поле firstname, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['105; DROP TABLE Suppliers', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - SQL инекция в поле firstname, NEGATIVE TEST')
except:
    print('NOK - SQL инекция в поле firstname, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['<style>input[name=csrf_token][value=^a]</style>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - CSS инекция в поле firstname, NEGATIVE TEST')
except:
    print('NOK - CSS инекция в поле firstname, NEGATIVE TEST')
    pass

try:
    q.negative_test_form(['<body>HTMLtag</body>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    print('OK - HTML инекция в поле firstname, NEGATIVE TEST')
except:
    print('NOK - HTML инекция в поле firstname, NEGATIVE test')


# q.positive_test_form(['qwe', 'йцу', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+420773288247'])