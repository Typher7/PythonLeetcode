"""
def lower_alpha(arr): #make list of only alpha
    a = [i.lower() for i in arr] #list each char in string as lower case
    for i in a :
        if i.isalpha() == False:
            a.remove(i)
    return a
"""


def lower_alpha(self, arr): #make list of only alpha
        a = [i.lower() for i in arr] #list each char in string as lower case using list comprehension
        b = [j for j in a if j.isalpha() == True]
        
        return b
