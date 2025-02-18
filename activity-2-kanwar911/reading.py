# create reading objects that has an arbitary structure
# ensure that you can create one that can print itself...and can be populated with randomly generated data

import threading
import pickle
import random
import time
from datetime import datetime

class Reading:
    def __init__(self):
        self.timestamp = datetime.now()
        self.value = random.uniform(0, 100)
    
    def __repr__(self):
        return f"Reading({self.timestamp}, {self.value:.2f})"

BUFFER = []
BUFFER_SIZE = 100
lock = threading.Lock()
condition = threading.Condition(lock)

class Producer(threading.Thread):
    def run(self):
        global BUFFER
        for _ in range(2000 // 7): 
            reading = Reading()
            with condition:
                while len(BUFFER) >= BUFFER_SIZE:
                    condition.wait()
                BUFFER.append(reading)
                condition.notify_all()

class Consumer(threading.Thread):
    def __init__(self, consumer_id):
        super().__init__()
        self.consumer_id = consumer_id

    def run(self):
        global BUFFER
        timeout = 60 
        start_time = time.time()
        with open(f"consumer_{self.consumer_id}.pkl", "wb") as file:
            while True:
                with condition:
                    while not BUFFER:
                        condition.wait(timeout=timeout)
                        if time.time() - start_time >= timeout:
                            return  
                    reading = BUFFER.pop(0)
                    condition.notify_all()
                pickle.dump(reading, file)
                start_time = time.time()  

producers = [Producer() for _ in range(7)]
consumers = [Consumer(i) for i in range(3)]

for p in producers:
    p.start()
for c in consumers:
    c.start()

for p in producers:
    p.join()
for c in consumers:
    c.join()

print("Processing completed.")

