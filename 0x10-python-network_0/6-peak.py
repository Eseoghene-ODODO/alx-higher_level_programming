def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.
    
    Args:
    - list_of_integers: A list of unsorted integers
    
    Returns:
    - The peak value found in the list
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)
    else:
        mid = n // 2
        if list_of_integers[mid] < list_of_integers[mid-1]:
            return find_peak(list_of_integers[:mid])
        elif list_of_integers[mid] < list_of_integers[mid+1]:
            return find_peak(list_of_integers[mid+1:])
        else:
            return list_of_integers[mid]
