import random
import time
import matplotlib.pyplot as plt

# Part 1: Defining Vehicle Class
class Vehicle:
    def __init__(self, manufacturer, model, type, cost, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.type = type
        self.cost = cost
        self.mileage = mileage
    
    def __repr__(self):
        return f"{self.manufacturer} {self.model} ({self.type}) - ${self.cost}, {self.mileage} miles"
    
    def __lt__(self, other):
        return self.cost < other.cost

# Part 2: Sorting Algorithms
# Selection Sort
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

# Merge Sort
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Bubble Sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def sort(lst, alg):
    return alg(lst[:])  # Returned sorted copy

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
