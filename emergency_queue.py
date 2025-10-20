class Patient:
    def __init__(self, name, urgency):
        self.name=name
        self.urgency=urgency
class MinHeap:
    def __init__(self):
        self.data=[]
    def _parent(self, i): return (i-1)//2
    def _left(self, i): return 2*i+1
    def _right(self, i): return 2*i+2
    def heapify_up(self, index):
        while index>0:
            parent_index=self._parent(index)
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index]=self.data[parent_index], self.data[index]
                index=parent_index
            else:
                break
    def heapify_down(self, index):
        size=len(self.data)
        while True:
            left=self._left(index)
            right=self._right(index)
            smallest=index
            if left<size and self.data[left].urgency<self.data[smallest].urgency:
                smallest=left
            if right<size and self.data[right].urgency<self.data[smallest].urgency:
                smallest=right

            if smallest!=index:
                self.data[index], self.data[smallest]=self.data[smallest], self.data[index]
                index=smallest
            else:
                break
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)
    def peek(self):
        if not self.data:
            print("Queue is empty.")
            return None
        return self.data[0]
    def remove_min(self):
        if not self.data:
            print("Queue is empty.")
            return None
        if len(self.data)==1:
            return self.data.pop()
        root=self.data[0]
        self.data[0]=self.data.pop()
        self.heapify_down(0)
        return root
    def print_heap(self):
        print("\nCurrent Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")
if __name__=="__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()
    print("\nNext up:", heap.peek().name, heap.peek().urgency)

    served=heap.remove_min()
    print("\nServed:", served.name)
    heap.print_heap()
"""
A binary tree works perfectly for the doctor structure because it mirrors how hospital management naturally forms hierarchies; each doctor may supervise two others. 
Recursion makes traversal simple, since each node (doctor) calls on its subordinates. Preorder traversal is best when passing commands top-down (an example being a head doctor issuing orders). 
Inorder traversal works well when doctors need to be processed in a left-to-right order, like by department or seniority. 
Postorder traversal helps when summarizing results bottom-up, such as collecting performance data from individual teams before reporting to a higher-level doctor.
The emergency room system uses a min-heap, which is best for priority-based queues where the most urgent patient must always be handled first.
With every insert or removal, the heap efficiently reorganizes itself, maintaining the smallest urgency value (most critical patient) at the root. 
This means the next patient to be treated can always be accessed instantly. 
The heap operations run in logarithmic time which keeps the system responsive even as new patients arrive constantly. 
These same principles are used in real-world scheduling systems like CPU task management making the structure both practical and efficient.
"""
