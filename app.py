#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ['NUMEXPR_MAX_THREADS'] = '16'


# In[2]:


import streamlit as st


# In[3]:


import random as rd


# In[ ]:


st.title('오늘 저녁은 무엇을 먹을까?!')


    
num_inputs = st.number_input("☑후보 개수", min_value=1, max_value=10, value=1, step=1)

inputs = []
for i in range(num_inputs):
    input_value = st.text_input(f"✅후보 {i+1}", key=f"input_{i}")
    inputs.append(input_value)

if st.button("🍴🍴이중에 골라보자🍴🍴"):
    st.write(f"👨‍🍳저녁 후보들: {inputs}")


        
button = st.button('🎯🎯저녁 메뉴 고르기🎯🎯')

if button:
    k = rd.randint(0, num_inputs)
    st.success(inputs[k])


# In[ ]:




