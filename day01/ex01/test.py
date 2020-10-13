import sys
from game import GotCharacter, Stark

def main():
	arya = Stark("Arya")
	print(arya.__dict__)
	arya.print_house_words()
	print(arya.is_alive)
	arya.die()
	print(arya.is_alive)
	print(arya.__doc__)

if __name__ == "__main__":
	main()
