#alphabet = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
from random import randint
import sys
my_pass = []

#my_str = raw_input("Please enter something: ")
#print "you entered", my_str

#num = 0
#for num in range(0,len(my_str)):
	#print (ord(my_str[num]))
#print

def crypt(my_str):
	new_str = ""
	for num in range(0,len(my_str)):
		if (((ord(my_str[num]) >= 65) and (ord(my_str[num]) <= 122)) or (ord(my_str[num]) == 32)):
			#print("leter order:")
			#print (ord(my_str[num]))
		
			i = randint(65,122)
			#print("random int:")
			#print (i)
		
			#print("changing:")
			if (my_str[num] == ' '):
				i = 34
			my_pass.append(ord(my_str[num]))
			my_pass.append(i)
			list1 = list(my_str)
			list1[num] = chr(i)
			new_str += chr(i)
			my_str = ''.join(list1) 
			#print("changed:")
			#print my_str
			#print "The password is:"
			#print my_pass
	i = randint(1,20)
	#print i
	for num in range(0,len(my_pass)):
		my_pass[num] += i
		if (my_pass[num] > 122):
			my_pass[num] -= 58
	i += 65
	my_pass.append(i)
	#print my_pass
	for num in range(0,len(my_pass)):
		my_pass[num] = chr(my_pass[num])
	my_real_pass = ''.join(my_pass)
	#print my_real_pass
	return [new_str,my_real_pass]

def decrypt(my_str, my_pass):
	arr = []
	final_pass = []
	for num in range(0,len(my_pass)):
		arr.append(ord(my_pass[num]))
	#print arr
	i = arr[-1]-65
	arr.pop()
	#print arr
	for num in range(0,len(arr)):
		arr[num] = arr[num] - i
		if (arr[num] != 32):
			if (arr[num] < 65):
				arr[num] += 58
	#print arr
	for num in range(0,len(arr)):
		if (num % 2 == 0):
			final_pass.append(arr[num])
		else:
			if (len(my_str)*2 == len(arr)):
				if ((ord(my_str[num/2]) != arr[num]) and (my_str[num/2] != "\"")):
					print ("Wrong key!")
					sys.exit()
			else:
				print ("Wrong key!")
				sys.exit()
	for num in range(0,len(final_pass)):
		final_pass[num] = chr(final_pass[num])
	final_pass = ''.join(final_pass)
	print final_pass
	
print ("Welcome to David\'s crypting script  ")
print ("Type \"c\" for crypting or \"d\" for decrypting")
print
arg = raw_input()
my_str = ""
key1 = ""
key2 = ""

if (arg == "c"):
	my_str = raw_input("Please enter your text here: ")
	output = crypt(my_str)
	print "Your crypted text is:"
	print output[0]
	print "Your password is:"
	print output[1]
else:
	key1 = raw_input("Please enter your crypted text here : ")
	key2 = raw_input("Please enter your password here     : ")
	decrypt(key1, key2)
