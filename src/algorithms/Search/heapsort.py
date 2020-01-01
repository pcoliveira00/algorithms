import math

def parent(i):
    return i/2

def left(i):
    return 2*i + 1 

def right(i):
    return 2*i + 2

def exchange(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp

def max_heapify(A, i):
    l = left(i)
    r = right(i)

    largest = -1

    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i 
    
    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        exchange(A, i, largest)
        max_heapify(A, largest)

def min_heapify(A, i):
    l = left(i)
    r = right(i)

    lowest = -1

    if l <= len(A) - 1 and A[l] < A[i]:
        lowest = l
    else:
        lowest = i
    
    if r <= len(A) - 1 and A[r] < A[lowest]:
        lowest = r

    if lowest != i:
        exchange(A, i, lowest)
        min_heapify(A, lowest)

def build_max_heap(A):
    half = math.floor(len(A)/2)

    for i in range(half,0,-1):
        max_heapify(A, i)

def build_min_heap(A):
    half = math.floor(len(A)/2)
    for i in range(half, 0, -1):
        min_heapify(A,i)

def heapsort(A):
    build_max_heap(A)
    for i in range(len(A), 2, -1):
        exchange(A, 0, i)
        max_heapify(A, 0)

def heap_max(A):
    return A[0]

def heap_extract_max(A):
    if len(A) < 1:
        return -1
    max = A[0]
    A[0] = A[len(A) - 1]
    max_heapify(A, 0)
    return max

def heap_increase_key(A, i, key):
    if key < A[i]:
        return -1
    
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        exchange(A, i, parent(i))
        i = parent(i)

def max_heap_insert(A, key):
    heap_increase_key(A, len(A), key)

if __name__ == "__main__":
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    B = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    #max_heapify(A, 2)
    # print(A)
    #min_heapify(B, 1)
    # print(B)
    build_max_heap(A)
    print(A)
    build_min_heap(B)
    print(B)