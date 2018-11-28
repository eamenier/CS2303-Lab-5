class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)
        self.perc_up(len(self.heap_array) - 1)
        
    def perc_up(self, node_ind):
        while node_ind > 0:
            parent_ind = (node_ind - 1) // 2
            if self.heap_array[node_ind] <= self.heap_array[parent_ind]:
                temp = self.heap_array[node_ind]
                self.heap_array[node_ind] = self.heap_array[parent_ind]
                self.heap_array[parent_ind] = temp
                node_ind = parent_ind

    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array.append[0]
        for i in range(len(self.heap_array)):
            if min_elem >= self.heap_array[i]:
                min_elem = self.heap_array[i]
        return min_elem
    
    def is_empty(self):
        return len(self.heap_array) == 0
    
    def heapify(self, len_array, node_ind):
        smallest = node_ind
        left = (2 * node_ind) + 1
        right = (2 * node_ind) + 2

        if (left < len_array) and (self.heap_array[left] < self.heap_array[smallest]):
            smallest = left 
        
        if (right < len_array) and (self.heap_array[right] < self.heap_array[smallest]):
            smallest = right

        if smallest != node_ind:
            temp = self.heap_array[node_ind]
            self.heap_array[node_ind] = self.heap_array[smallest]
            self.heap_array[smallest] = temp
            self.heapify(len_array,smallest)

    def heap_sort(self, len_array):
        start = (len_array // 2) - 1
        for i in range(start, 0, -1):
            self.heapify(start, i)
        start2 = len_array - 1
        for i in range(start2, 0, -1):
           temp = self.heap_array[i]
           self.heap_array[i] = self.heap_array[0]
           self.heap_array[0] = temp 
           self.heapify(i,0)
    
    def print_heap(self):
        for i in range(len(self.heap_array)):
            print(self.heap_array[i])
    
    def len_of_heap(self):
        length = 0
        for i in range(len(self.heap_array)):
            length += 1
        return length 

with open("test.txt", "r") as file:
    heap = Heap()
    nums = file.readline()
    heap.insert(nums.split(","))
    length = heap.len_of_heap()
    print(length)
    #heap.heap_sort(length)
    heap.print_heap()