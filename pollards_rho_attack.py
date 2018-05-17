from fastecdsa.curve import Curve
from fastecdsa.point import Point
import random
import time
import sys

##  sys.argv[1] for selected_curve : ex 32bits, 40 bits
##  sys.argv[2] for attact times,
##  record steps per attack in file sys.argv[1].txt
selected_curve = sys.argv[1]
times = sys.argv[2]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def partition(point):
    return point.x%n_of_set

curve32 = Curve(
    '32bits',  # (str): The name of the curve
    long(4000001039),  # (long): The value of p in the curve equation.
    long(1745322301),  # (long): The value of a in the curve equation.
    long(130575212), # (long): The value of b in the curve equation.
    long(3999907399), # (long): The order of the base point of the curve.
    long(2951351449), # (long): The x coordinate of the base point of the curve.
    long(2085375757), # (long): The y coordinate of the base point of the curve.
    #oid  # (str): The object identifier of the curve (optional).
)

curve36 = Curve(
    '36bits',  # (str): The name of the curve
    long(50000001637),  # (long): The value of p in the curve equation.
    long(10730991330),  # (long): The value of a in the curve equation.
    long(10461429567), # (long): The value of b in the curve equation.
    long(49999749391), # (long): The order of the base point of the curve.
    long(39948220728), # (long): The x coordinate of the base point of the curve.
    long(46724792678), # (long): The y coordinate of the base point of the curve.
    #oid  # (str): The object identifier of the curve (optional).
)

curve40 = Curve(
    '40bits',  # (str): The name of the curve
    long(1000000003571),  # (long): The value of p in the curve equation.
    long(120982395053),  # (long): The value of a in the curve equation.
    long(42757531213), # (long): The value of b in the curve equation.
    long(999998469709), # (long): The order of the base point of the curve.
    long(923179549631), # (long): The x coordinate of the base point of the curve.
    long(952583441553), # (long): The y coordinate of the base point of the curve.
    #oid  # (str): The object identifier of the curve (optional).
)

curve44 = Curve(
    '44bits',  # (str): The name of the curve
    long(9809862296159),  # (long): The value of p in the curve equation.
    long(2172373435844),  # (long): The value of a in the curve equation.
    long(864878753836), # (long): The value of b in the curve equation.
    long(9809858895373), # (long): The order of the base point of the curve.
    long(7573089241231), # (long): The x coordinate of the base point of the curve.
    long(4438676127758), # (long): The y coordinate of the base point of the curve.
    #oid  # (str): The object identifier of the curve (optional).
)

curve48 = Curve(
    '48bits',  # (str): The name of the curve
    long(210548486455921),  # (long): The value of p in the curve equation.
    long(18424416311620),  # (long): The value of a in the curve equation.
    long(2813146810101), # (long): The value of b in the curve equation.
    long(210548502757267), # (long): The order of the base point of the curve.
    long(91541889026188), # (long): The x coordinate of the base point of the curve.
    long(123287677451334), # (long): The y coordinate of the base point of the curve.
    #oid  # (str): The object identifier of the curve (optional).
)

curve52 = Curve(
    '52bits',  # (str): The name of the curve
    long(3093215881333057),  # (long): The value of p in the curve equation.
    long(1130104090562190),  # (long): The value of a in the curve equation.
    long(961750782982658), # (long): The value of b in the curve equation.
    long(3093215911838831), # (long): The order of the base point of the curve.
    long(2730087332105783), # (long): The x coordinate of the base point of the curve.
    long(2918974547317441), # (long): The y coordinate of the base point of the curve.
    #oid  # (str): The object identifier of the curve (optional).
)


curve56 = Curve(
    '56bits',  # (str): The name of the curve
    long(50544702849929377),  # (long): The value of p in the curve equation.
    long(17387714570041336),  # (long): The value of a in the curve equation.
    long(14158762040267516), # (long): The value of b in the curve equation.
    long(50544703140954961), # (long): The order of the base point of the curve.
    long(36182928645730553), # (long): The x coordinate of the base point of the curve.
    long(5540583353843909), # (long): The y coordinate of the base point of the curve.
    #oid  # (str): The object identifier of the curve (optional).
)

"""
###RESET FOR DIFFERENT CURVES
order=3999907399 ## ORDER OF ELLIPTIC CURVE
curve=curve32
P = Point(2951351449,2085375757,curve=curve)
file_name = '32bits.txt'
#####
"""

def param(selected_curve):
    global n_of_set
    global order
    global curve
    global P
    global file_name
    n_of_set = 16
    if selected_curve=='32bits':
        order=3999907399 ## ORDER OF ELLIPTIC CURVE
        curve=curve32
        P = Point(2951351449,2085375757,curve=curve)
        file_name = '32bits.txt'

    elif selected_curve=='36bits':
        order=49999749391 ## ORDER OF ELLIPTIC CURVE
        curve=curve36
        P = Point(39948220728,46724792678,curve=curve)
        file_name = '36bits.txt'

    elif selected_curve=='40bits':
        order=999998469709 ## ORDER OF ELLIPTIC CURVE
        curve=curve40
        P = Point(923179549631,952583441553,curve=curve)
        file_name = '40bits.txt'

    elif selected_curve=='44bits':
        order=9809858895373 ## ORDER OF ELLIPTIC CURVE
        curve=curve44
        P = Point(7573089241231,4438676127758,curve=curve)
        file_name = '44bits.txt'

    elif selected_curve=='48bits':
        order=210548502757267 ## ORDER OF ELLIPTIC CURVE
        curve=curve48
        P = Point(91541889026188,123287677451334,curve=curve)
        file_name = '48bits.txt'

    elif selected_curve=='52bits':
        order=3093215911838831 ## ORDER OF ELLIPTIC CURVE
        curve=curve52
        P = Point(2730087332105783,2918974547317441,curve=curve)
        file_name = '52bits.txt'

    elif selected_curve=='56bits':
        order=50544703140954961 ## ORDER OF ELLIPTIC CURVE
        curve=curve56
        P = Point(36182928645730553,5540583353843909,curve=curve)
        file_name = '56bits.txt'
    else:error

"""
time_list=[]
steps_list=[]
time_per_step=[]
for i in range(len(time_list)):
    time_per_step.append(time_list[i]/steps_list[i])
"""
def time_evaluate(times):
    for i in range(times):
        k = long(random.randint(0,order-1))
        Q = k*P
        tStart = time.time()
        step=pollards_rho(P,Q,k)
        tEnd = time.time()
        thefile = open(file_name, 'a')
        thefile.write("%i\n" %step)
        thefile.close()


def pollards_rho(P,Q,k):
    ## [ai,bi,Ri]
    sets = []
    for i in range(n_of_set):
        a=long(random.randint(0,order-1));
        b=long(random.randint(0,order-1));
        R=a*P+b*Q
        sets.append([a,b,R])
    c1 = long(random.randint(0,order-1));d1 = long(random.randint(0,order-1)); X1 = c1*P+d1*Q
    c2 = c1;d2 = d1; X2 = c2*P+d2*Q
    count=0
    while True:
        p = partition(X1)
        X1 = X1 + sets[p][2]; c1 = (c1+sets[p][0])%order; d1 = (d1+sets[p][1])%order;
        for i in range(2):
            p = partition(X2)
            X2 = X2 + sets[p][2]; c2 = (c2+sets[p][0])%order; d2 = (d2+sets[p][1])%order;
        count+=1
        if (count %100000 ==0):
            print(count)
    #   print('X1:',X1)
    #   print('X2:',X2)
        if (X1==X2): break;
    if (d1==d2):
        print('failure')
        return -1 # is pollards_rho(P,Q) ok?
    else:
        l = (c1-c2)%order*modinv((d2-d1)%order,order)%order
        print 'count',count
        print 'k:',k
        print 'l:',l
        if k!=l: return -1
        return count

selected_curve = sys.argv[1]
times = int(sys.argv[2])
param(selected_curve)
time_evaluate(times)

"""
t1 = [79,163,Point(135,117,curve=curve)]
t2 = [206,19,Point(96,97,curve=curve)]
t3 = [87,109,Point(84,62,curve=curve)]
t4 = [219,68,Point(72,134,curve=curve)]

t = [t1,t2,t3,t4]


c1 = random.randint(0,order-1);d1 = random.randint(0,order-1); X1 = c1*P+d1*Q
c2 = c1;d2 = d1; X2 = c2*P+d2*Q

count=0
while True:
    count+=1
    set = partition(X1)
    X1 = X1 + t[set][2]; c1 = (c1+t[set][0])%order; d1 = (d1+t[set][1])%order;
    for i in range(2):
        set = partition(X2)
        X2 = X2 + t[set][2]; c2 = (c2+t[set][0])%order; d2 = (d2+t[set][1])%order;
    print(count)
    print('X1:',X1)
    print('X2:',X2)
    if (d1==d2): print('failure')
    if (X1==X2): break;

if (d1==d2):
    print('failure')
else:
    l = (c1-c2)%order*modinv((d2-d1)%order,order)%order
    print(l)

l=0

"""









