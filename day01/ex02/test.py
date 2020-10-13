import sys
from vector import Vector

def main():
	v1 = Vector(2)
	print(v1)
	v2 = Vector((3, 6))	
	print(v2)
	v3 = Vector([2, 3.0, "a", 4])
	v4 = Vector([2,3,4,5,19,23])
	print(v4)
	print(v1)
	v5 = v1 + v1
	print(v1, v5)
	v6 = v1 - v1
	print(v6)
	print(2 + 3)
	print(2 - 7)
	print(4 / 2)
	a = Vector([2,3,4])
	b = Vector([5,6,7])
	print(a,b)
	print(a*b)
	c = Vector(5)
	d = Vector(5)
	print(c*d)

if __name__ == "__main__":
	main()
