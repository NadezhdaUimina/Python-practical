from datetime import datetime
from time import time


def log(data):
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write('{} / {} = {} Time {}\n'.format(data, time))