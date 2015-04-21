import random

class bucketArray:

	def __init__(self, size):
		self.size = size
		# self.sizeCount = 0
		# self.size = 8
		# if self.sizeCount > size/2 :
		# 	self.size = 
		self.buckets = size * [None]

	# modifies bucketArray to store KVP
	# xxx check that we aren't getting stuck in a full array
	def store(self, KVP, index):
		self.sizeCount += 1
		if index >= self.size:
			index = 0
		if self.buckets[index]:
			self.store(KVP, index+1)
		else:
			self.buckets[index] = KVP

	def fetch(self, key, index):
		if self.buckets[index] == None:
			return None
		elif self.buckets[index][0] == key:
			return self.buckets[index]
		else:
			return self.fetch(key, index+1)

	# xxx Add remove function
	# def remove:
	# 	self.sizeCount -= 1

	# def setSize:



# take a KVP and returns an index and KVP 
# should also set the size of the table?
# class hasher:

# 	def __init__(self, KVP):
# 		self.KVP = KVP

# 	def findIndex():
# 		random.seed(KVP[0])
# 		hash_key = random.random()
# 		hash_key
# 		return index

# 	def setSize():
# 		size = 8
# 		if size 
# 		return size



	
def main():

	test1 = bucketArray(8)
	test1.store(('Hamilton', 'Margaret'), 0)




	# TESTS BELOW

	# test for fetch correctly finding input
	test_result = test1.fetch('Hamilton', 0)
	if test_result[1] == 'Margaret':
		print "ok"
	else:
		print "input %s , expected 'Margaret'" %str(test_result)

	# test for seraching for input in wrong bucket
	test_result2 = test1.fetch('Hamilton', 2)
	if test_result2 == None:
		print "ok"
	else:
		print "input %s , expected 'None'" %str(test_result2)

	# test for searching for wrong name at filled index
	test_result3 = test1.fetch('Jim', 0)
	if test_result3 == None:
		print "ok"
	else:
		print "input %s , expected 'None'" %str(test_result3)

	# test for inserting something at an already filled spot
	test_result4 = test1.store(('Franklin', 'Rosalind'), 0)
	if test1.buckets[1][0] == 'Franklin':
		print "ok"
	else:
		print "input %s , expected 'Franklin'" %str(test_result4)

	# test for inserting at out of bounds
	test_result5 = test1.store(('Kwan', 'Michelle'), 15)
	if test1.buckets[2][0] == 'Kwan':
		print "ok"
	else:
		print "input %s , expected 'Kwan'" %str(test_result5)
	

	


if __name__ == '__main__':
	    main()
