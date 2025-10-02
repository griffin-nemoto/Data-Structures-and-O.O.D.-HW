import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes

class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort"""
    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3

def linear_scan(L):
    '''Counts number of out of place elements in list, returns different cases depending on that count'''
    inversions = 0

    for i in range(len(L) - 1):

        if L[i] > L[i+1]:
            inversions += 1

    if inversions == 0:
        return MagicCase.SORTED
    
    if inversions == len(L) - 1:
        return MagicCase.REVERSE_SORTED
    
    if inversions <= INVERSION_BOUND:
        return MagicCase.CONSTANT_INVERSIONS
    
    return MagicCase.GENERAL
    
    
    

def reverse_list(L, alg_set=None):
    '''Reverses given list'''
    if alg_set is None:
        alg_set = set()
        
    last_index = len(L) - 1

    for i in range(len(L) // 2):            #Only iterates through half the list to prevent switching elements back

        L[i],L[last_index - i] = L[last_index - i],L[i]    #Switches corresponding elements from front of end of list

    alg_set.add(reverse_list.__name__)
    
    return L

def magic_insertionsort(L, left, right, alg_set=None):
    '''Sorts given list from 'left' to 'right' indices using insertion sort'''

    if alg_set is None:
        alg_set = set()

    for i in range(left, right):

        j = i

        while j > left and L[j-1] > L[j]:

            L[j-1], L[j] = L[j], L[j-1]
            j -= 1

    alg_set.add(magic_insertionsort.__name__)

def magic_mergesort(L, left, right, alg_set = None):
    '''Sorts 'left' to 'right' indices of L using mergesort'''
    if alg_set is None:
        alg_set = set()

    alg_set.add(magic_mergesort.__name__)

    temp = L[left:right]    # Temporary list so that mergesort can be implemented normally

    _magic_mergesort(temp, alg_set)

    L[left:right] = temp    # Replaces original list bounds with sorted sublist

def _magic_mergesort(L, alg_set):
    '''Sorts L using mergesort, uses insertion sort for sublists <= 20'''
    
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]
    
    if len(B) <= 20:        # B will be the larger of the two lists if len is odd, calls insertion when it falls below length 20
        magic_insertionsort(A, 0, len(A), alg_set)
        magic_insertionsort(B, 0, len(B), alg_set)
    else:
        _magic_mergesort(A, alg_set)
        _magic_mergesort(B, alg_set)
    
    _merge(A, B, L)

def _merge(A, B, L):
    '''Merges two sorted lists into one sorted list'''
    i = j = 0
    
    while i < len(A) or j < len(B):

        if (j == len(B)) or (i < len(A) and A[i] < B[j]):

            L[i+j] = A[i]
            i += 1

        else:

            L[i+j] = B[j]
            j += 1

def magic_quicksort(L, left, right, alg_set=None):
    '''Sorts L from 'left' to 'right' using quicksort'''
    if alg_set is None:
        alg_set = set()

    alg_set.add(magic_quicksort.__name__)

    temp = L[left:right]
    if len(L) != 0:         # Only runs if list isn't empty
        worst_case = 3 * (math.log2(len(temp)) + 1)

        _quicksort(temp, 0, len(temp), alg_set, 0, worst_case)

        L[left:right] = temp

        

def _quicksort(L, left, right, alg_set, depth, worst_case):
    """Helper method for magic_quicksort, uses mergesort if several bad pivots are used, insertion sort when sublists <= 20"""

    if depth > worst_case:
        magic_mergesort(L, left, right, alg_set)

    if right - left <= 20:
        magic_insertionsort(L, left, right, alg_set)
        return L
    else:
    
        pivot = _partition(L, left, right)

        depth += 1
    
        _quicksort(L, left, pivot, alg_set, depth, worst_case)
        _quicksort(L, pivot + 1, right, alg_set, depth, worst_case)

    


def _partition(L, left, right):
    '''Partitions L for quicksort and returns the pivot index'''

    pivot = right - 1
    i = left
    j = pivot -1

    while i < j:
        
        while L[i] < L[pivot]:
            i += 1
            
        while i < j and L[j] >= L[pivot]:
            j -= 1
            
        if i < j:
            L[i], L[j] = L[j], L[i]
            
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i

    return pivot


def magicsort(L):
    '''Takes input list and sorts it using the most efficient algorithm and returns methods used'''
    alg_set = set()
    if linear_scan(L) == MagicCase.SORTED:
        return alg_set
    elif linear_scan(L) == MagicCase.REVERSE_SORTED:
        reverse_list(L, alg_set)
    elif linear_scan(L) == MagicCase.CONSTANT_INVERSIONS:
        magic_insertionsort(L, 0, len(L),alg_set)
    else:
        magic_quicksort(L, 0, len(L), alg_set)
    
    return alg_set
