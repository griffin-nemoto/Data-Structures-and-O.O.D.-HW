def bubble_sort(matrix):
    '''Takes matrix as argument and uses bubble sort to sort the list in the first row
    Returns sorted list of first row and number of swaps'''


    n = len(matrix[0])

    if n == 0:
        return matrix[0], 0
    
    count = 0
    check_sort = True
    list1 = matrix[0]

    while check_sort:

        check_sort = False

        for i in range(n-1):

            if list1[i] > list1[i+1]:

                list1[i], list1[i+1] = list1[i+1], list1[i]
                count += 1
                check_sort = True

    return list1, count

def insertion_sort(matrix):
    """Uses insertion sort to sort 2nd row of given matrix, returns sorted list and number of swaps"""

    list2 = matrix[1]
    n = len(list2)

    if n == 0:
        return list2, 0
    
    count = 0 

    for i in range(n):
        
        j = i

        while j > 0 and list2[j-1] > list2[j]:
            
            list2[j-1], list2[j] = list2[j], list2[j-1]
            j -= 1
            count += 1
        
    return list2, count


def selection_sort(matrix):
    """Uses selection sort to sort 3rd row of given matrix, returns sorted list and number of swaps"""

    n = len(matrix[2])
    count = 0
    list3 = matrix[2]
    
    if n == 0:
        return list3, 0


    for i in range(n):

        min = i

        for j in range(i,n):
            
            if list3[j] < list3[min]:

                min = j

        if min != i:        # Only swaps and increases count if min isn't the current item anymore
                list3[i],list3[min] = list3[min],list3[i]
                count += 1 

    return list3, count

def merge(first_row, second_row, third_row):
    """
    Merges three sorted rows of the matrix into one sorted 1D list.
    
    Args:
        matrix (list of list of int): 2D list (matrix) where each row has 'n' elements and is sorted.
    
    Returns:
        list: A merged 1D list that contains all elements from the matrix in sorted order.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements
    
    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float('inf')
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row= 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move the corresponding index forward
        if target_row == 1: 
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list
