import copy

# Discovering tuples
tuple_a = (1, 3)
tuple_b = (4, 7)
print(tuple_a + tuple_b)

# Zip function
list = []
z = zip(tuple_a, tuple_b)
t = tuple([a+b for a,b in z])
print(t)

# Reversing a tuple
tc = (1,2,3,4,5,6,8)
print(tuple((reversed(tc))))
print(tc[::-1])

# Sorting a tuple
values = (42, 5, 12 ,99, 18)
sorted_values = tuple(sorted(values))
print(sorted_values)

records = (
    ("s6", 30),
    ("s2", 13),
    ("s4", 67),
)

sorted_by_value = sorted(records, key= lambda item: item[1])
print(sorted_by_value)


products = (
    ('a', 120, 10),
    ('b', 200, 100),
    ('c', 150, 20)
) # name, price, discount

sorted_by_final_price = sorted(products, key= lambda x: x[1] - x[2])
print("Sorted after applying discount:", tuple(sorted_by_final_price))\

# Tuple with mutable element
modules = (['core', 'subcore'], 'auth', 'storage')
alias = modules
copied = modules[:]

print(modules is alias and modules is copied)

# If modules had immutable elements, deep_copy is modules would be true
deep_copy = copy.deepcopy(modules)
print(deep_copy is modules)

# Unpacking
dimensions = (10, 5, 2)
l, w, h = dimensions

def compute_volume(l, w, h):
    return l*w*h

# Unpack when calling a function with *
print(compute_volume(*dimensions))

# *sections packs arguments into a tuple
def gen_reports(title, *sections):
    print(sections)
    print (f"--- {title} ---")
    for i, section in enumerate(sections, 1):
        print(f"{i} section: {section}")


gen_reports("System report", "cpu usage: 67%", "hdd: 1.9TB free")

def min_max(t):
    # Implicit tuple
    return min(t), max(t)

# Unpack to min, max variables
min, max = min_max(values)
