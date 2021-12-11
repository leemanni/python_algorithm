#!/usr/bin/env python
# coding: utf-8

# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

# In[20]:


def solution(num):
    count = 0
    while num > 1:
        count += 1
        num =  num // 2 if num % 2 == 0 else num * 3 + 1
        if count == 500 :
            return -1
    return count


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




