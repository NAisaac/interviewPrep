"""
Given two strings s and t, determine whether some anagram of t (i.e. some combination of letters in t) 
is a substring of s. For example: if s = "udacity" and t = "cadi", then the function returns True. 
Your function definition should look like: anagramCheck(s, t) and return a boolean True or False.
"""

import pdb

def stringToPrime(inputString):
	alphabetPrime = {
	"a":2,
	"b":3,
	"c":5,
	"d":7,
	"e":11,
	"f":13,
	"g":17,
	"h":19,
	"i":23,
	"j":29,
	"k":31,
	"l":37,
	"m":41,
	"n":43,
	"o":47,
	"p":53,
	"q":59,
	"r":61,
	"s":67,
	"t":71,
	"u":73,
	"v":79,
	"w":83,
	"x":89,
	"y":97,
	"z":101
	}
	if len(inputString) > 0:
		primeProduct = 1
		for i in inputString:
			primeProduct *= alphabetPrime[i] 
		return primeProduct
	else:
		return null

def anagramCheck(s,t):
	s_prime = stringToPrime(s)
	t_prime = stringToPrime(t)
	if s_prime and t_prime:
		if s_prime % t_prime == 0:
			print "True"
			return True
		else:
			print "False"
			return False
	else: 
		print "Make sure both input strings are non-empty"

a = "udacity"
b = "tciy"
c = "tcity"
anagramCheck(a,b)
anagramCheck(a,c)

