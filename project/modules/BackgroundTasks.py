#https://stackoverflow.com/questions/59850517/how-to-run-background-tasks-in-python
import threading
import time

class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        while True:
            print('Hello')
            time.sleep(1)

t = BackgroundTasks()
t.start()
