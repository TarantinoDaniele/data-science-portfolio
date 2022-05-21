#!/usr/bin/env python
# coding: utf-8

# In[1]:


# generate a .py for parameter storage
#!jupyter nbconvert --to script parameters.ipynb


# In[2]:


import os

from IPython.core.display import display, HTML
display(HTML("<style>.container { width: 90% !important; }</style>"))


# ## Import fun

# In[3]:


def open_csvfile(filename):
    pwd = os.getcwd()
    path_dir = pwd
    filename = filename
    
    path: str = path_dir + '\\' + filename
    return path


# In[ ]:




