# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:32:13 2021

@author: Donya
"""

def is_unique(s:str)->bool:
    """It takes string s and returns true if its 
    characters are unique."""
    s = s.replace(" ", "")
    return(len(s)==len(set(s)))



def check_permutation_1(s1:str,s2:str)->bool:
    """This function takes two strings s1 and s2, and
    return true if one is the permutation of the another by sorting."""
    return(sorted(s1)==sorted(s2))



def check_permutation_2(s1:str,s2:str)->bool:
    """This function takes two strings s1 and s2, and
    return true if one is the permutation of the another using hash."""
    import collections
    d= collections.defaultdict(int)
     
    for i in s1:
        d[i] += 1
        
    for i in s2:
        d[i] -= 1
        
    return not any(d.values()) 



def palindrome_permutation(s:str)->bool:
    """checks whether a string is a permutation of a plandrome"""
    import collections
    d = collections.defaultdict(int)
    for i in s:
        d[i]+=1
    print(d)
    count=0
    for v in d.values():
        if v%2 != 0:
            count+=1
            if count > 1:
                print('Not palindrome')
                return
    return('palindrome')



def urlify(s:str)->str:
    """Takes a string 
    and then puts %20 instead of spaces"""   
    mylist = list(s)
    for m in range(len(s)):    
        if mylist[m] == ' ':
            mylist[m] = '20%'  
    result=''.join(map(str, mylist))
    print(result)    
    
                