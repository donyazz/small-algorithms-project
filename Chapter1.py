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
    
    
    
def one_away(s1:str,s2:str)->str:
    """takes two strings and outputs true if they are one edit away"""
    s1=list(s1)
    s2=list(s2)
    
    if abs(len(s1)-len(s2))>=2:
        return('No')
    
    if abs(len(s1)-len(s2))==1:
        if s1>s2:
            long=s1
            short=s2
        else:
            long=s2
            short=s1
        flag=False
        a=0
        for i in range(len(long)-1):
            if (long[i+a] != short[i]):
                if flag == True:
                    return('No')
                else:
                    flag = True
                    a=1
        return('yes')
    
    if (len(s1)==len(s2)):
            flag=bool()
            for i in range(len(s1)):
                if (s1[i] != s2[i]):
                    if flag == True:
                        return('No')
                    else:
                        flag = not flag
    return('yes')
     
               
                
                