import math
import operator as op

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

def Squidward():
    q = input()
    a = list(map(int, raw_input().split()))
    s = 0
    w = 0
    for i, j in zip(a, sorted(a)):
        s += j - i
        w += not s

    print w

def sorteddd():

    n, p, q, = map(int, raw_input().split())
    s = raw_input()
    a = []
    if (n == p+q):
        a.append(s[:p])
        a.append(s[p:])
    elif (n % min(p,q) == 0):
        m = min(p,q)
        while(s):
            a.append(s[:m])
            s = s[m:]
    else:
        big = max(p, q)
        small = min(p, q)
        while(s):
            if (len(s) < big and len(s) < small):
                print "-1"
                exit()
            if (len(s) % small == 0):
                a.append(s[:small])
                s = s[small:]
            else:
                if (len(s) < big):
                    print "-1"
                    exit()
                a.append(s[:big])
                s = s[big:]

    print len(a)
    for i in a:
        print i

def WSOE():
    n = input()
    r = map(int, raw_input().split())
    r.sort()

    print sum(r) if sum(r) % 2 == 0 else sum(r) - min(filter(lambda x:x&1, r) or [0])

def onelineTest():
    a = []
    for i in range(1,50):
        a.append(pow(i,3))

    print  reduce(lambda a,b: a+b, filter(lambda a: not(a&1), a)) - \
           reduce(lambda a,b: a+b, filter(lambda a: a&1, a)) \
           + 1





#for i, j in enumerate(r):
#    if sum(r[i:]) % 2 == 0:
#        print sum(r[i:])
#        exit()

#print "0"


#V1 = [1,2,3,4,5]
#V2 = [2,2,2,2,2]

#xx = map(op.mul, V1,V2)
#print xx

#print math.factorial(42) / (math.factorial(6)*math.factorial(36) )

#x = [tuple(map(int, raw_input().split())) for _ in range(input())]

#count = 0
#n = len(x)+1
#for i in range(len(x)):
#    n -= 1
#    for j in xrange(1, n):
#        count += 1 if abs(x[i][0] - x[i+j][0]) == abs(x[i][1] - x[i+j][1]) else 0

#print count

    #x[i][0] - x[i+1][0]
    #x[i][1] - x[i+1][1]

#for _ in range(n):
#    ai, bi = map(int, raw_input().split())
#    x.append((ai, bi))



#print x[0][0] - x[1][0]

#print x[0][1] - x[1][1]
#while (s):
#    print s


#print len(a)
#for i in a:
#    print i





