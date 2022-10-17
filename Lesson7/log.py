from datetime import datetime
from time import time


def div_log(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} / {} = {} Time {}\n'.format(data, time))