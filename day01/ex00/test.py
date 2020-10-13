import os
import sys

from book import Book
from recipe import Recipe

usage = """
	1. Add a recipe
	2. Get a recipe by its name
	3. Get the recipes by their types
	4. Quit
	"""

def	main():
	book = Book()
	while 1:
		i = input("What do you wanna do ?\t\t" + book.name + "\t Last Update: " + book.last_update + "\n" + usage)
		
		if i == "1":
			name_recipe = input("What recipe do you want to add ?\t")
			new_recipe = book.add_recipe(name_recipe)
			print(type(new_recipe))
			book.recipes_list[new_recipe.recipe_type][new_recipe] = new_recipe
		
		elif i == "2":
			print("We have these recipes : \n")
			
			for recipe_type, recipes in book.recipes_list.items():
				print("Recipe type:", recipe_type)
				for recipe in recipes:
					print("\t-" + str(recipe.name))
				print("\n")
			while 1:
				i = input("What recipe are you looking for ? (0 to go to menu)\t")
				if i == "0":
					break
				else:
					for recipe_type, recipes in book.recipes_list.items():
						for recipe in recipes:
							if i == recipe.name:
								print(recipe)
							else:
								print("We don't have that recipe...")
		elif i == "3":
			while 1:
				i = input("What is the type of the recette you're looking for ? (start/lunch/dessert)\t")
				if i == "starter" or i == "lunch" or i == "dessert":
					for item in book.recipes_list[i]:
						print("\n- " + str(item))
					print("\n")
					break
				else:
					print("We don't have any recipe of that kind")
		elif i == "4":
			print("Bye bye !")
			break

if __name__ == "__main__":
	main()
