class QuickFind(object):
    elements = []

    def __init__(self, n):
        for i in n.split(' '):
            self.elements.append(int(i))

    def union(self, p, q):

        pid = self.elements[p]
        qid = self.elements[q]

        for i in self.elements:
            if self.elements[i] == pid:
                self.elements[i] = qid

    def connected(self, p, q):
        if self.elements[p] == self.elements[q]:
            return True
        return False
