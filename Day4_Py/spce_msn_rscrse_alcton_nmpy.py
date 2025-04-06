import numpy as np

np.random.seed(10)

resources = np.random.randint(3,6, size = (6,3))

print("resource = \n", resources)

total_resources = np.sum(resources, axis =0)

print(f"Total resources needed (tons): Oxygen: {total_resources[0]}, Water : {total_resources[1]}, Food: {total_resources[2]}")

max_value = np.max(resources)
max_index = np.unravel_index(np.argmax(resources), resources.shape)
resources_names = ["Oxygen", "Water", "Food"]
highest_resource = resources_names[max_index[1]]
print(f"\nHighest consumption in a month: {highest_resource} ({max_value} tons in month {max_index[0]+1})")

std_dev = np.std(resources, axis=0)
print(f"\nStandard deviation of consumption: Oxygen: {std_dev[0]:.1f}, Water: {std_dev[1]:.1f}, Food: {std_dev[2]:.1f}")

transposed = resources.T
print("\nTransposed matrix (resource-wise monthly breakdown):")

print(transposed)