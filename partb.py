from pylab import *
from set import *

def part1(s):
    s.product (-0.95);
    s.sumofset (Set ([(-0,1, 0.1)]))
    return s

def part2(s):
    s.product (-0.96);
    s.sumofset (Set ([(-0,1, 0.1)]))
    return s

def part3(s):
    s.product (-0.95);
    s.sumofset (Set ([(-0,2, 0.2)]))
    return s

def part4 (s):
    s.square ()
    s.product (0.5)
    s.sumofset (Set ([(0, 0.1)]))
    return s

def part5 (s):
    s.product (0.9)
    s.sumofset (Set ([(-0.01, 0.01)]))
    return s

def func (s):
    return part1 (s)

def fixList (i):
	ret = [[], []]
	for (x,y) in i:
		ret[0].append (x)
		ret[1].append (y)
	return ret

def bfs (s, N, ff, filename):
    Reach = s

    for k in range (N):
        ReachP = ff (Reach)
        ReachCopy = ReachP
        ReachCopy.diff (Reach)
        
        if (ReachCopy.empty ()):
            break
        Reach.union (ReachP)

        plot((k,k), fixList (Reach.i), 'b')

    print Reach.i
    xlabel('k')
    ylabel('Reach')
    title(filename)
    savefig (filename + ".png")

bfs (Set([(1,2)]), 100, part1, "part1")
bfs (Set([(1,2)]), 100, part2, "part2")
bfs (Set([(1,2)]), 100, part3, "part3")
bfs (Set([(1.8, 1.89)]), 40, part4, "part4")
bfs (Set([(1.8, 1.9)]), 40, part4, "part5")
