# might finish it later
"# coding=utf-8"
import random

print("Do you like Pokémon?")
print("Well then, guess which Pokémon is this by its Pokédex entry!\n")

dexEntry = [
	"It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.", # Charizard
	"When walking on land, it covers its body with a poisonous film that keeps its skin from dehydrating.", # Wooper
	"It prefers arid environments. It leaks water from its eyes to adjust its body's fluid levels.", # Bonsly
	"This Pokémon is quick to anger, and it has no problem using its prodigious strength to get its way. It lives for duels against Obstagoon." # Pangoro
]

p = random.randint(0, (len(dexEntry)-1))

print(dexEntry[p] + "\n")