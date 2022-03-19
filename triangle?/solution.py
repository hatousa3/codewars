def is_triangle(a, b, c):
    if a*b*c > 0 and a + b > c and a + c > b and b + c > a:
        return True
    return False
