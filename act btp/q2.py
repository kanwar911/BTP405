import matplotlib.pyplot as plt
import numpy as np

def graphSnowfall(filename):
    # Read data from file
    with open(filename, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file if line.strip().isdigit()]
    
    # Define range bins
    bins = np.arange(1, max(snowfall_data, default=50) + 10, 10)
    labels = [f"{bins[i]}-{bins[i+1]-1}cms" for i in range(len(bins)-1)]
    
    # Count occurrences in each range
    counts = np.histogram(snowfall_data, bins=bins)[0]

    # Display counts in console
    for label, count in zip(labels, counts):
        print(f"{count} between {label}")

    # Plot the bar graph
    plt.figure(figsize=(8,5))
    plt.bar(labels, counts, color='blue', alpha=0.7)
    plt.xlabel("Snowfall Ranges (cm)")
    plt.ylabel("Number of Occurrences")
    plt.title("Snowfall Accumulation Ranges")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

# Call the function with the file in the current folder
graphSnowfall("snowfall.txt")  # Ensure the file is in the same directory as the script.
