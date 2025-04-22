# Global variable
num_calls = 0

# Partition using middle element as pivot
def partition(user_ids, l, h):
    pivot = user_ids[(l + h) // 2]
    while l <= h:
        while user_ids[l] < pivot:
            l += 1
        while user_ids[h] > pivot:
            h -= 1
        if l <= h:
            user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
            l += 1
            h -= 1
    return l

# Quicksort with global counter
def quicksort(user_ids, l, h):
    global num_calls
    num_calls += 1

    if l < h:
        index = partition(user_ids, l, h)
        quicksort(user_ids, l, index - 1)
        quicksort(user_ids, index, h)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
        
    # Initial call to quicksort 
    quicksort(user_ids, 0, len(user_ids) - 1)
    
    # Print number of calls to quicksort
    print(num_calls)
    
    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
