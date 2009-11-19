
from set import *

def part1(s):
    s.product (-0.95);
    s.sumofset (Set ([(-0,1, 0.1)]))
    return s

def part6 (s):
    s.square ()
    s.product (0.5)
    s.sumofset (Set ([(0, 0.1)]))
    return s

def func (s):
    return part1 (s)

def bfs (s, N, ff):
    Reach = s

    for k in range (N):
        ReachP = ff (Reach)
        ReachCopy = ReachP
        ReachCopy.diff (Reach)
        
        if (ReachCopy.empty ()):
            break

        Reach.union (ReachP)

    print Reach.i


bfs (Set([(1,2)]), 100, part1)
bfs (Set([(1.8, 1.9)]), 2, part6)
