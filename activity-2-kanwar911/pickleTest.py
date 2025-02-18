# pickleTest.py

# program should read pickled Reading objects and write their contents to the console.  The number of objects should
# also be reported.
import pickle
import os
from reading import Reading

def read_pickled_files():
    total_readings = 0
    for i in range(3): 
        filename = f"consumer_{i}.pkl"
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                try:
                    while True:
                        reading = pickle.load(file)
                        print(reading)  
                        total_readings += 1
                except EOFError:
                    pass 
    print(f"Total Readings Read are: {total_readings}")

if __name__ == "__main__":
    read_pickled_files()
