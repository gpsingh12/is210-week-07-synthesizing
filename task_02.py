#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02."""

def prepare_email(appointments):
    """
    """
    email = []
    
    
    name = appointments[0]
    date = appointments[1]
    LIST = 'Dear {}, n\I look forward to meet you on {} \nBest, \n Gp'
    email.append(LIST.format(name, date))
    for item in appointments:
        
        print email
    
