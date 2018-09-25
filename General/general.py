from random import shuffle, randint

def getHash(length):
	hash_arr = []
	hash = ""

	for x in range(48, 58):
		hash_arr.append(chr(x))

	shuffle(hash_arr)

	for x in range(65, 91):
		hash_arr.append(chr(x))

	shuffle(hash_arr)

	for x in range(97, 122):
		hash_arr.append(chr(x))

	shuffle(hash_arr)

	for x in range(length):
		hash += str(hash_arr[randint(0, 60)])

	return hash