class SegmentTree(object):
    def __init__(self, arr):
        n = len(arr)
        self.lo = [-1]*(4*n+1)
        self.hi = [-1]*(4*n+1)
        self.min = [float('inf')]*(4*n+1)
        self.arr = arr
        self.buildTree(0, 0, n-1, arr)
        
    def buildTree(self, i, start, end, arr):    
        if start > end:
            return -1
        
        if start == end:
            self.lo[i] = start
            self.hi[i] = end
            self.min[i] = start
            return self.min[i]
        
        mid = (start + end) // 2
        self.lo[i] = start
        self.hi[i] = end
        
        left = self.buildTree(i*2+1, start, mid, arr)
        right = self.buildTree(i*2+2, mid+1, end, arr)
        self.min[i] = left if self.arr[left] < self.arr[right] else right
        
        return self.min[i]
    
    def query(self, start, end):
        return self.__query__(0, start, end)
        
    def __query__(self, i, start, end):
        if start > end or self.lo[i] > end or self.hi[i] < start:
            return -1
        
        if self.lo[i] >= start and self.hi[i] <= end:
            return self.min[i]

        left = self.__query__(i*2+1, start, end)
        right = self.__query__(i*2+2, start, end)
        
        if left == -1: return right
        if right == -1: return left

        return left if self.arr[left] < self.arr[right] else right


if __name__ == '__main__':
    arr = [1, 7, 3, 2, 9]
    sgTree = SegmentTree(arr)
    
    assert(sgTree.query(0, 4) == 0)
    assert(sgTree.query(1, 4) == 3)
    assert(sgTree.query(2, 4) == 3)
    assert(sgTree.query(3, 4) == 3)
    assert(sgTree.query(4, 4) == 4)
    assert(sgTree.query(1, 2) == 2)
    assert(sgTree.query(3, 4) == 3)

    