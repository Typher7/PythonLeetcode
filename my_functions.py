def reverse_list(arr): #reverse a list using two pointers
    left = 0
    right = len(arr)-1

    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def lower_alpha(arr): #make list of only alpha
    a = [i.lower() for i in arr] #list each char in string as lower case
    for i in a :
        if i.isalpha() == False:
            a.remove(i)
    return a

def alphaNum(c):
    return (ord("A") <= ord(c) <= ord("Z") or
    ord("a") <= ord(c) <= ord("z") or
    ord("0") <= ord(c) <= ord("9"))