#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02."""


def prepare_email(appointments):
    """Function takes client's name and date as input and return the
        email template formatted.
        Arg:
            appointments(mix): Input value of a list containing name and date.
        Return:
                returns an email template formatted for the input names
                and dates.
        Example:
                >>> prepare_email([('Jack', 2015), ('Max', 'March 3')])
                ['Dear Jack, \nI look forward to meeting you on 2015. \nBest,
                    \nMe',
                'Dear Max, \nI look forward to meeting you on March 3. \nBest,
                \nMe']
    """
    email = []
    list1 = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for item in appointments:
        email.append(list1.format(item[0], item[1]))

    return email
