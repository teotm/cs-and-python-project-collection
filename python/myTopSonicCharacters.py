characters = [
	"Knuckles",
	"Tails",
	"Mighty",
	"Robotnik",
	"Metal Sonic",
	"Sonic",
	"Ray"
]

print("My top " + str(len(characters)) + " Sonic characters")

for i in range(0, len(characters)):
	print(str(i+1) + ". " + str(characters[i]))