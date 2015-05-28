poly = 0xedb88320
startxor = 0xffffffff

def ConstructCRC32ReverseTable():
	revtable = [0]*256
	for i in range(256):
		rev = i << 24
		for j in range(8):
			rev = [rev<<1, ((rev^poly)<<1) | 1][rev & 0x80000000 != 0]
		revtable[i] = rev & 0xffffffff
	return revtable

def ConstructCRC32Table():
	table = [0]*256
	for i in range(256):
		fwd = i
		for j in range(8):
			fwd = [fwd>>1, (fwd>>1)^poly][fwd & 1]
		table[i] = fwd & 0xffffffff
	return table

ft = ConstructCRC32Table()
bt = ConstructCRC32ReverseTable()

# we can only leak at most 4 bytes
def crc32leakNbyte(ss, bytenum):
	crc = ss ^ startxor
	for _ in range(bytenum):
		#print hex(crc)
		crc = ((crc << 8) ^ rt[crc >> 24]) & 0xffffffff
	return hex((~crc) & 0xffffffff)[2:].decode('hex')[::-1]

def crc32(ss):
	crc = startxor
	for c in ss:
		#print hex(crc)
		crc = (crc >> 8) ^ ft[(crc^ord(c)) & 0xff]
	return crc^0xffffffff

### test ###
'''
crc32leakNbyte(crc32('abcd'), 4) == 'abcd'

'''
