class Set:
    i=[]  # list of touples

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

    def diff(self,b):
        result = []
        i = self.i
        cura = i[0]
        curb = b.i[0]

        while ( len (i)):

            if (cura[0]>curb[1]):
                b.i = b.i[1:]
                if (len(b.i) > 0):
                    curb = b.i[0]    
                else:
                    result.append (cura)
                    i = i[1:]
                    if (len (i)>=1):
                        cura=i[0]

            if ((curb[0] > cura[0]) & (curb[1] < cura[1])):
                curat = (cura[0], curb[0])
                result.append (curat)
                cura = (curb[1],cura[1])
                result.append (cura)
                
                b.i = b.i[1:]
                if (len(b.i) > 0):
                    curb = b.i[0]    
                i = i[1:]
                if (len (i)>=1):
                        cura=i[0]
        
            else:
                if (cura[1]<curb[0]):
                    result.append (cura)
                
                if ((cura [1] >= curb[0])&(cura[0]<=curb[0])):
                    cura = (cura[0], curb[0])
                    result.append (cura)
                    
                if ((cura [0] <= curb[1])&(cura[1]>=curb[1])):
                    cura = (curb[1], cura[1])
                    result.append (cura)

                i = i[1:]
                if (len (i)>=1):
                        cura=i[0]
        self.i = result
        self.empty ()                
                
    def checkempty (self):
        assert self.i == []        

    def subset (self):
        print self.i
        print b.i
        self.union (b)
        print self.i
        self.diff (b)
        print self.i
        self.checkempty ()

#Unit tests
def unit_test ():
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

    s = Set([(1, 3), (5, 7),(9,14)])
    b = Set([(6, 7),(10,12)])
    s.diff (b)
    print s.i
    assert s.i == [(1,3),(5,6),(9,10),(12,14)]

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
#    s.i = [(1, 2), (6, 7)]
 #   b = Set ()
  #  b.i = [(1, 3), (5, 7)]
   # s.subset (b)
    #print s.i



# this is temporary! so that you can call "pythong set.py" on the command
# line and the unit tests always get called.
unit_test ();
