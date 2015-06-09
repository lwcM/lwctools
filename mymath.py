# by lwc

# Extended Euclidean algorithm 
# given (a, b), find (x, y) s.t. ax + by = gcd(a, b) = q

def ext_euclid(a, b):
    if(b == 0):
        return (1, 0, a)
    else:
        (x, y, q) = ext_euclid(b, a%b)
        (x, y) = (y, x-a/b*y)
        return (x, y, q)

# find modular multiplicative inverse
# given (a, n), find a^{-1} (mod n)

def mod_mul_inverse(a, n):
    return ext_euclid(a, n)[0]

