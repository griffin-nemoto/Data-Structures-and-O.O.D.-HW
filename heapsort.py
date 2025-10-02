def idx_left(L, idx, right):
    """Returns index of left child of idx unless the index is greater than 'right', then None"""

    left =  idx * 2 + 1

    return left if left < right else None

def idx_right(L, idx, right):
    """Returns index of right child of idx unless the index is greater than 'right', then None"""

    r_idx = idx * 2 + 2

    return r_idx if r_idx < right else None

def idx_max_child(L, idx, right):
    """Returns index of max child of idx unless the index is greater than 'right', then None"""
    l_idx = idx_left(L,idx,right)
    r_idx = idx_right(L,idx,right)

    if l_idx is None and r_idx is None:
        return None
    
    elif r_idx is None:
        return l_idx
    
    elif l_idx is None or L[r_idx] > L[l_idx]:
        return r_idx
    
    else:
        return l_idx
    
def swap(L, i, j):
    """Swaps elements at given indices"""

    L[i], L[j] = L[j], L[i]

    
def downheap(L, idx, right):
    """Downheaps item at index 'idx' until list is heap ordered from [idx-right)"""

    max = idx_max_child(L, idx,right)

    if max is not None and L[idx] < L[max]:

        swap(L, idx, max)
        downheap(L, max, right)

def heapsort(L):
    """Creates max-heap and then iterates until list is fully sorted"""

    for i in reversed(range(len(L) // 2)):

        downheap(L, i, len(L))


    for i in range(len(L)-1, 0, -1):
        

        swap(L, 0, i)
        downheap(L, 0, i)

    
