#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01."""


def get_party_stats(families, table_size=6):
    """Function takes two parameters and return and return a headcount for
        caterer and total number of tables needed.
        Arg:
            families(str): list of families which are themselves list of
                            members.
            table_size(int): maximum no. of seats at each table.
        Return:
               returns the total no. of guests and total tables needed.
        Examples:
            get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
            'Janis']])
            (6, 3)
    """
    total_guests = 0
    total_tables = 0
    for people in families:
        family = len(people)
        total_guests += family
        total_tables += -(-family//table_size)

    return (total_guests, total_tables)
