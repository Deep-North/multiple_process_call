import time
import psutil
import subprocess

from psutil import NoSuchProcess


def recursive_process_starter(width: int, depth: int):
    """
    Рекурсивный запуск процессов.
    :param width:   Количество процессов порождаемых родительским процессом.
    :param depth:   Количество итераций порождения процессов.
    :return:        Рекурсивный вызов самого метода.
    """
    if width <= 0 or depth <= 0:
        print('Задайте положительное целое число.')
        return
    if depth == 0:
        return
    for iterator in range(width):
        try:
            si = subprocess.STARTUPINFO()
            si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
            si.wShowWindow = subprocess.SW_HIDE
            process = subprocess.Popen('notepad.exe', startupinfo=si)
            pids.append(process.pid)
            recursive_process_starter(width, depth - 1)
        except Exception:
            print('Не удалось запустить процесс.')
            pass


def process_terminator(pid_list: list):
    """
    Завершение списка процессов
    :param pid_list: Список процессов
    :return: None
    """
    for item in pid_list:
        try:
            process = psutil.Process(item)
            process.terminate()
        except NoSuchProcess:
            print('Такого процесса нет.')
            pass


def cpu_and_ram_metrix(n: int):
    """
    Получение среднего значения загрузки процессора в процентах.
    :param n: Количество опросов процессора с частотой 0.1 в секунду.
    :return: None
    """
    average = 0
    for i in range(n):
        average += psutil.cpu_percent(interval=0.1)
    average = average / n
    print('_______________________________________________')
    print('Загрузка процессора: ' + str(average) + '%')
    print('Данные по RAM:\n----------------------------')
    ram = str(psutil.virtual_memory()).replace('svmem(', '').replace(')', '').split(', ')
    for item in ram:
        print(item)


pids = []
cpu_and_ram_metrix(20)  # Загрузка процессора до запуска процессов
recursive_process_starter(4, -4)  # Запуск процессов
time.sleep(5)  # Пауза 5 секунд
cpu_and_ram_metrix(20)  # Загрузка процессора после запуска процессов
process_terminator(pids)
time.sleep(5)  # Пауза 5 секунд
cpu_and_ram_metrix(20)  # Загрузка процессора после завершения процессов
print('Суммарно было запущено ' + str(len(pids)) + ' процессов.')
