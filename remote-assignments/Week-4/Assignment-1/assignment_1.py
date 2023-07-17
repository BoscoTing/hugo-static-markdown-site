import threading
from time import sleep

def do_job(number): 
    sleep(3)
    print(f"Job {number} finished")

def main():
    for i in range(5):
        t = threading.Thread(target=do_job, args=(i,))
        t.start()

main()

