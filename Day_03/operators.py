# Day 3: 30 Days of Python programming - Operators
# Name: Annamary Shiju
# Staff: Sathish Kumar M

age = 20
height = 5.6
complex_num = 1 + 2j

# Area of a triangle (b = 20, h = 10)
base = 20
h = 10
area_triangle = 0.5 * base * h
print('Triangle Area:', area_triangle)

# Perimeter of a triangle (a = 5, b = 4, c = 3)
a, b, c = 5, 4, 3
perimeter_triangle = a + b + c
print('Triangle Perimeter:', perimeter_triangle)

# Rectangle calculations (length = 10, width = 5)
length = 10
width = 5
rect_area = length * width
rect_perimeter = 2 * (length + width)
print('Rectangle Area:', rect_area)
print('Rectangle Perimeter:', rect_perimeter)

# Comparison operations
print('Length comparison:', len('python') != len('dragon'))
print('Is "on" in python and dragon:', ('on' in 'python') and ('on' in 'dragon'))
print('Is "jargon" in sentence:', 'jargon' in 'I hope this course is not full of jargon')

# Check even/odd
num = 8
is_even = (num % 2 == 0)
print(f'Is {num} even?:', is_even)

# Floor division and type comparison
floor_div_check = 7 // 3 == int(2.7)
print('7 // 3 == int(2.7):', floor_div_check)

# String type vs int type comparison
print('type("10") == type(10):', type('10') == type(10))