def lower_alpha(arr): #make list of only alpha
    a = [i.lower() for i in arr] #list each char in string as lower case
    for i in a :
        if i.isalpha() == False:
            a.remove(i)
    return a

