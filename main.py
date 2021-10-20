class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryHeap:
    def __init__(self):
        self.root = None
        self.length = 0

        
    def append(self,value):
        node = Node(value)
        if self.length < 1:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while True:
                if len(queue) == 0:
                    break
                current = queue.pop(0)
                    
                if not current.left:
                    current.left = node
                    break

                elif not current.right:
                    current.right = node
                    break

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

        self.length += 1
    def inorder(self):
        return traverse([],self.root,self.length)
    def maxheapify(self):
        queue = [self.root]
        while True:
            if queue == []:
                break
            current = queue.pop(0)
            bubble(current.left,current.right,current,queue)

    def heapSort(self,heap):
        return hs([],self.root,heap)
    
    def clear(self):
        self.root = None
        self.length = 0


    #inorder traversal

def traverse(results,current,l):
    if l == 1:
        results.append(current.value)
    else:
        results.append(current.value)
        if current.left:
            traverse(results,current.left,l)
        if current.right:
            traverse(results,current.right,l)
    return results

def bubble(left,right,current,queue):
    if left and right:
        if left.value >= right.value :
            larger = left.value
        else:
            larger = right.value
            
        if current.value < larger:
            current.value,larger = larger,current.value

            if left.value >= right.value:
                left.value = larger
            else:
                right.value = larger

        queue.append(left)
        queue.append(right)

def hs(result,current,array):
    if len(array) < 2:
        result.append(array[0])
    else:
        result.append(current.value)
        array[array.index(current.value)] = array[-1]
        array.pop()
        bh.clear()
        for i in array:
            bh.append(i)
        for i in range(2):
            bh.maxheapify()
        print(bh.inorder())
        print(bh.root.value)
        hs(result,bh.root,bh.inorder())


    return result[::-1]





array = [37,14,4,25,97,21,38,41,87,29,
95,16,68,9,79]
bh = BinaryHeap()
for i in array:
    bh.append(i)

for i in range(4):
    bh.maxheapify()

print('space')
print(bh.heapSort(bh.inorder()))

        
