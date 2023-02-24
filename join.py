#!/usr/bin/python3
import unittest

def join(array, sep=''):

	if len(array) > 1:
		return str(array[0]) + sep + join(array[1:])
	return str(array[0])



class TestJoin(unittest.TestCase):

	def test_string_array(self):
		self.assertTrue(join(['I', 'am', 'a' , 'string', 'array']), "Iamastringarray")

	def test_string_array_with_separator(self):
		self.assertTrue(join(['I', "am", "number", "one"], " "), "I am  number one")

	def test_number_array(self): 
		self.assertTrue(join([1, 2, 3, 4, 5]), 15)

	def test_array_of_arrays(self):
		self.assertTrue(join([["I", "am", "a", "string", "array"], [1,2,3,4,5]]), ["I", "am", "a", "string", "array", 1, 2, 3, 4, 5])

if __name__ == '__main__':
	unittest.main()
