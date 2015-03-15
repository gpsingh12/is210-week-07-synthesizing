#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02."""


def prepare_email(appointments):
    """
    """
    
    LIST = 'Dear {}, n\I look forward to meet you on.\nBest, \n Gp'

    counter = 0

    for item in appointments:
        counter += 1
        item = LIST
        #appointments = tuple(name), tuple(date)
        print item.format(appointments)

