#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Assignment_2
Module spam
"""
import logging

def bacon() :
    """
    module bacon functionality
    """
    logging.info("in function bacon")
    try :
        logging.info("processing bacon function")
        print("in bacon funtionality")
    except Exception as e :
        logging.error(e)
