import time
from datetime import datetime

def check_list_registration_form(q):
    # [firstname, lastname, password, password-confirm, phone namber]
    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp)
    str_date_time = str(date_time.strftime("%d-%m-%Y, %H:%M:%S"))
    list_1 = ['sdf', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233']
    list_2 = ['', ' ', 'йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', '<script>alert("XSS atack!");</script>',
              '105; DROP TABLE Suppliers', '<style>input[name=csrf_token][value=^a]</style>',
              '<body>HTMLtag</body>']


    with open('info_log.txt', 'a') as f:
        f.write('\n' + "---------------------------------------------------" + '\n' + str_date_time + ', ')
        if 'chrome' in str(q.driver):
            f.write('Chrome browser tests' + '\n' + "---------------------------------------------------" + '\n')
        elif 'firefox' in str(q.driver):
            f.write('Firefox browser tests' + '\n' + "---------------------------------------------------" + '\n')

    try:
        q.negative_test_form(['', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
        with open('info_log.txt', 'a') as f:
            f.write('OK - empty field firstname, NEGATIVE TEST\n')
    except:
        with open('info_log.txt', 'a') as f:
            f.write('NOK - empty field firstname, NEGATIVE TEST\n')
        pass

    try:
        q.negative_test_form(['  ', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
        with open('info_log.txt', 'a') as f:
            f.write('OK - only spaces in field firstname, NEGATIVE TEST\n')
    except:
        with open('info_log.txt', 'a') as f:
            f.write('NOK - only spaces in field firstname, NEGATIVE TEST\n')
        pass

    try:
        q.negative_test_form(['йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', 'qwe', 'ermqwe', 'Qwertyuiop[1974',
                              'Qwertyuiop[1974', '+79223332233'])
        with open('info_log.txt', 'a') as f:
            f.write('OK - 51 simbols in field firstname, NEGATIVE TEST\n')
    except:
        with open('info_log.txt', 'a') as f:
            f.write('NOK - 51 simbols in field firstname, NEGATIVE TEST\n')
        pass

    try:
        q.negative_test_form(
            ['<script>alert("XSS atack!");</script>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974',
             '+79223332233'])
        with open('info_log.txt', 'a') as f:
            f.write('OK - XSS injection in field firstname, NEGATIVE TEST\n')
    except:
        with open('info_log.txt', 'a') as f:
            f.write('NOK - XSS injection in field firstname, NEGATIVE TEST\n')
        pass

    try:
        q.negative_test_form(
            ['105; DROP TABLE Suppliers', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
        with open('info_log.txt', 'a') as f:
            f.write('OK - SQL injection in field firstname, NEGATIVE TEST\n')
    except:
        with open('info_log.txt', 'a') as f:
            f.write('NOK - SQL injection in field firstname, NEGATIVE TEST\n')
        pass

    try:
        q.negative_test_form(
            ['<style>input[name=csrf_token][value=^a]</style>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974',
             '+79223332233'])
        with open('info_log.txt', 'a') as f:
            f.write('OK - CSS injection in field firstname, NEGATIVE TEST\n')
    except:
        with open('info_log.txt', 'a') as f:
            f.write('NOK - CSS injection in field firstname, NEGATIVE TEST\n')
        pass

    try:
        q.negative_test_form(
            ['<body>HTMLtag</body>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
        with open('info_log.txt', 'a') as f:
            f.write('OK - HTML injection in field firstname, NEGATIVE TEST\n')
    except:
        with open('info_log.txt', 'a') as f:
            f.write('NOK - HTML injection in field firstname, NEGATIVE TEST\n')


# q.positive_test_form(['qwe', 'йцу', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+420773288247'])