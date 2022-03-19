def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

# or sort
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c
