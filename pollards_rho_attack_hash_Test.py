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
        while True:
            x = long(random.randint(0,curve.p-1))
            y_2 = x**3+x*curve.a+curve.b
            y = modular_sqrt(y_2,curve.p)
            if y!=0:
                break
        Q = Point(x,y,curve=curve)
        tStart = time.time()
        step=pollards_rho(Q)
        tEnd = time.time()
        thefile = open(file_name, 'a')
        thefile.write("%i\n" %step)
        thefile.close()


def pollards_rho(Q):
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
        #print 'count',count
        print 'l\n',l
        print 'Q\n',Q
        print 'l*P\n',l*P
        if (l*P==Q): return count
        else: return -1

def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.
        
        Solve the congruence of the form:
        x^2 = a (mod p)
        And returns x. Note that p - x is also a root.
        
        0 is returned is no square root exists for
        these a and p.
        
        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
        """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)
    #
    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1
    #
    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    #
    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #
    #
    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e
    #
    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)
        if m == 0:
            return x
            gs = pow(g, 2 ** (r - m - 1), p)
            g = (gs * gs) % p
            x = (x * gs) % p
            b = (b * g) % p
            r = m


def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)
        
        Returns 1 if a has a square root modulo
        p, -1 otherwise.
        """
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls

selected_curve = sys.argv[1]
times = int(sys.argv[2])
param(selected_curve)
file_name = 'direct_to_point_'+file_name
time_evaluate(times)








