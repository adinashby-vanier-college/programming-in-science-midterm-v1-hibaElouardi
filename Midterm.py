import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    r = radius
    area_of_circle = (math.pi * r**2)

    return round(area_of_circle, 2)



# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n <= 3:
        return "The triangle height should be at least 4."
    
    result = ""

    for i in range(1, n + 1):
        if i == 1 or i == n:
            result += ("*" * i)
        else:
            result += "*" + (" " * (i - 2)) + "*"
        result += "\n"

    return result.rstrip()



# Q3: Inverted Pyramid
def inverted_pyramid(n):
    if n <= 2:
        return "The pyramid height should be at least 3."

    result = ""

    for i in range (1, n + 1):
        for j in range(i - 1):
            result += " "
        for k in range(2 * (n - i) + 1):
            result += "*"
        result += "\n"

    return result.rstrip()





# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()