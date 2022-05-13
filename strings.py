x = 'Ala ma kota'

# 1. Convert to lower case
x = x.lower()
print("1.", end = ' ')
print(x)

# 2. Convert to upper case
x = x.upper()
print("2.", end = ' ')
print(x)

# 3. First letter is capital
x = x.lower()
x = x.capitalize()
print("3.", end = ' ')
print(x)

y = 'kot koty kotach'

# 4. Check if substring is in the string
print("4.", end = ' ')
if 'kot' in y:
    print("'kot' present in '" + y + "'")
else:
    print("'kot' NOT present in '" + y + "'")

# 5. Count substrings in string
counter = y.count('kot')
print("5.", end = ' ')
print("'kot' present " + str(counter) + " times in '" + y + "'")

# 6. Check if string ends with substring (suffix, start, end)
print("6.", end = ' ')
if y.endswith('tach', 3, len(y)):
    print(True)
else:
    print(False)

p = "Python is awesome"

# 7. Center the string with padding on both sides and fill it with characters
pp = p.center(24, "-")
print("7.", end = ' ')
print(pp)

f = "Hello world llo"

# 8. Find the lowest index with the found substring (substr, start, end), rfind starts searching from the end, if not found return -1
print("8.", end = ' ')
found = f.find('llo', 1, len(f))
if(found != -1):
    print("'llo' found in '" + f + "' at index: " + str(found))
else:
    print("'llo' not found in '" + f + "'")

rfound = f.rfind('llo')
print('rfind index: ' + str(rfound))

# 9. Reverse a string
rev_f = f[::-1]
print("9.", end = ' ')
print(rev_f)

# 10. Aggresive lower case e.g. ß -> ss
str1 = "der Fluß"
str2 = "der Fluss"
print("10.", end = ' ')
print(str1.casefold() == str2.casefold())

# 11. Apply different encoding (utf-8, ascii) with error strategy (ignore, replace)
d = 'pythön!'
print("11.", end = ' ')
print(d.encode('ascii','replace'))

# 12. String formatting
print("12.", end = ' ')
name = "Adam"
money = 10000.857
greeting = "Hello {name}, your account balance is: ${money:9.2f}".format(name = name, money = money)
print(greeting)

n = 1234
print("bin: {num:b}, oct: {num:o}, hex: {num:x}".format(num = n))

# 13. Finding index of substring, if not found raise exception
string = "YOLO"
print("13.", end = ' ')
print(str(string.index('LO')))

# 14. Check if all chars in string are alphanumeric ( numbers or alphabet ), no spaces or special characters
string2 = "Hello123"
print("14.", end = ' ')
print(string2.isalnum())

# 15. Check if all chars in string are alpha ( alphabet )
string3 = "JustinSavage"
print("15.", end = ' ')
print(string3.isalpha())

# 16. Check if all chars are decimal
string4 = '12345MP3'
print("16.", end = ' ')
print(string4.isdecimal())

# 17. Check if all chars are digits ( includes sub and super script )
print("17.", end = ' ')
string5 = '\u00B23455'
# string 5 = ²3455
print(string5, end = ' ')
print(string5.isdigit())

# 18. Check if a string is a Python identifier
print("18.", end = ' ')
string6 = "Python33"
string7 = "33Python"
print(string6.isidentifier(), end = ' ')
print(string7.isidentifier())

# 19. Check if all chars are lower case
print("19.", end = ' ')
string8 = "Ala ma kota"
print(string8.islower())

# 20. Check if string contains only whitespace chars
print("20.", end = ' ')
string9 = "\n   \t"
print(string9.isspace())

# 21. Check if string is title e.g. Hello World Python
print("21.", end = ' ')
string10 = "Hello World PYTHON"
print(string10.istitle())

# 22. Check if all chars are upper case
print("22.", end = ' ')
string11 = "HeLLO WORLD"
print(string11.isupper())

# 23. String join with lists
print("23.", end = ' ')
list1 = ["Hello", "world", "Python", "again!"]
print(' '.join(list1))

seperator = ' || '
print(seperator.join(list1))

dict1 = {"key1" : 1, "key2" : 2, "key3" : 3}
print('->'.join(dict1))

# 24. Adjust string with min length(6) to left and right and fill chars
print("24.", end = ' ')
string12 = "cat"
print(string12.ljust(6, '-'))
print(string12.rjust(6, '-'))

# 25. Swap case
print("25.", end = ' ')
string13 = "Ala ma KOTA"
string14 = string13.swapcase()
print(string14)

# 26. Strip the string of some chars
print("26.", end = ' ')
string15 = "https://www.programiz.com/"
print(string15.strip('https://'))

string16 = "Python is cool      "
print(string16.rstrip())

string17 = "xoxo love xoxo"
print(string17.strip('xoe'))

# 27. String partition
print("27.", end = ' ')
string18 = "Python is fun"
print(string18.partition('is '))

# 28. Split the string into list of words
print("28.", end = ' ')
string19 = "Hello Python World Again"
print(string19.split(' ')) # 4 items
print(string19.split(' ', 2)) # 3 items ( maxsplit + 1 )

# 29. String mapping with dictionaries ( 'a' = 97 ASCII )
print("29.", end = ' ')
string20 = "abc"
dict2 = {"a" : 123, "b" : 456, "c" : 789}
print(string20.maketrans(dict2))

# 30. String mapping part 2
print("30.", end = ' ')
first_string = "abc"
second_string = "efg"
third_string = "ab"

string21 = "abcdef"
translation1 = string21.maketrans(first_string, second_string, third_string) # third string resets mapping of 'ab' to None
translation2 = string21.maketrans(first_string, second_string)

print("Translated(1) string: " + string21.translate(translation1))
print("Translated(2) string: " + string21.translate(translation2))

# 31. Replace char with another char in a string
print("31.", end = ' ')
string22 = "Ala ma kota"
replace_string22 = string22.replace('a','A')
print(replace_string22)
print(string22.replace('a','A', 1))

# 32. Find maximum index of substring, if not exists return -1
print("32.", end = ' ')
string23 = "kot kota koty"
print(str(string23.rfind('kot')))
print(str(string23.find('kot')))

# 33. Split string on lines
print("33.", end = ' ')
string24 = "Hello\nWorld\nPython"
print(string24.splitlines())

# 34. Check if string starts with substring ( prefix, start, end )
print("34.", end = ' ')
string25 = "Python is amazing"
print(string25.startswith('Py'))
print(string25.startswith('Py', 2, 6))

# 35. Convert string to title
print("35.", end = ' ')
string26 = "hello world again again"
print(string26.title())

# 36. Fill start with zeros
print("36.", end = ' ')
string27 = "Python"
print(string27.zfill(10))
signed_string = "-223"
print(signed_string.zfill(6))

# 37. Format string with dict
print("37.", end = ' ')
point = {"x" : 4, "y" : 5}
print("Point: x = {x}, y = {y}".format_map(point))

# 38. Find highest index of substring, if not exists raise exception
print("38.", end = ' ')
string28 = "Pool Liverpool"
print(string28.rindex('pool'))