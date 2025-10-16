import numpy as np 
 
# Get help on add 
help(np.add) 
 
# Check if none are zero 
arr = np.array([1, 2, 3, 4, 5]) 
print("Array:", arr) 
print("None of the elements is zero:", np.all(arr)) 
 
# Comparisons 
a = np.array([1, 2, 3, 4]) 
b = np.array([2, 2, 1, 4]) 
print("Greater:", np.greater(a, b)) 
print("Greater or Equal:", np.greater_equal(a, b)) 
print("Less:", np.less(a, b)) 
print("Less or Equal:", np.less_equal(a, b)) 
print("Equal:", np.equal(a, b)) 
print("Allclose:", np.allclose(a, b)) 
 
# Create arrays 
zeros_array = np.zeros(5) 
ones_array = np.ones(5) 
linspace_array = np.linspace(0, 10, 5) 
print("Zeros array:", zeros_array) 
print("Ones array:", ones_array) 
print("Linspace array:", linspace_array) 
# Convert to list 
array_list = a.tolist() 
print("Array converted to list:", array_list)
