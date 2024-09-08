array = [i for i in range(1,33)]
print(array)

m = int(input())
def binarysearch(arr, n):

    lower_bound = 0
    upper_bound = len(arr)-1
     
     
    while lower_bound <= upper_bound:
        midpoint = int((lower_bound+upper_bound)/2)
        if n > arr[midpoint]:
            lower_bound = midpoint + 1
        elif n < arr[midpoint]:
            upper_bound = midpoint - 1
        elif n == arr[midpoint]:
            return str(n) + " is in the list."
        
    return -1
    
print(binarysearch(array, m))
