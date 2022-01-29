class BinarySearch(object):

    elements = []

    def __init__(self, n):
        for i in n.split(" "):
            self.elements.append(int(i))

    def find(self, value):
        low = 0
        high = int(len(self.elements) - 1)
        while low <= high:
            middle = int(low + (high - low) / 2)
            if value < self.elements[middle]:
                high = middle - 1
            elif value > self.elements[middle]:
                low = middle + 1
            else:
                return middle
        return False
