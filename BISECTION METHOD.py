# Bisection method----------------
import math
n = 4                                    # ROUND UPTO 4 DECIMAL PLACES 
pos = 0
neg = 0
x = 1
i = 1



for x in range(1, 10):

    # q=(x*math.log(x,10)) - 1.2
    # q=x*x*x - 9*x + 1
    # q = x - math.cos(x)
    q = x*x*x - 8
    if q >= 0:
        pos = round(x, n)                     # POSITIVE VALUE
        break

for x in range(1, 10):

    # q=(x*math.log(x,10)) - 1.2
    # q=x*x*x - 9*x + 1
    # q=x - math.cos(x)
    q = x*x*x - 8
    if q < 0:
        neg = round(x, n)                    # NEGATIVE VALUE
        break


game_over = True
while game_over:

    if pos <= neg:
        print('the root lies between', pos, 'and', neg,)
    else:
        print('the root lies between', neg, 'and', pos,)

    print(i, "approximation : ")
    x1 = round((pos+neg)/2, n)
    print("x", i, "=", x1)

    x = x1                                            # PUTTING THE VALUE OF X1 IN X

    # func= round((x*math.log(x,10)) - 1.2,4)
    # func=round(x*x*x - 9*x + 1,4)
    # func = round(x - math.cos(x),4)
    func = round(x*x*x - 8, n)

    print("f(x) = ", func)
    if func > 0:
        pos = round(x1, n)
    else:
        neg = round(x1, n)

    i += 1                                          # FOR NEXT APPROXIMATION
    # CHECKING FOR NEXT APPROXIMATION IF AS X2
    x2 = round((pos+neg)/2, n)
    if x1 == x2:
        print("Hence the root is", x2)
        game_over = False
