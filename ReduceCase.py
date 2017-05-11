from functools import reduce
def fn(x, y):
	return x*10 + y
r = reduce(fn, [0,1,2,3,4,5,6,7,8,9])
print(r)