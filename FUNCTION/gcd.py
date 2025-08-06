# def gcd(a, b, c):
#     gcd = min(a, b, c)  # Use min for optimization
#     while gcd > 0:
#         if a % gcd == 0 and b % gcd == 0 and c % gcd == 0:
#             return gcd
#         gcd -= 1
#     

# print(gcd(10, 20, 30))  # Output: 10


# EFFICIENT VERSION

from math import gcd
from functools import reduce

def gcd_of_three(a, b, c):
    return reduce(gcd, (a, b, c))

print(gcd_of_three(10, 20, 30))  # Output: 10
