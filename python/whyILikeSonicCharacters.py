import random
characterAndReason = [
	[
		'Sonic the Hedgehog',
		"he's really fast, blue and friendly."
	],
	[
		"Miles \"Tails\" Prower",
		'he is able to fly and without him Sonic would not be able to save the world without him.'
	],
	[
		'Knuckles the Echidna',
		'he is the guardian of Chaos Emeralds.'
	]
]

i = random.randint(0, (len(characterAndReason)-1))

print("My favorite character from Sonic franchise is " + str(characterAndReason[i][0]) +
	'.\nThe reason I like the character is because ' + str(characterAndReason[i][1]))