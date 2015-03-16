#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01."""

#from math import ceil

def get_party_stats(families, table_size):
    """
    """
    total_guests = 0
    total_tables = 0
    for people in families:
        total_guests += len(people)
        tables = (-(-len(people)//table_size))
        total_tables += tables
    print (total_guests, total_tables)
