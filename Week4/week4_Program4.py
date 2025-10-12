import os
import datetime

try:
    path = "C:/Users/sreej/Downloads"
    files = os.listdir(path)
    for file in files:
        print(file)
except FileNotFoundError as e:
    with open("error_log.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} - Error: {e}\n")

start_time = datetime.datetime.now()
with open("process_log.txt", "a") as log:
    log.write(f"Process started at: {start_time}\n")
print("Process started at:", start_time)
