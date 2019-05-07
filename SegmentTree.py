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
            return float('inf')
        
        if start == end:
            self.lo[i] = start
            self.hi[i] = end
            self.min[i] = arr[start]
            return self.min[i]
        
        mid = (start + end) // 2
        
        leftMin = self.buildTree(i*2+1, start, mid, arr)
        rightMin = self.buildTree(i*2+2, mid+1, end, arr)
        
        self.lo[i] = start
        self.hi[i] = end
        self.min[i] = min(leftMin, rightMin)
        return self.min[i]
    
    def query(self, start, end):
        return self.__query__(0, start, end)
        
    def __query__(self, i, start, end):
        if start > end or self.lo[i] > end or self.hi[i] < start:
            return float('inf')
        
        if self.lo[i] >= start and self.hi[i] <= end:
            return self.min[i]
        
        return min(self.__query__(i*2+1, start, end), self.__query__(i*2+2, start, end))

if __name__ == '__main__':
    arr = [1, 7, 3, 2, 9]
    sgTree = SegmentTree(arr)
    
    assert(sgTree.query(0, 4) == 1)
    assert(sgTree.query(1, 4) == 2)
    assert(sgTree.query(2, 4) == 2)
    assert(sgTree.query(3, 4) == 2)
    assert(sgTree.query(4, 4) == 9)
    assert(sgTree.query(1, 2) == 3)
    assert(sgTree.query(3, 4) == 2)

    for N in range(10, 1023, 13):
        arr = range(0, N)
        sgTree = SegmentTree(arr)
        for i in range(1, N):
            assert(sgTree.query(0, i) == 0)
            assert(sgTree.query(i, N) == i)
            assert(sgTree.query(i, i+1) == i)
            assert(sgTree.query(N//2, N) == N//2)