import random

class bucketArray:

	def __init__(self):
		self.size = 8
		self.sizeCount = 0
		self.buckets = self.size * [None]

	# modifies bucketArray to store KVP
	# xxx check that we aren't getting stuck in a full array
	def internal_store(self, KVP, index):
		self.sizeCount += 1
		if index >= self.size:
			index = 0
		if self.buckets[index]:
			self.internal_store(KVP, index+1)
		else:
			self.buckets[index] = KVP

	def internal_fetch(self, key, index):
		if self.buckets[index] == None:
			return None
		elif self.buckets[index][0] == key:
			return self.buckets[index]
		else:
			return self.internal_fetch(key, index+1)

	# xxx Add remove function
	def internal_remove(self, key, index):
		self.sizeCount -= 1

	def setSize(self):
		if self.sizeCount > self.size/2:
			self.buckets += self.size * [None]
			self.size = self.size * 2
		return self.size

	def printMe(self):
		print self.buckets



# take a KVP and returns an index and KVP 

def findIndex(key, size):
	random.seed(key)
	# xxx how large should i allow it to choose randInt>?
	hash_key = random.randint(1, 1e12)
	index = hash_key%size
	return index

# my class to interact with the user to make dictionary
class dict:

	def __init__(self):
		self.bucketArray = bucketArray()

	# self.KVP = KVP
	# self.size = bucketArray.setSize()
	# self.index = hasher.findIndex()

	def store(self, KVP):
		index = findIndex(KVP[0], self.bucketArray.setSize())
		self.bucketArray.internal_store(KVP, index)

	def fetch(self, key):
		index = findIndex(key, self.bucketArray.setSize())
		return self.bucketArray.internal_fetch(key, index)

	def printMe(self):
		print self.bucketArray.printMe()

	# def remove(KVP):
	# 	bucketArray.remove()



	
def main():

	test1 = dict()
	KVP1 = ('Hamilton', 'Margaret')
	test1.store(KVP1)


	# TESTS BELOW

	# test for fetch correctly finding input
	test_result = test1.fetch(KVP1[0])
	index = findIndex(KVP1[0], 8)
	if test_result[1] == 'Margaret':
		print "ok"
	else:
		print "input %t , expected 'Margaret'" %test_result

	# test for searching for wrong name at filled index
	test_result3 = test1.fetch('Jim')
	if test_result3 == None:
		print "ok"
	else:
		print "input %s , expected 'None'" %str(test_result3)

	# test for inserting something at an already filled spot with same key
	test_result4 = test1.store(('Hamilton', 'Rosalind'))
	test1.printMe()


if __name__ == '__main__':
	    main()
