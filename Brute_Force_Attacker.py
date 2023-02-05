import random
usr = input()

pwd = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

pw = ""

while True:
	pw = ""
	for i in range(len(usr)):
		x = pwd[random.randint(0, 25)]
		pw += x
	print(pw)
	
	if pw == usr:
		break
	
print("Your Password : ", pw)