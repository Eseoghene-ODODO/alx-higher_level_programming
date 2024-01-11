#!/usr/bin/python3
"""
A function that returns the weighted average of all integers tuple
(<score>, <weight>)
"""



def weight_average(my_list=[]):
    """ Function body """
    if not my_list:
        return 0

    total_weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    if total_weight == 0:
        return 0

    return total_weighted_sum / total_weight
