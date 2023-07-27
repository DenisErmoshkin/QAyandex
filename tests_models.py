import time
from datetime import datetime

# list_1 = ['Jan', 'Hus', 'janhus.cz', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233']
# list_2 = [['', 'empty field firstname, NEGATIVE TEST'],
#           [' ', 'only spaces in field firstname, NEGATIVE TEST'],
#           ['йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', '51 simbols in field firstname, NEGATIVE TEST'],
#           ['<script>alert("XSS attack!");</script>', 'XSS injection in field firstname, NEGATIVE TEST'],
#           ['105; DROP TABLE Suppliers', 'SQL injection in field firstname, NEGATIVE TEST'],
#           ['<style>input[name=csrf_token][value=^a]</style>', 'CSS injection in field firstname, NEGATIVE TEST'],
#           ['<body>HTMLtag</body>', 'HTML injection in field firstname, NEGATIVE TEST']]
#
# for element in list_2:
#     list_1[0] = element[0]
#     print(f'{list_1} + as')
#     with open('info_log.txt', 'a') as f:
#         print(f'OK + {list_1}', file=f)


def check_list_registration_form(q, list_1, list_2):
    # [firstname, lastname, password, password-confirm, phone namber]
    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp)
    str_date_time = str(date_time.strftime("%d-%m-%Y, %H:%M:%S"))

    with open('info_log.txt', 'a') as f:
        f.write('\n' + "---------------------------------------------------" + '\n' + str_date_time + ', ')
        if 'chrome' in str(q.driver):
            f.write('Chrome browser tests' + '\n' + "---------------------------------------------------" + '\n')
        elif 'firefox' in str(q.driver):
            f.write('Firefox browser tests' + '\n' + "---------------------------------------------------" + '\n')

    for element in list_2:
        list_1[0] = element[0]
        try:
            q.negative_test_form(list_1)
            with open('info_log.txt', 'a') as f:
                f.write(f'OK + {list_2[1]}\n', file=f)
        except:
            with open('info_log.txt', 'a') as f:
                f.write('NOK - empty field firstname, NEGATIVE TEST\n')
            pass
    #
    #
    #
    # try:
    #     q.negative_test_form(['', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    #     with open('info_log.txt', 'a') as f:
    #         f.write('OK - empty field firstname, NEGATIVE TEST\n')
    # except:
    #     with open('info_log.txt', 'a') as f:
    #         f.write('NOK - empty field firstname, NEGATIVE TEST\n')
    #     pass
    #
    # try:
    #     q.negative_test_form(['  ', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    #     with open('info_log.txt', 'a') as f:
    #         f.write('OK - only spaces in field firstname, NEGATIVE TEST\n')
    # except:
    #     with open('info_log.txt', 'a') as f:
    #         f.write('NOK - only spaces in field firstname, NEGATIVE TEST\n')
    #     pass
    #
    # try:
    #     q.negative_test_form(['йорптирвнкглРПимхъэжфрыпвагцштиьмофяРЕУфвапясьмдлйь', 'qwe', 'ermqwe', 'Qwertyuiop[1974',
    #                           'Qwertyuiop[1974', '+79223332233'])
    #     with open('info_log.txt', 'a') as f:
    #         f.write('OK - 51 simbols in field firstname, NEGATIVE TEST\n')
    # except:
    #     with open('info_log.txt', 'a') as f:
    #         f.write('NOK - 51 simbols in field firstname, NEGATIVE TEST\n')
    #     pass
    #
    # try:
    #     q.negative_test_form(
    #         ['<script>alert("XSS atack!");</script>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974',
    #          '+79223332233'])
    #     with open('info_log.txt', 'a') as f:
    #         f.write('OK - XSS injection in field firstname, NEGATIVE TEST\n')
    # except:
    #     with open('info_log.txt', 'a') as f:
    #         f.write('NOK - XSS injection in field firstname, NEGATIVE TEST\n')
    #     pass
    #
    # try:
    #     q.negative_test_form(
    #         ['105; DROP TABLE Suppliers', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    #     with open('info_log.txt', 'a') as f:
    #         f.write('OK - SQL injection in field firstname, NEGATIVE TEST\n')
    # except:
    #     with open('info_log.txt', 'a') as f:
    #         f.write('NOK - SQL injection in field firstname, NEGATIVE TEST\n')
    #     pass
    #
    # try:
    #     q.negative_test_form(
    #         ['<style>input[name=csrf_token][value=^a]</style>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974',
    #          '+79223332233'])
    #     with open('info_log.txt', 'a') as f:
    #         f.write('OK - CSS injection in field firstname, NEGATIVE TEST\n')
    # except:
    #     with open('info_log.txt', 'a') as f:
    #         f.write('NOK - CSS injection in field firstname, NEGATIVE TEST\n')
    #     pass
    #
    # try:
    #     q.negative_test_form(
    #         ['<body>HTMLtag</body>', 'qwe', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+79223332233'])
    #     with open('info_log.txt', 'a') as f:
    #         f.write('OK - HTML injection in field firstname, NEGATIVE TEST\n')
    # except:
    #     with open('info_log.txt', 'a') as f:
    #         f.write('NOK - HTML injection in field firstname, NEGATIVE TEST\n')
    #

# q.positive_test_form(['qwe', 'йцу', 'ermqwe', 'Qwertyuiop[1974', 'Qwertyuiop[1974', '+420773288247'])
