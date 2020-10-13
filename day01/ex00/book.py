import os
import sys
import datetime
from recipe import Recipe

class Book:
	"""Class of books

	self.name
	self.creation_date
	self.last_update
	self.recipes_list
	
	"""
	def __init__(self):

		while 1:
			self.name = input("What's the name of the book ?\t")
			if self.name != "":
				break
			else:
				print("The book has to have a name")

		now = datetime.date.today()	
		self.creation_date = now.strftime("%d/%m/%Y")

		self.last_update = self.creation_date
		self.recipes_list = {"starter" : {}, "lunch" : {}, "dessert" : {}}

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		print(self.name)
		pass
	
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type"""

		pass

	def add_recipe(self, name):
		"""Add a recipe to the book and update last_update"""
		self.last_update = datetime.date.today().strftime("%d/%m/%Y")
		recipe = Recipe(name)
		return recipe
