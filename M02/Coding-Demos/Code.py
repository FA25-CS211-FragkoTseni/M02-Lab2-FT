import array
import time

# Declare an array of integers
my_array = array.array('i', [10, 20, 30, 40, 50])  # 'i' means integer type (int)

# Display the array
def DisplayArray(arr):
    print("Current array:", list(arr))

DisplayArray(my_array)

# Insert element at the end
def InsertAtEnd(arr, value):
    arr.append(value)

print("\nInsert 60 at the end:")
InsertAtEnd(my_array, 60)
DisplayArray(my_array)

# Insert element at the beginning
def InsertAtBeginning(arr, value):
    arr.insert(0, value)

print("\nInsert 5 at the beginning:")
InsertAtBeginning(my_array, 5)
DisplayArray(my_array)

# Insert element in the middle (at position pos)
def InsertAtMiddle(arr, pos, value):
    arr.insert(pos, value)

print("\nInsert 25 at position 3:")
InsertAtMiddle(my_array, 3, 25)
DisplayArray(my_array)

# Delete element from the end
def DeleteFromEnd(arr):
    if len(arr) > 0:
        arr.pop()

print("\nDelete from the end:")
DeleteFromEnd(my_array)
DisplayArray(my_array)

# Delete element from the beginning
def DeleteFromBeginning(arr):
    if len(arr) > 0:
        arr.pop(0)

print("\nDelete from the beginning:")
DeleteFromBeginning(my_array)
DisplayArray(my_array)

# Delete element from the middle (at position pos)
def DeleteFromMiddle(arr, pos):
    if 0 <= pos < len(arr):
        arr.pop(pos)

print("\nDelete from position 2:")
DeleteFromMiddle(my_array, 2)
DisplayArray(my_array)

# Search for an element
def SearchElement(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i  # index found
    return -1  # not found

print("\nSearch for 30:")
index = SearchElement(my_array, 30)
if index != -1:
    print(f"Element 30 found at index {index}")
else:
    print("Element 30 not found")

print("\nFinal array state:")
DisplayArray(my_array)

#DICTIONARY 
# Declare a dictionary
dict = {}

# -------------------------------
# Insert key-value pair
def InsertKeyValue(d, key, value):
    d[key] = value
    print(f"Inserted ({key}: {value}) successfully.")

# -------------------------------
# Update value for an existing key
def UpdateValue(d, key, newValue):
    if key in d:
        d[key] = newValue
        print(f"Key {key} updated successfully to {newValue}.")
    else:
        print("Key not found.")

# -------------------------------
# Delete a key-value pair
def DeleteKey(d, key):
    if key in d:
        del d[key]
        print(f"Key {key} deleted successfully.")
    else:
        print("Key not found.")

# -------------------------------
# Search for a value by key
def SearchByKey(d, key):
    if key in d:
        return d[key]
    else:
        return "Key not found"

# -------------------------------
# Display the dictionary
def DisplayDictionary(d):
    if d:
        print("Current Dictionary:")
        for key, value in d.items():
            print(f"{key}: {value}")
    else:
        print("Dictionary is empty.")

# -------------------------------
# MAIN PROGRAM DEMONSTRATION
# -------------------------------

# Insert some key-value pairs
InsertKeyValue(dict, 1, "1")
InsertKeyValue(dict, 2, "2")
InsertKeyValue(dict, 3, "3")

# Display dictionary after insertions
DisplayDictionary(dict)

# Update key 1
UpdateValue(dict, 1, "11")

# Delete key 3
DeleteKey(dict, 3)

# Search for a key
print("Search result for key 2:", SearchByKey(dict, 2))
print("Search result for key 99:", SearchByKey(dict, 99))

# Final dictionary state
DisplayDictionary(dict)


#COMPARISON
print("\n Performance Comparison ")

# Measure array insertion at beginning
start = time.time()
InsertAtBeginning(my_array, 5)
end = time.time()
print(f"Array insert at beginning took {end - start:.8f} seconds")

# Measure dict insertion
start = time.time()
InsertKeyValue(dict, 6, 60)
end = time.time()
print(f"Dict insert took {end - start:.8f} seconds")

# Measure array deletion at beginning
start = time.time()
DeleteFromBeginning(my_array)
end = time.time()
print(f"Array delete at beginning took {end - start:.8f} seconds")

# Measure dict deletion
start = time.time()
DeleteKey(dict, 6)
end = time.time()
print(f"Dict delete took {end - start:.8f} seconds")

# Measure array search
start = time.time()
SearchElement(my_array, 30)
end = time.time()
print(f"Array search took {end - start:.8f} seconds")

# Measure dict search
start = time.time()
SearchByKey(dict, 3)
end = time.time()
print(f"Dict search took {end - start:.8f} seconds")

print("\nFinal array state:")
DisplayArray(my_array)

print("Final dict state:")
DisplayDictionary(dict)