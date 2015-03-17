#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02."""




def prepare_email(appointments):
    """
    """
    email = []

    
    LIST = 'Dear {}, n\I look forward to meet you on {} \nBest, \n Gp'
   
    #counter = 0
    for item in appointments:
        #counter += 1
        name = item[0]
        date = item[1]
        
        email.append(LIST.format(name, date))
        print LIST.format(name, date)
