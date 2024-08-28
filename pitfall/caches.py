import time
import matplotlib.pyplot as plt

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def measure_warm_cache_effect(file_path, iterations=10):
    times = []
    
    for i in range(iterations):
        print(f"Starting iter {i}")
        start_time = time.time()
        read_file(file_path)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
    
    return times

def plot_warm_cache_effect(times):
    plt.plot(times, marker='o')
    plt.title("Warm Cache Effect: Time Taken to Read a File")
    plt.xlabel("Iteration")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.savefig("warm_cache_effect.png")  # Save the plot as a PNG file
    print("Saved")

# Example usage
file_path = 'example.txt'  # Replace with your file path
iterations = 10  # Number of times to read the file

times = measure_warm_cache_effect(file_path, iterations)
plot_warm_cache_effect(times)

