#!/usr/bin/python3
""" 6-peak module """


def find_peak(list_of_integers):
    """ find the peak in a list of unsorted integers """

    size = len(list_of_integers)
    mid = size // 2
    mid_a = size

    if size == 0:
        return None

    while True:
        mid_a = mid_a // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_a // 2 == 0:
                mid_a = 2
            mid = mid + mid_a // 2
        elif (mid_a > 0 and 
                list_of_integers[mid] < list_of_integers[mid - 1]):
            if mid_a // 2 == 0:
                mid_a == 2
            mid = mid - mid_a // 2
        else:
            return list_of_integers[mid]
