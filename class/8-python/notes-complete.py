
# ------------------------------------------------
# Example function in Python

def isEven(n):
    if (n % 2 == 0):
        return(True)
    return(False)

# ------------------------------------------------
# Quick practice 1:

# Write Python code to do the following:

# 1. Create an object x that stores the value "123"

x = "123"

# 2. Create an object y that is x converted to an integer

y = int(x)

# 3. Write code to confirm that y is indeed an integer

type(y) == int

# 4. Write a logical statement to determine if y is odd or even

(y % 2) == 0

# ------------------------------------------------
# Practice 1

# Write the following two functions in Python code:

# 1. hypotenuse(a, b): Returns the hypotenuse of the two lines of
#    length a and b.

def sqrt(x):
    return(x**0.5)
    
def hypotenuse(a, b):
    return(sqrt(a**2 + b**2))
    
def hypotenuse(a, b):
    return((a**2 + b**2)**0.5)

hypotenuse(3, 4)

# 2. isRightTriangle(a, b, c): Returns True if the triangle formed by
#    the lines of length a, b, and c is a right triangle and False otherwise.
#    **Hint**: you may not know which value (a, b, or c) is the hypotenuse.

def isRightTriangle(a, b, c):
    test1 = (c == hypotenuse(a, b))
    test2 = (b == hypotenuse(a, c))
    test3 = (a == hypotenuse(c, b))
    return(test1 | test2 | test3)

def isRightTriangle(a, b, c):
    test1 = (c == hypotenuse(a, b))
    test2 = (b == hypotenuse(a, c))
    test3 = (a == hypotenuse(c, b))
    return(test1 or test2 or test3)

isRightTriangle(3, 4, 5)

# ------------------------------------------------
# Practice 2

# Write the following two functions in Python code:

# 1. factorial(n): Returns the factorial of n, e.g. 3! = 3*2*1 = 6.
#    Note that 0 is a special case, and 0! = 1. Assume n >= 0.

# 2. nthHighestValue(n, x): Returns the nth highest value in a list of
#    numbers. For example, if x = [5, 1, 3], then nthHighestValue(1, x)
#    should return 5, because 5 is the 1st highest value in x, and
#    nthHighestValue(2, x) should return 3 because it's the 2nd highest
#    value in x. Assume that n <= len(x).

def factorial(n):
    if (n == 0):
        return(1)
    total = 1        
    for i in range(1, n+1):
        total = total*i
    return(total)

factorial(0) == 1
factorial(3) == 3*2*1

def nthHighestValue(n, x):
    x.sort(reverse = True)
    return(x[n-1])

def nthHighestValue(n, x):
    y = sorted(x, reverse = True)
    return(y[n-1])
    
nthHighestValue(1, [5,1,3]) == 5
nthHighestValue(2, [5,1,3]) == 3
nthHighestValue(3, [5,1,3]) == 1

# ------------------------------------------------
# Practice 3

# Write the following two functions in Python code:

# 1. sortString(s): Takes a string s and returns back an alphabetically
#    sorted string. **Hint**: Use list(s) to break a string into a list
#    of letters.

def sortString(s): 
    x = sorted(list(s))
    return("".join(x))

sortString("cba") == "abc"
sortString("abedhg") == "abdegh"
sortString("AbacBc") == "ABabcc"

# 2. areAnagrams(s1, s2): Takes two strings, s1 and s2, and returns True if
#    the strings are anagrams, and False otherwise. **Treat lower and upper
#    case as the same letters**.

def areAnagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return(sortString(s1) == sortString(s2))

def areAnagrams(s1, s2):
    return(sortString(s1.lower()) == sortString(s2.lower()))
    
areAnagrams("", "") == True
areAnagrams("aabbccdd", "bbccddee") == False
areAnagrams("TomMarvoloRiddle", "IAmLordVoldemort") == True


