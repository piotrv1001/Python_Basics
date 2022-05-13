
# 1. Absolute value
print("1.", end = ' ')
x = -20
print(abs(x))
# Magnitude of complex nums ( sqrt(a^2 + b^2))
c = 3 + 4j
print(abs(c))

# 2. Any with booleans, strings, lists etc.
print("2.", end = ' ')
bools = [True, False, True, False]
print(any(bools))
st = "0"
print(any(st))
di = {0 : "False", False : "False again"}
# Looks at keys
print(any(di))

# 3. All, similar to any but all must be true
print("3.", end = ' ')
print(all(bools))

# 4. ASCII conversion
print("4.", end = ' ')
otherText = 'Pythön is interesting'
print(ascii(otherText))

# 5. Return binary string of int with 0b prefix
print("5.", end = ' ')
n = 5
print(bin(5))

# 6. Convert to bool
x = []
y = 0
z = 0j
print("6.")
print(bool(x))
print(bool(y))
print(bool(z))

# 7. Get bytearray
print("7.", end = ' ')
size = 5
print(bytearray(size))

# 8. Check if it's callable
print("8.")
x = 5
print(callable(x))
def fun():
    print("Hello world")

print(callable(fun))

# 9. Get bytes
print("9.", end = ' ')
x = [1, 2, 3, 4, 5]
print(bytes(x))

#10. Convert int to char
print("10.", end = ' ')
x = 97
print(chr(x))

# 11. Compile code from string ( WTF )
print("11.", end = ' ')
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'built_in', 'exec')

exec(codeObejct)

# 12. Create complex number
print("12.")
print(complex(5, 3)) # 5 + 3j
print(complex("4+4j")) # No spaces!

# 13. Create dict from kwargs ( keyword arguments )
print("13.", end = ' ')
di = dict(x = "1", y = "2", z = "3")
print(di)

# 14. Division and remainder in tuple
print("14.", end = ' ')
print(divmod(8 ,3)) # 8 / 3 = 2 reszty 2

# 15. Enumerate
print("15.")
grocery = ['bread', 'milk', 'butter']
for count, item in enumerate(grocery, 100):
  print(count, item)

# 16. Convert to static method
print("16.", end = ' ')
class Calculator:

    def addNumbers(num1, num2):
        return num1 + num2

Calculator.addNumbers = staticmethod(Calculator.addNumbers)
print(Calculator.addNumbers(3, 4))

# 17. Filter list
print("17.", end = ' ')
x = [1, 2, 3, 4, 5, 6, 7, 8]
def isEven(num):
    return num % 2 == 0

evenIterator = filter(isEven, x)
evenList = list(evenIterator)
print(evenList)

def isVowel(letter):
    vowels = "aeiou"
    return letter in vowels

letters = ['a','b','c','d','e','f']
vowelsList = list(filter(isVowel, letters))
print(vowelsList)

nums = [1.2, 1.4, 2.0, 3.0, 4.0, 5.3]
wholeNumbers = list(filter(lambda x: (x.is_integer()), nums))
print(wholeNumbers)