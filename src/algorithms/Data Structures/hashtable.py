'''
When the set K of keys stored in a dictionary is much smaller than the universe
U of all possible keys, a hash table requires much less storage than a directaddress
table.

Using a hash function to map U to Keys
h : U -> {0,1,...,m-1}

We say that an element with key k hashes to slot h.k/; we also say that h.k/ is the hash value of
key k.

Theorem 11.1
In a hash table in which collisions are resolved by chaining, an unsuccessful search
takes average-case time ‚.1C˛/, under the assumption of simple uniform hashing.

Theorem 11.2
In a hash table in which collisions are resolved by chaining, a successful search
takes average-case time ‚.1C˛/, under the assumption of simple uniform hashing.

Since insertion takes O(1) worst-case time and deletion takes O(1)
worst-case time when the lists are doubly linked, we can support all dictionary
operations in O(1) time on average.
'''


# Collision resolution by chaining

def chained_hash_insert(T, x):
    # insert x at the head of list T[h(x.key)]


def chained_hash_search(T, x):
    # search for an element with key k un list T[h(k)]


def chained_hash_delete(T, x):
    # delete x from the list T[h(x.key)]


'''
Good hashing function

A prime not too close to an exact power of 2 is often a good choice for m. For
example, suppose we wish to allocate a hash table, with collisions resolved by
chaining, to hold roughly n D 2000 character strings, where a character has 8 bits.
We don’t mind examining an average of 3 elements in an unsuccessful search, and
so we allocate a hash table of size m D 701. We could choose m D 701 because
it is a prime near 2000=3 but not near any power of 2. Treating each key k as an
integer, our hash function would be
h(k) = k mod 701
'''

