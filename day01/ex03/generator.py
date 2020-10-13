import sys
import time

def swap(list, pos1, pos2):
	list[pos1], list[pos2] = list[pos2], list[pos1] 
	return list

def shuffle(list, size):
	
	for i in range(len(list)):
		if size <= 9:
			rn = 11
			while rn not in range(size - 1):
				rn = rng()
			swap(list, i, rn)
		else:
			rn = 0
			tmp = 0
			nbtimes = rng()
			while rn in range(size - 1) and nbtimes > 0:
				tmp = rn
				rn += rng()
				nbtimes -= 1
			swap(list, i, tmp)
	return list

def rng():
	ms = time.time()*1000.0
	return int(1000 * ms % 10)


def generator(text, sep=" ", option=None):
	"""Option is an optional arg, sep is mandatory"""

	if isinstance(text, str) == False or (option != "shuffle" and option != "unique" and option != "ordered" and option != "None"):
		print("ERROR")

	else:
		lsep = text.split(sep)
		size = len(lsep)
		if option == "shuffle":
			print("we shuffle the list !")
			shuffling_times = 1 + rng() * 10
			while shuffling_times > 0:
				lsep = shuffle(lsep, size)
				shuffling_times -= 1
			return lsep
			

		elif option == "unique":
			print("Here are only unique words!")
			mylist = []
			for word in lsep:
				if word not in mylist:
					mylist.append(word)
			return mylist


		elif option == "ordered":
			print("We sort the list!")
			lsep.sort()
			return lsep
