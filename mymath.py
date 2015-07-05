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


# baby-step giant-step algorithm
# given a^x = b (mod n), find x
def babyStep_giantStep(a, b, n):
	m = int(math.ceil(math.sqrt(n)))
	hh = {pow(a, j, n):j for j in range(m)}
	
	g_m_inv = mod_mul_inverse(pow(a, m, n), n)
	
	try_i = b
	for i in range(0, m):
		if try_i in hh:
			return i*m+hh[try_i]
		try_i = try_i * g_m_inv % n


