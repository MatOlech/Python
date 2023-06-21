import sys
sys.path.append('/usr/lib/python3/dist-packages')
import psutil
import datetime
import time


def main():
    while True:  
        cpu_percent = psutil.cpu_percent()

        
        memory_percent = psutil.virtual_memory().percent

        
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        
        with open('server_load.txt', 'a') as file:
            file.write(f'{current_time}, CPU: {cpu_percent}%, Memory: {memory_percent}%\n')

        
        time.sleep(60)