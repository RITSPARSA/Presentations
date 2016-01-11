#!/usr/bin/env python

def ldDict(shift=0):
	"""
	Loads a caesar cipher dictionary based on the shift key entered.
	This example only takes lower case letters into account.
	By default, there is no shift.
	Returns a dictionary.
	"""
	letters = {} #create a dictionary
	for i in range(ord('a'),ord('z')+1): #For all letters a-z
		if (ord(chr(i+shift)) > ord('z')): #if shifted char is past 'z'
			letters[chr(i)] = chr((i+shift)-26) #rotate back to beginning
		elif (ord(chr(i+shift)) < ord('a')): #if shifted char is before 'a'
			letters[chr(i)] = chr((i+shift)+26) #rotate back to the end
		else: #if shifted char is between a and z
			letters[chr(i)] = chr(i+shift) #just save it
	return letters #return the dictionary

def translate(string,cdict):
	"""
	Translates a string based on the caesar dictionary loaded
	Keep the string in lower case letters - this example
	does not take upper case letters into account
	Returns a string.
	"""
	retstring = "" #create a return string
	for letter in string: #parse string char by char
		if letter in cdict: #if char in dict
			retstring += cdict[letter] #produce the shifted char
		else: #otherwise
			retstring += letter #just pass the char to the return string
	return retstring #return the string

def testCaesar():
	myDict = ldDict(4)
	plain = "hello, world!"
	cipher = translate(plain,myDict)
	print(plain)
	print(cipher)
	

if __name__ == "__main__":
	testCaesar()
