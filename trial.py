from my_functions import reverse_list as rev, lower_alpha as lwalp

def ispal(string):
    p1 = lwalp(string)
    p = p1[:]
    p2 = rev(p)

    return p1 == p2

