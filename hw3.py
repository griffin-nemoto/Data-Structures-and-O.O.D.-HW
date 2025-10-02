import random
import time
def generate_lists(size):
    '''Generates two lists with length 'size' with random integer elements
    Parameters: size - (int) desired length of lists
    Returns 2 randomly generated lists of length 'size' 
    '''
    list1 = random.sample(range(size*2),size)
    list2 = random.sample(range(size*2),size)
    return list1,list2

def find_common(list1, list2):
    '''Finds the number of common values in two lists
    Parameters: list1, list2 - (list) lists with randomly generated integers of the same size
    Returns: count - (int) number of common values in the two lists'''
    count = 0                          # +1
    for num1 in list1:                 # n*
        for num2 in list2:             #    n*
            if num1 == num2:           #          1+
                count += 1             #            2
    return count                       # +1
                                    # Total: 2+ 3n^2 = O(n^2)
def find_common_efficient(list1, list2):
    '''Finds the number of common values in two lists faster
    Parameters: list1,list2 - (list) lists with randomly generated intgers of the same size
    Returns: count - (int) number of common values in the two lists'''
    # Casts list1 to a set to remove duplicates, then uses .intersection(list2) to find the common values
    return len(set(list1).intersection(list2)) # 2n + 1
                                        # Total: 2n + 1 = O(n)


def measure_time():
    '''Prints table with list sizes and corresponding times to run find_common and find_common_efficient
    No Parameters
    No Returns
    '''
    sizes = [10,100,1000,10000,20000]
    common_list = []
    efficient_list = []
    for i in range(len(sizes)):
        s1 = time.time()
        list1,list2 = generate_lists(sizes[i])
        find_common(list1,list2)
        e1 = time.time()
        s2 = time.time()
        find_common_efficient(list1,list2)
        e2 = time.time()
        common_list.append(e1-s1)
        efficient_list.append(e2-s2)
    print('List size:              find_common Time(s)               find_common_efficient Time(s)')
    print('----------              --------------------              -------------------------------')
    for i in range(len(sizes)):
        print(f'{sizes[i]}              {common_list[i]}                    {efficient_list[i]}')

if __name__ == "__main__":
    measure_time()

