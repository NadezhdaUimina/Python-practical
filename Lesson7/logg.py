from datetime import datetime
from time import time


def l_p_csv(l_info):
    t_inf = datetime.now().strftime('%H:%M')
    with open('Lesson7/log.csv', 'a') as log_file:
        log_file.write('[{}] Time {}\n'.format(l_info, t_inf))

def l_p_txt(l_info):
    t_inf = datetime.now().strftime('%H:%M')
    with open('Lesson7/log.csv', 'a') as log_file:
        log_file.write('[{}] Time {}\n'.format(l_info, t_inf))

def l_p_all(l_info):
    t_inf = datetime.now().strftime('%H:%M')
    with open('Lesson7/log.csv', 'a') as log_file:
        log_file.write('[{}] Time {}\n'.format(l_info, t_inf))

def l_w_csv(l_info):
    t_inf = datetime.now().strftime('%H:%M')
    with open('Lesson7/log.csv', 'a') as log_file:
        log_file.write('[{}] Time {}\n'.format(l_info, t_inf))

def l_w_txt(l_info):
    t_inf = datetime.now().strftime('%H:%M')
    with open('Lesson7/log.csv', 'a') as log_file:
        log_file.write('[{}] Time {}\n'.format(l_info, t_inf))

def l_s_txt(l_info):
    t_inf = datetime.now().strftime('%H:%M')
    with open('Lesson7/log.csv', 'a') as log_file:
        log_file.write('[{}] Time {}\n'.format(l_info, t_inf))

def l_c_csv(l_info):
    t_inf = datetime.now().strftime('%H:%M')
    with open('Lesson7/log.csv', 'a') as log_file:
        log_file.write('[{}] Time {}\n'.format(l_info, t_inf))

def l_c_txt(l_info):
    t_inf = datetime.now().strftime('%H:%M')
    with open('Lesson7/log.csv', 'a') as log_file:
        log_file.write('[{}] Time {}\n'.format(l_info, t_inf))