# -*- coding: utf-8 -*-
"""
Eric Born
codewars.com
"""

# Categorize New Member

# Input will consist of a list of lists containing two items each. 
# Each list contains information for a single potential member. 
# Information consists of an integer for the person's age and an integer for 
# the person's handicap.
def openOrSenior(data):
    category = []
    for i in range(len(data)):
        if data[i][0] >= 55 and data[i][1] > 7:
            category.append('Senior')
        else:
            category.append('Open')
    return(category)
 
# test case       
openOrSenior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])

# desired output
# ["Open", "Open", "Senior", "Open", "Open", "Senior"]

# One-liner
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]