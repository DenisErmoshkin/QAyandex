import time
from datetime import datetime

def time_stamp(n, q):
    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp)
    str_date_time = str(date_time.strftime("%d-%m-%Y, %H:%M:%S"))

    with open('info_log.txt', 'a') as f:
        f.write('\n' + "---------------------------------------------------" + '\n' + str_date_time + ', ')
        if 'chrome' in str(q.driver):
            f.write('Chrome browser tests,' + ' formfield number - ' + str(n) + '\n' + "---------------------------------------------------" + '\n')
        elif 'firefox' in str(q.driver):
            f.write('Firefox browser tests,' + ' formfield number - ' + str(n) + '\n' + "---------------------------------------------------" + '\n')
        print(str(q.driver))


def check_list_registration_form(q, l, w, n):
    # [firstname, lastname, password, password-confirm, phone namber]
    time_stamp(n, q)
    list_11 = l.copy()
    for element in w:
        list_11[n] = element[0]
        try:
            q.negative_test_form(list_11)
            with open('info_log.txt', 'a') as f:
                print(f'OK - {element[1]}', file=f)
        except:
            with open('info_log.txt', 'a') as f:
                print(f'NOK - {element[1]}, input date - {element[0]}', file=f)
            pass
