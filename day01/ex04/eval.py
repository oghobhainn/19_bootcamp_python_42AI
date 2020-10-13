import sys

class Evaluator:
	"""Learn about static functions (not related to objects, tied to a class"""

	@staticmethod
	def zip_evaluate(coefs, words):
		try:
			lenc = len(coefs)
			lenw = len(words)

			if lenc == lenw:
				results = 0
				for c, w in zip(coefs, words):
					results += c * len(w)
				return results
			else:
				return -1
							
		except:
			return -1


	@staticmethod
	def enumerate_evaluate(coefs,words):
		try:
			lenc = len(coefs)
			lenw = len(words)

			if lenc == lenw:
				results = 0
				for idx1, val1 in enumerate(coefs):
					for idx2, val2 in enumerate(words):
						if idx1 == idx2:
							results += val1 * len(val2)
				return results
			else:
				return -1

		except:
			return -1
