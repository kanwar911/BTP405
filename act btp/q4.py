def stats_decorator(func):
    def wrapper(t):
        with open(t, 'r', encoding='utf-8') as file:
            for line in file:
                numbers = [float(num) for num in line.split() if num.replace('.', '', 1).isdigit()]
                if numbers:
                    print(f"Numbers read: {numbers}")
                    print(f"Count: {len(numbers)}")
                    print(f"Average: {sum(numbers) / len(numbers):.2f}")
                    print(f"Maximum: {max(numbers)}\n")
        return func(t)
    return wrapper

@stats_decorator
def printStats(t):
    pass  # The decorator handles all the printing

# Calling the function with the existing file in the folder
printStats("numbers.txt") 
