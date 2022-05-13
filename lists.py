x = [1, 2, 3, 4, 5]

# 1. Find index of element
print("1.", end = ' ')
print(x.index(1))

# 2. Add item to the end of the list
print("2.", end = ' ')
x.append(6)
print(x)

# 3. Extend the list with another list, tuple, set etc.
print("3.", end = ' ')
y = (7, 8)
x.extend(y)
print(x)
x += [9, 10]
print(x)

# 4. Insert item at specified index
print("4.", end = ' ')
x.insert(1, 1.5)
print(x)

# 5. Remove the first occurence of the element
print("5.", end = ' ')
x.remove(1.5)
print(x)

# 6. Count number of times element is in the list
print("6.", end = ' ')
x.append(1)
print(str(x.count(1)))

# 7. Pop item at specified index, default -1 ( last item )
print("7.", end = ' ')
x.pop()
value = x.pop(0)
print(x, end = ' ')
print(f" Returned value: {value}")

# 8. Reverse the list
print("8.", end = ' ')
x.reverse()
# x = x[::-1]
print(x)

# 9. Sort the list with custom function
print("9.")
x.sort()
print(x)
x.sort(reverse = True)
print(x)
# take second element for sort
def takeSecond(elem):
    return elem[1]
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
random.sort(key = takeSecond)
# print list
print(random)

def customSort(item):
    return item % 3

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
items.sort(key = customSort)
print(items)

# 10. Copy, shallow copy = list.copy() and reference list1 = list2, slicing returns shallow copy
print("10.", end = ' ')
itemsCopy = items.copy()
itemsCopy.append(69)
print(items)
print(itemsCopy)
print('\n')
itemsCopy2 = items
itemsCopy2.append(69)
print(items)
print(itemsCopy2)

# 11. Clear all items
print("11.", end = ' ')
itemsCopy.clear()
print(itemsCopy)

# 12. Count item
print("12.", end = ' ')
x1 = [1, 2, 3, 4, 1, 1]
print(x1.count(1))

