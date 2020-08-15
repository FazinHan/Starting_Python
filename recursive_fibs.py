#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# In[24]:


def fib2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib2(n-1, memo) + fib2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None]*(n+1)
    return fib2(n, memo)


# In[32]:


def fib_bottom_up(n):
    bottom = [None]*(n+1)
    bottom[1] = 1
    bottom[2] = 1
    for i in range(3,n+1):
        bottom[i] = bottom[i-1] + bottom[i-2]
    return bottom[n]

