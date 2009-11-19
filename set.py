class Set:

    i=[]  # list of touples

    MinVal = -10000000.0;
    MaxVal = +10000000.0;

    # constructor
    def __init__ (self, intervals):
        self.i = intervals

    def fix (self): 
        if (len (self.i) < 2): return 
        i = self.i
        i.sort()
        result = []
        cur = i[0]
        i = i [1:]

        while (len (i) > 0):
            if (cur [1] >= i[0][0]):
                cur = (cur[0], max(i[0][1], cur[1]))
            else:
                result.append (cur)
                cur = i[0]
            i = i[1:]

        result.append (cur)
        self.i = result

    def empty (self):
        i = self.i
        result = []
        cur = i[0]

        while(len(i) > 0):
            if (cur[0] != cur[1]):
                result.append (cur)
            i = i [1:]
            if (len(i) != 0):
                cur = i[0]
        self.i = result
        
    def union(self,b):
        self.i += b.i
        self.fix ()

    def complement (self):
        result = []
        i = self.i
        cur = i[0]
        curt = (Set.MinVal, cur[0])
        result.append (curt)
        k = cur [1]
        
        while (len(i) > 1):
            i= i[1:]
            cur = i[0]
            curt = (k, cur[0])
            result.append (curt)
            k = cur [1]

        curt = (k, Set.MaxVal)
        result.append (curt)
        self.i = result
        self.fix()
        
    def diff(self,b):
        self.complement ()
        self.union(b)
        self.complement ()
        self.empty()
                
    def checkempty (self):
        assert self.i == []        

    def subset (self,b):
        self.union (b)
        self.diff (b)
        self.checkempty ()

    def sumofset (self, b):
        result = []
        i=self.i
        cura = i[0];
        curb = b.i[0]

        for cura in i:
            for curb in b.i:
                temp = (cura[0]+curb[0], cura[1]+curb[1])
                result.append(temp)
            
        self.i = result
        self.fix() 

#Unit tests
def unit_test ():

    s = Set([(1, 3), (5, 9)])
    b = Set([(1, 2),(3,4)])
    s.sumofset (b)
    print s.i
    assert s.i == [(2,13)]

    s = Set([(1, 3), (5, 7)])
    b = Set([(1, 7)])
    s.subset (b)
    print s.i
    assert s.i == []

    ss = s = Set ([(1,2), (3,6)])
    s.complement()
    print s.i
    assert s.i == [(Set.MinVal,1),(2,3),(6,Set.MaxVal)]

    s.complement ()
    assert s == ss;

    s = Set([(1, 3), (5, 7),(9,14)])
    b = Set([(6, 7),(10,12)])
    s.diff (b)
    print s.i
    assert s.i == [(1,3),(5,6),(9,10),(12,14)]


    s = Set([(1, 3), (5, 9),(11,14)])
    b = Set([(6, 7),(8,9),(10,12)])
    s.diff (b)
    print s.i
    assert s.i == [(1,3),(5,6),(7,8),(12,14)]

    s = Set ([(1,2), (2,3), (4,5)])
    s.fix ()
    print s.i 
    assert s.i == [(1,3), (4,5)]

    s = Set ([(1,2), (2,3) , (3,4), (5,6), (6,7)])
    s.fix()
    print s.i
    assert s.i == [(1,4), (5,7)]

    s = Set ([(2,4), (1,5)])
    s.fix ()
    print s.i
    assert s.i == [(1,5)]
     
    s = Set([(1,5), (2, 5), (2,8)])
    s.fix ()
    print s.i
    assert s.i == [(1,8)]
    
    s = Set([(1, 3), (5, 7)])
    b = Set([(6, 7)])
    s.diff (b)
    print s.i
    assert s.i == [(1,3),(5,6)]


    s = Set([(1, 3), (5, 7)])
    b = Set([(1, 3), (5, 7)])
    s.diff (b)
    print s.i
    assert s.i == []

    s = Set([])
    s.checkempty ()
    print s.i
    assert s.i == []

    s = Set ([(1,4)]);
    b = Set ([(2,4)]);
    s.diff (b);
    print s.i
    assert s.i == [(1,2)]

    s = Set ([(1,5)])
    b = Set ([(1,2), (4,5)])
    s.diff (b)
    print s.i
    assert s.i == [(2,4)]
    s = Set ([(2,8),(9,10)])
    b = Set ([(1,3), (4,5), (6,7)])
    s.diff (b)
    print s.i
    assert s.i == [(3,4),(5,6),(7,8),(9,10)]

# this is temporary! so that you can call "pythong set.py" on the command
# line and the unit tests always get called.
unit_test ();
