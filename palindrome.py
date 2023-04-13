class Palindrome:

    def __init__(self, s):
        self.s = s

    def isPalindrome(self):
        p1 = self.lower_alpha(self.s)
        p = p1[:]
        p2 = self.reverse_list(p)

        return p1 == p2

    def lower_alpha(self, arr): #make list of only alpha
        a = [i.lower() for i in arr] #list each char in string as lower case
        b = [j for j in a if j.isalpha() == True]
        
        return b
        
    def reverse_list(self, arr): #reverse a list using two pointers
        left = 0
        right = len(arr)-1

        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr
    
