from generator import generator
from generator import swap
from generator import shuffle
from generator import rng
import sys

def main():
	
	print(generator("Gazam ad ad et nullam intervalla nulli honorem itidemque Caesaream et exaedificavit Neapolim Ascalonem sibi nitidis aemulas: Herodes ad est et principis abundans per exstructas abundans nitidis Gazam habens sed.", " ", "unique"))
		
	print(generator("Gazam ad ad et nullam intervalla nulli honorem itidemque Caesaream et exaedificavit Neapolim Ascalonem sibi nitidis aemulas: Herodes ad est et principis abundans per exstructas abundans nitidis Gazam habens sed.", " ", "ordered"))

	print(generator("Gazam ad ad et nullam intervalla nulli honorem itidemque Caesaream et exaedificavit Neapolim Ascalonem sibi nitidis aemulas: Herodes ad est et principis abundans per exstructas abundans nitidis Gazam habens sed.", " ", "shuffle"))

if __name__ == "__main__":
	main()
