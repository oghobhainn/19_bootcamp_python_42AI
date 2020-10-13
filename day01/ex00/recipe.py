import os
import sys

class Recipe:
	"""Classe building a recipe, defined by :

		-name
		-cooking_lvl
		-cooking_time
		-ingredients
		-description (optionnal)
		-recipe_type
		
		"""

	def __init__(self, name="default recipe_name"): #constructor
		
		self.name = name
		while 1:
			try:
				self.cooking_lvl = int(input("What's the level of difficulty (1 -> 5) ?\t"))
				if self.cooking_lvl > 0 and self.cooking_lvl < 6:
					break
				else:
					print("The difficulty has to be between 1 and 5")
			except ValueError:
				print("That's not a correct number. Try again.")
		while 1:
			try:
				self.cooking_time = int(input("How much time is needed for the preparation ?\t"))
				if self.cooking_time > 0:
					break
				else:
					print("Time can't have a negative value nor be zero...")
			except ValueError:
				print("That's not a correct number. Try again.")

		self.ingredients = []
		while 1:
			ing = input("What are the ingredients ? (one by one, type 0 when done)\t")
			
			if ing != '0' and ing != "":
				self.ingredients.append(ing)
			elif len(self.ingredients) != 0 and ing == '0':
				break
			else:
				print("We need to know the ingredients...")
		self.description = input("Add a little description of the recipe :\t")
		while 1:
			self.recipe_type = input("What kind of meal is it (starter / lunch / dessert) ?\t").lower()
			if self.recipe_type == "starter" or self.recipe_type == "lunch" or self.recipe_type == "dessert":
				break
			else:
				print("We need to know the kind of meal it is...")

	def __str__(self):
		
		"""Return the string to print with the recipe info"""
		
		txt = ""
		txt = "It's a '{}' made of {}. You'll need '{}' minutes to cook it, and the difficulty is '{}'.".format(self.name, self.ingredients, self.cooking_time, self.cooking_lvl)
		if self.description != "":
			txt += " Description : {}.".format(self.description)
		return txt
