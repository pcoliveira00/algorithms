class QuickUnion(object):

    elements = []

    def __init__(self, n):
        for i in n.split(" "):
            self.elements.append(int(i))

    def root(self, n):
        result = n
        while self.elements[n] != n:
            n = self.elements[n]

        return result

    def connected(self, p, q):
        if self.root(self.elements[p]) == self.root(self.elements[q]):
            return True
        return False

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        self.elements[p_root] = q_root
