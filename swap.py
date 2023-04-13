def swap_a(a,b):
    temp = a
    a = b
    b = temp
    return f"({a},{b})"
    
#Below is a shorter version for swapping
def swap_b(a,b):
    a,b = b,a
    return f"({a},{b})"

