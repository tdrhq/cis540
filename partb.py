
from set import *

def part1(s):
    s.product (-0.95);
    s.sumofset (Set ([(-0,1, 0.1)]))
    return s

def func (s):
    return part1 (s)

def bfs (s, N):
    Reach = s

    for k in range (N):
        ReachP = func (Reach)
        ReachCopy = ReachP
        ReachCopy.diff (Reach)
        
        if (ReachCopy.empty ()):
            break

        Reach = ReachP


    print Reach.i


bfs (Set([(1,2)]), 100)
