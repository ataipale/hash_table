import random
import timeit
from textwrap import dedent
import sys

class bucketArray:

	def __init__(self):
		self.size = 8
		self.sizeCount = 0
		self.buckets = self.size * [None]

	def internal_store(self, KVP, index):

		'''
		Internal method to modify the bucket array to store KVP
		'''

		if index >= self.size:
			index = 0

		if self.buckets[index] == None or self.buckets[index] == "Grave Stone" or self.buckets[index][0] == KVP[0]:
			self.sizeCount += 1
			self.buckets[index] = KVP
		else:
			self.internal_store(KVP, index+1)

	def internal_fetch(self, key, index):

		'''
		Method to return value stored at given key
		'''
		if index >= self.size:
			index = 0
		if self.buckets[index] == None:
			return None
		elif self.buckets[index][0] == key:
			return self.buckets[index][1]
		else:
			return self.internal_fetch(key, index+1)

	def internal_remove(self, key, index):

		'''
		If we find none at the insertion site or the following spaces
		return "key not found". Otherwise, replace the KVP with a 
		Grave Stone.

		'''
		if index >= self.size:
			index = 0
			
		if self.buckets[index] == None:
			print "Key Not Found"
		elif self.buckets[index][0] == key:
			print "Made Grave Stone"
			self.buckets[index] = "Grave Stone"
			self.sizeCount -= 1
		else:
			self.internal_remove(key, index+1)


	def setSize(self):

		'''
		Resize the bucket array to 4x original size when it gets 
		more than 2/3 full, to avoid time expensive collisions 
		'''

		if self.sizeCount > self.size*.66:
			self.buckets += (self.size*3) * [None]
			self.size = self.size * 4
		return self.size

	def printMe(self):
		print self.buckets


def findIndex(key, size):

	'''
	Take a KVP and returns an index to store the KVP in the bucket Array.
	I use a PRNG seeded on the key value as a hash function to return 
	a repeatable large hash number. Mod this PRNG number by the size 
	of the bucket array will give an index within the range of the bucketArray
	to insert the KVP into.
	'''

	random.seed(key)
	hash_key = random.randint(1, 1e32)
	index = hash_key%size
	return index

class myDict:

	'''
	My class to interact with the user to make dictionary
	'''

	def __init__(self):
		self.bucketArray = bucketArray()
		# self.size = self.bucketArray.setSize()

	def store(self, KVP):
		index = findIndex(KVP[0], self.bucketArray.setSize())
		self.bucketArray.internal_store(KVP, index)

	def fetch(self, key):
		index = findIndex(key, self.bucketArray.setSize())
		return self.bucketArray.internal_fetch(key, index)

	def remove(self, key):
		index = findIndex(key, self.bucketArray.setSize())
		self.bucketArray.internal_remove(key, index)

	def printMe(self):
		self.bucketArray.printMe()

def test(actual, expected, message):
	if actual == expected: print "ok      # %s" %message
	else: print "not ok # got %s, expected %s, (%s)" %(actual, expected, message)

def main():

	# TESTS BELOW
	test1 = myDict()

	# test large insertion
	list = [ (str(x), x) for x in range(1000) ]
	for key, value in list: test1.store((key, value))
	test(test1.bucketArray.sizeCount, 1000, "test sizeCount")
	test(test1.bucketArray.size > 1000.0/.66, True, "test size")

	
	# test for input and fetch function
	test1.store(('Hamilton', 'Margaret'))
	test(test1.fetch('Hamilton'), 'Margaret', "fetch inserted key")

	# test for searching for wrong name at filled index
	test(test1.fetch('Jim'), None, "fetch non-existant key")

	# test for inserting something at an already filled spot with same key
	test1.store(('Hamilton', 'Rosalind'))
	test(test1.fetch('Hamilton'), 'Rosalind', "rewrite key")

	# test removal 
	test1.remove('Hamilton')
	test(test1.fetch('Hamilton'), None, "delete key")


	print "TIME TESTS:"
	# Timing Tests 
	range_size=500
	count=500
	repeat = 3

	def print_results(t):
		print "Time for %s items stored in %s: " %(str(count), str(t))
		print t.timeit(number = count)
		print "Repeated %s times in %s: " %(str(repeat), str(t))
		print t.repeat(3, count)

	setup_statement=dedent('''
		from bucketArray import myDict;
		l = [ (str(x), x) for x in range(%d) ];
		d = myDict()''') % range_size
	setup_statement_machine='l = [ (str(x), x) for x in range(%d) ]; d = {}' % range_size

	# Test for inputting large number(1000) words

	my_timer = timeit.Timer("for s, i in l: d.store((s, i))",setup_statement)
	print_results(my_timer)
	machine_timer = timeit.Timer("for s, i in l: d[s] = i",setup_statement_machine)
	print_results(machine_timer)

	# Test for getting 1000 items

	my_timer = timeit.Timer("for s in l: d.fetch(s)",setup_statement)
	print_results(my_timer)
	machine_timer = timeit.Timer("for s in l: d.get(s)",setup_statement_machine)
	print_results(machine_timer)	

	# Test for removing 1000 items
	# xxx Still working on getting below method to work....
	'''
	machine_timer = timeit.Timer("for s in l: d.pop(s)",setup_statement_machine)
	print_results(machine_timer)	
	my_timer = timeit.Timer("for s in l: d.remove(s)",setup_statement)
	print_results(my_timer)
	'''

if __name__ == '__main__':
	main()

