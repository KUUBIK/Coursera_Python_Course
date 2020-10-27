import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
discrim = b**2 - (4*a*c)
if discrim > 0:
    X1 = (-b + ((b**2 - 4*a*c))**0.5)/(2 * a)
    X2 = (-b - ((b**2 - 4*a*c))**0.5)/(2 * a)
    print(math.floor(X1))
    print(math.floor(X2))
elif discrim == 0:
    X3 = -(b/ (2 * a))
    print(X3)
else:
    print("число пжалста")
