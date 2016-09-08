"""
A dictionary is a data structure that maps keys to values.
A hash table is a data structure that maps keys to values by taking the hash value of the key 
(by applying some hash function to it) and mapping that to a bucket where one or more values is stored.
The difference is that hashmap gets its key(hash) by applying hash function on the value, where as dictionary
may or may not have such key-value relationship.

Without using a dictionary, write a HashTable class that stores strings in a hash table, where keys are calculated
using the first two letters of the string

Hash Function: 

	Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 

function ord() to get the ASCII value of a letter, and chr() to get the letter associated with an ASCII value
"""

class HashTable(object):
	def __init__(self):
		self.table = [None]*10000

	def store(self, string):
		# Input a string that's stored in the table
		h_value = self.calculate_hash_value(string)
		if self.table[h_value]:
			self.table[h_value].append(string)
		else:
			self.table[h_value] = [string]

	def lookup(self, string):
		# Return the hash value if the string is already in the table. Return -1 otherwise
		h_value = self.calculate_hash_value(string)
		if self.table[h_value]:
			return h_value
		else:
			return -1

	def calculate_hash_value(self, string):
		# Helper function to calulate a hash value from a string
		h_value = ord(string[0]) * 100 + ord(string[1])
		return h_value
	
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
