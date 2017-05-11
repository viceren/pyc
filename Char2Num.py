from functools import reduce
def Fn(x, y):
	return x*10 +y
def Charm2NumTran(s):
	return	{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
r = reduce(Fn, map(Charm2NumTran,'123456789'))
print(r)
