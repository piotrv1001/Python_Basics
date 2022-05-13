x = {"C++", "Python", "JavaScript", "HTML", "Java", "SQL", "SQL"}
print(x)

# 1. Remove item from set
print("1.", end = ' ')
x.remove("HTML")
print(x)

# 2. Add item to set
print("2.", end = ' ')
x.add("Kotlin")
print(x)

# 3. Copy set shallow copy and reference
print("3.")
y = x.copy()
y.add("Ruby")
print(x)
print(y)
z = x
z.add('C')
print(x)
print(z)

# 4. Clear set of all items
print("4.", end = ' ')
y.clear()
print(y)

# 5. Difference of sets C = A - B
print("5.", end = ' ')
a = {1, 2, 3, 4, 5}
b = {4, 5}
c = a.difference(b)
print(c)
print(a - b)

# 6. Difference and update
print("6.", end = ' ')
a.difference_update(b)
print(a)

# 7. Discard = safe remove, no exception if no item in set
print("7.", end = ' ')
x.discard("CSS")
x.discard("C++")
print(x)

# 8. Intersection
print("8.", end = ' ')
set1 = {1, 2, 3}
set2 = {2, 4, 5}
set3 = {2, 8, 9, 10}
print(set1.intersection(set2, set3))

# 9. Intersection update
print("9.")
print(set1)
set1.intersection_update(set2)
print(set1)

# 10. Are sets disjoint, no common elements
print("10.", end = ' ')
print(set1.isdisjoint(set2))

# 11. Is set a subset of another set
print("11.", end = ' ')
print(set1.issubset(set2))

# 12. Is set a superset of another set
print("12.", end = ' ')
print(set2.issuperset(set1))

# 13. Pop random element
print("13.")
random = x.pop()
print(random)
print(x)

# 14. Symmetric difference of sets, A or B but not both ( XOR )
print("14.", end = ' ')
set4 = {2, 3, 4}
set5 = {2, 6, 7}
print(set4.symmetric_difference(set5))

# 15. Symmetric difference update
print("15.", end = ' ')
set4.symmetric_difference_update(set5)
print(set4)

# 16. Union of 2 sets
print("16.", end = ' ')
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.union(s2))

# 17. Update set with iterables
print("17.", end = ' ')
s3 = s1.union(s2)
tup = (10, 11, 12)
s3.update(tup)
print(s3)