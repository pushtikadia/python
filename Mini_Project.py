# Mini Project Using "numpy"
import numpy as np
import matplotlib.pyplot as plt

# Generate random dataset
np.random.seed(42)
data = np.random.randint(1, 100, size=100)

# Compute basic statistics
mean_val = np.mean(data)
median_val = np.median(data)
std_val = np.std(data)
var_val = np.var(data)

# Display statistics
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Standard Deviation: {std_val}")
print(f"Variance: {var_val}")

# Plot histogram
plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_val:.2f}')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Generated Data")
plt.legend()
plt.show()
