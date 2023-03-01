"# coding=utf-8"

import random

drop = random.randint(1, 6) # You can change the numbers to whatever you want.
isEven = False

if drop % 2 == 0:
	isEven = True

print("Let's roll the dice, shall we?\nThe rules are simple:\nIf the number is odd, you lose.\n" +
	"If it's even, you win!")
print("The number in the dice, you've dropped is:" + str(drop))

if (isEven):
	print("It means that the number you got is even. You were lucky today for now, go outside or something")
else:
	print("What a misfortune for you. You've dropped an odd number. Prepare to die.")