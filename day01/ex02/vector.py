import sys

class Vector:
	"""Class building a vector
	
		-list of values (float)
		-size (number of values)
		-r (range)
	
	"""
	
	def __init__(self, values=[]):
		
		if isinstance(values, list):
			try:
				self.values = [float(item) for item in values]
				self.size = len(self.values)
			except:
				print("ERROR")
		
		elif isinstance(values, int):
			try:
				self.values = [float(x) for x in range(values)]
				self.size = len(self.values)
			except:
				print("ERROR")

		elif isinstance(values, tuple):
			try:
				self.values = [float(x) for x in range(values[0], values[1])]
			except:
				print("ERROR")

		else:
			print("ERROR: constructor needs a list, a tuple or a range")
		

	def __str__(self):
		return str(self.values)

	def __repr__(self):
		return ("The values are " + str(self.values))

	def __add__(v1, v2):
		i = 0
		new_vector = Vector()
		if len(v1.values) == len(v2.values):
			while i < len(v1.values):
				new_vector.values.append(v1.values[i] + v2.values[i])
				i += 1
			return new_vector
		else:
			print("ERROR : vectors havent the same length")

	def __radd__(x, y):
		return x + y

	def __sub__(v1, v2):
		i = 0
		new_vector = Vector()
		if len(v1.values) == len(v2.values):
			while i < len(v1.values):
				new_vector.values.append(v1.values[i] - v2.values[i])
				i += 1
			return new_vector
		else:
			print("ERROR : vectors haven't the same length")
	
	def __rsub__(x, y):
		return x - y

	def __truediv__(self, other):
		if (isinstance(self, Vector) or isinstance(other, Vector)):
			print("ERROR: u can't divide vectors or by vectors")
		else:
			__rtruediv__(self,other)

	def __rtruediv__(self, other):
		try:
			ans = int(self) / int(other)
		except:
			print("There's been an ERROR")

	def __mul__(self, other):
		nv = Vector()
		"""Multiplying vector by a scalar"""
		if isinstance(self, Vector) and isinstance(other, int):
			for i in self.values:
				nv.values.append(self.values * other)
			return nv
		elif isinstance(self, Vector) and isinstance(other, Vector):
			if self.size == 3 and other.size == 3:
				nv.values.append(self.values[1]*other.values[2] - self.values[2]*other.values[1])
				nv.values.append(self.values[2]*other.values[0] - self.values[0]*other.values[2])
				nv.values.append(self.values[0]*other.values[1] - self.values[1]*other.values[0])
				return nv
			elif self.size == other.size:
				ans = 0
				for i, j in zip(self.values, other.values):
					ans += i * j
				return ans
			else:
				print("ERROR: the vectors haven't the same size")
			

	def __rmul__(self, other):
		return self * other


