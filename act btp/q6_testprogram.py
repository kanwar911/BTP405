import random
import time
import matplotlib.pyplot as plt
from q6_sort import Vehicle, selection_sort, merge_sort, bubble_sort, sort
# Generating random vehicle data
manufacturers = ["Toyota", "Ford", "Honda", "BMW", "Tesla"]
models = ["Model X", "Corolla", "Civic", "F-150", "X5"]
types = ["Sedan", "SUV", "Truck", "Coupe"]

def generate_vehicles(num):
    return [Vehicle(random.choice(manufacturers),
                    random.choice(models),
                    random.choice(types),
                    random.randint(10000, 50000),
                    random.randint(0, 200000))
            for _ in range(num)]

# Experiment and Graph
sizes = [10, 50, 100, 500, 1000]
time_results = {"Selection Sort": [], "Merge Sort": [], "Bubble Sort": []}

for size in sizes:
    vehicles = generate_vehicles(size)
    
    for sort_alg, name in zip([selection_sort, merge_sort, bubble_sort], time_results.keys()):
        start_time = time.time()
        sort(vehicles, sort_alg)
        time_results[name].append(time.time() - start_time)

# Plotting results
plt.figure(figsize=(10, 5))
for name, times in time_results.items():
    plt.plot(sizes, times, label=name, marker='o')
plt.xlabel("Number of Vehicles")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithm Performance Comparison")
plt.legend()
plt.grid()
plt.show()
