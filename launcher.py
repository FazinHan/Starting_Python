#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os


# In[ ]:


'''
def breakbypart(string,s1):
    if type(string) != str:
        raise ValueError('Cannot break elements from non-string objects')
    if string.count(s1) == 0:
        return [string]
    elif string.count(s1) == 1 and string[-1] == s1:
        return [string[0:len(string)-1]]
    a = 0
    res = []
    for i in range(string.count(s1)+1):
        b = string.find(s1, a+1)
        res += [string[a:b]]
        a = string.find(s1, b)+1
    return res
'''
#discovered string.split() so is now obsolete^

def show_ftype(ftype):
    if type(ftype) != str:
        raise ValueError('Please provide a string to show_ftype()')
    find = os.popen(f'dir *.{ftype} /b')
    found = find.read()
    return found

def get_choice(menu):
    if type(menu) != list:
        raise ValueError('Lists make it easier to index and create a menu')
    for i in range(len(menu) if len(menu) == 1 else len(menu)-1):
        print(str(i+1)+': '+str(menu[i]))
    a = int(input('Please enter a number from above for your file selection>>> '))
    return menu[a-1]

#def json_to_xl(filename):
    


# In[ ]:


#print(breakbypart(show_ftype('json'),'\n'))
#print(show_ftype('ipynb'))
#get_choice(breakbypart(show_ftype('json'),'\n'))
#f = open(get_choice(show_ftype('py').split('\n')),'r')
#d = f.read()
#f.close()
d = get_choice(show_ftype('py').split('\n'))
os.system(f'python {d}')

