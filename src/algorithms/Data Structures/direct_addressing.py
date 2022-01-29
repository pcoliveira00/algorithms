def direct_address_search(T, k):
    return T[k]


def direct_address_insert(T, x):
    T[x.key] = x


def direct_address_delete(T, x):
    T[x.key] = None


def max_element(T):
    for i in range(len(T) - 1, 0, -1):
        if T[i] is not None:
            return i
    return None


def min_element(T):
    for i in range(len(T)):
        if T[i] is not None:
            return i
    return None
