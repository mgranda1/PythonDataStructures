# Python containers
# Lists

import copy
empty_list = []

# Homogenous list
hourly_temperatures = [21.5, 21.0, 20.5, 20.3, 20.1]
print(f'Temperatures: {hourly_temperatures}')
print(f'List length: {len(hourly_temperatures)}')

# Heterogenous list
file_info = ["report.pdf", 2.4, True]
print(f'File info: {file_info}')
print(f'List length: {len(file_info)}')

# Access last element of the list
print(f'Last element of homogenous list: {hourly_temperatures[-1]}')
print(f'Last element of heterogenous list: {file_info[len(file_info) - 1]}')

# Append element 
hourly_temperatures.append(19.0)
print(f'Temperatures after appending: {hourly_temperatures}')
hourly_temperatures.insert(1, 18.0)
print(f'Temperatures after inserting at first index: {hourly_temperatures}')

# Concatenate lists
new_list = hourly_temperatures + file_info
print(f"New concatenated list: {new_list}")

# Extending list
new_hourly_temperatures = [17.1, 16.3, 15.8]
hourly_temperatures.extend(new_hourly_temperatures)
print(f"Extended hourly temperatures list: {hourly_temperatures}")

# Remove element of the list (by default last)
removed_value = hourly_temperatures.pop()
print(f'Temperatures after using pop(): {hourly_temperatures}, removed value: {removed_value}')

# Remove (by default first) occurence of item
hourly_temperatures.remove(17.1)
print(f'Temperatures after using remove(17.1): {hourly_temperatures}')

# Clear list
file_info.clear()
print(f"Cleared file_info: {file_info}")

# Iterating over list elements
instruments = ["guitar", "piano", "drums"]
for i in instruments:
    print(f"I can play {i}")

for i, item in enumerate(instruments, 1):
    print(f"{i}, {item}")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    print(row)
    for i, v in enumerate(row,1):
        print(v, end = '')
        if i != len(row):
            print(', ', end = '')
    print("")

# Return occurences of the value
statuses = ["online", "offline", "online", "error", "online"]
online_cound = statuses.count("online")

# Find index of the first occurence
if "error" in statuses:
    first_error_occurence = statuses.index("error")
    print(f"\"error\" at position: {first_error_occurence}")
else:
    print("\"error\" not in the list")

# Sorting 
hourly_temperatures.sort()
print(f"Reverse sorted list: \n{hourly_temperatures}")

# New list 
new_sorted_list = sorted(hourly_temperatures, reverse=True)
print(new_sorted_list)

new_sorted_list.reverse()
print(new_sorted_list)

# Slices
num = ['1', 2, 5, 9, 13, ['a', 'b', 'd']]
print(f"Original list: {num}")

# Alias to list, pointing to the same place in memory
n = num
n.pop(2)
print(f"After pop(2) : \norg: {num}\nnew: {n}")

# Shallow copy of the list, you can also use [:]
copied = list(num)
copied.pop(2)
print(f"After pop(2) from copied list : \norg: {num}\nnew: {copied}")

# List elements are implemented as references to the specific objects in memory
settings = [['vol', 50], ['bright', 10], 200, "OK"]

# new_settings holds references to the same objects as the original settings list
new_settings = settings[:]
new_settings[0][1] = 99
print(f"After new_settings[0][1]\nsettings: {settings}\nnew_settings:{new_settings}")

# Deep copy holds references to the new copies of elements from the list
deep_copy = copy.deepcopy(settings)

# Unpacking and extended unpacking
vol, bright, *other = settings
print(f"{vol}\n{bright}\n{other}")

#List comprehension
numbers = [0,1,2,3,4,5,6]
squares = [n ** 2 for n in numbers]
odd = [n for n in numbers if n % 2 != 0]
print(squares)
print(odd)

# Joining and splitting
linux_path = '/'.join(['home','user', 'Desktop'])
print(linux_path)
print(linux_path.split('/'))

# Aggregate functions
print(f"numbers: {numbers}")
print(f"sum: {sum(numbers)}")
print(f"min: {min(numbers)}")
print(f"max: {max(numbers)}")
print(f"any: {any(numbers)}")
print(f"all: {all(numbers)}")
