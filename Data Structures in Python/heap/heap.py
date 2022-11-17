class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, val):
        print("Inserting {} into the heap".format(val))

        self.heap.append(val)
        self.size+=1

        current = self.size-1

        while (self.heap[current] <
               self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def parent(self, pos):
        return pos//2

    def left_child(self, pos):
        return pos*2

    def right_child(self, pos):
        return (pos*2) + 1

    def is_leaf_node(self, pos):
        return pos >= self.size//2

    def extract_min(self):
        min_val = self.heap[0]
        self.swap(0, self.size-1)
        self.size-=1
        self.heapify(0)
        return min_val

    def heapify(self, pos):
        if self.is_leaf_node(pos):
            return

        if self.heap[pos] > self.heap[self.right_child(pos)]:
            self.swap(pos, self.right_child(pos))
            self.heapify(self.right_child(pos))
        if self.heap[pos] > self.heap[self.left_child(pos)]:
            self.swap(pos, self.left_child(pos))
            self.heapify(self.left_child(pos))

def main():
        minHeap = MinHeap()
        minHeap.insert(12)
        minHeap.insert(15)
        minHeap.insert(32)
        minHeap.insert(4)
        minHeap.insert(55)
        minHeap.insert(2)
        print(minHeap.heap)
        print(minHeap.extract_min())
        print(minHeap.heap)

        print(minHeap.extract_min())
        print(minHeap.heap)

        print(minHeap.extract_min())
        print(minHeap.heap)
if __name__ == "__main__":
        main()
