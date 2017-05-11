def FuncPro(x, y, f):
	return f(x) + f(y)
r = FuncPro(-5, 6, abs)
print(r)