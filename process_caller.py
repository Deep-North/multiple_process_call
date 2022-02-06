import time
import psutil
import subprocess
import _winapi

def recursive_process_starter(width: int, depth=1):
    # to do
    # Сделать проверку на корректность аргументов (инты, больше нуля и т.п.)
    if depth == 0:
        return
    for iterator in range(width):
        si = subprocess.STARTUPINFO()
        si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
        si.wShowWindow = subprocess.SW_HIDE
        process = subprocess.Popen('notepad.exe', startupinfo=si)
        pids.append(process.pid)
        recursive_process_starter(width, depth - 1)

def process_terminator(pid_list: list):
    for item in pid_list:
        process = psutil.Process(item)
        process.terminate()
        time.sleep(0.1)
        print('pid=' + str(item) + ' ' + str(process))

pids = []
recursive_process_starter(3, 2)
for i in range(10): print(psutil.cpu_percent(interval=0.1))
time.sleep(10)
process_terminator(pids)

for i in range(10): print(psutil.cpu_percent(interval=0.1))
# gives an object with many fields
print(psutil.virtual_memory())
# print(psutil._ppid_map())
