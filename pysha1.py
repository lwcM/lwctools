# my implementation of sha1
# 1. we can change the last 8 bytes of padding (msgbytes)
# 2. we can restore a state by a sha1 result (hex)
#    (it means we can run sha1 with our different initial constant)

import struct

mask = 0xffffffff

def rotate_left(x, n):
	return (x<<n | x>>(32-n)) & mask

def padding(msg, msgbytes=None):

	if msgbytes == None:
		msgbytes = len(msg)

	msglenbits = msgbytes * 8
	paddingLen = 512 - 64 - (msglenbits + 8) % 512
	return msg + '\x80' + '\x00' * (paddingLen / 8) + struct.pack('>q', msglenbits)

# imeplementaion referenced to wikipedia
def _mysha1(msg, msgbytes=None, state=None):

	#
	#set state
	#
	if state == None:
		h0, h1, h2, h3, h4 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
	elif len(state) != 40:
		return [0]*5
	else:
		h0, h1, h2, h3, h4 = [int(state[i:i+8], 16) for i in range(0, 40, 8)]
	
	#
	#padding
	#
	msg = padding(msg, msgbytes)

	for j in xrange(len(msg) / 64):
		chunk = msg[j*64: (j+1)*64]

		w = [0]*80
		for i in xrange(16):
			w[i] = struct.unpack('>i', chunk[i*4:(i+1)*4])[0]
		for i in xrange(16, 80):
			w[i] = rotate_left(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)

		a = h0
		b = h1
		c = h2
		d = h3
		e = h4

		for i in range(80):
			if 0 <= i <= 19:
				f = (b & c) | ((~b) & d)
				k = 0x5A827999
			elif 20 <= i <= 39:
				f = b ^ c ^ d
				k = 0x6ED9EBA1
			elif 40 <= i <= 59:
				f = (b & c) | (b & d) | (c & d) 
				k = 0x8F1BBCDC
			elif 60 <= i <= 79:
				f = b ^ c ^ d
				k = 0xCA62C1D6

			temp = (rotate_left(a, 5) + f + e + k + w[i]) & mask

			e = d
			d = c
			c = rotate_left(b, 30)
			b = a
			a = temp

		h0 = (h0 + a) & mask
		h1 = (h1 + b) & mask
		h2 = (h2 + c) & mask
		h3 = (h3 + d) & mask
		h4 = (h4 + e) & mask
	
	return [h0,h1,h2,h3,h4]

def mysha1(msg, msgbytes=None, state=None):
	return ''.join(map(lambda x:struct.pack('>I', x), _mysha1(msg, msgbytes, state)))

def hexmysha1(msg, msgbytes=None, state=None):
	return ''.join([hex(i)[2:] for i in _mysha1(msg, msgbytes, state)])
