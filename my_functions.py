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


def searchInsert(nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid =(left+right)//2
            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
                
        return left
                
#print(searchInsert([2,4,6,7,9], 1))

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True
            
#print(is_prime(37))

def duplicate(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if i!=j and list[i]==list[j]:
                return True
    return False

def hashfunct(n):
    s=0
    while len(n)>1:
        for i in n:
            s+=int(i)
        n=str(s)
        s=0
    return int(n)

print(hashfunct(str(9935627547462643548638548636746249)))