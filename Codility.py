import math

    # write your code in Python 2.7
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math
def solution(N):
    # write your code in Python 2.7
    B = []
    j = 1
    for i in set(str(N)):
        B.append(str(N).count(i))

    for i in B:
        if (i > 1):
            j *= math.factorial(i)

    return math.factorial(len(str(N))) / j

#print solution(1213)
#n = raw_input()
#a = map(int, raw_input().split())
#x = []
#s = set()
#f = 0
#for i, j in enumerate(a):
#    if j in s:
#        x.append([f+1, i+1])
#        s = set()
#        f = i+1
#    else:
#        s.add(j)
#print x
#print len(x)
#print "x = ", x[-1][0]

#if len(x) == 0:
#    print -1
#else:
#    x[-1][1] = len(a)
#    print len(x)
#    for i in x:
#        print i[0],i[1]
def calculator (a = 0, b = 9):
    a = str(list(range(a, b + 1)))
    return a.count('0')*6+a.count('1')*2+a.count('2')*5+a.count('3')*5+a.count('4')*4+ \
        a.count('5')*5+a.count('6')*6+a.count('7')*3+a.count('8')*7+a.count('9')*6








