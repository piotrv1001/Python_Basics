di = {1: "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five"}

# 1. Copy dictionary ( shallow copy ) vs = operator ( reference )
print("1.", end = ' ')
di2 = di.copy()
print(di2)

# 2. Clear dictionary
print("2.", end = ' ')
di2.clear()
print(di2)

# 3. Create dict from keys and keep value as reference
print("3.")
keys = {'a','e','i','o','u'}
value = [1]
di3 = dict.fromkeys(keys, value)
print(di3)
value.append(2)
print(di3)

# 4. Get value for key and specify what to return if key not found
print("4.", end = ' ')
print(di.get(6 ,-1))

# 5. Get dict items
print("5.")
for item in di.items():
    msg = "Key: {key}, Value: {value}".format(key = item[0], value = item[1])
    print(msg)

# 6. Get dict keys
print("6.", end = ' ')
print(di.keys())

# 7. Pop last inserted item and return it
print("7.")
item = di.popitem()
print(item)
print(di)

# 8. Set default
print("8.")
two = di.setdefault(2)
print(two)
no = di.setdefault(7)
print(no) # None cuz 6 not present
six = di.setdefault(6, "six") # Add 6 to dict and return "six"
print(di)
print(six)

# 9. Pop item
print("9.")
popped = di.pop(2)
print(popped)
print(di)

# 10. Get dict values
print("10.")
print(di.values())

# 11. Update the dict
print("11.")
new = (8, "eight")
new2 = {9 : "nine"}
di.update([new])
di.update(new2)
print(di)




