import functools
int16 = functools.partial(int, base = 16)
Case = int16('10000000')
print(Case)