a = {3, 5, 6}
b = {2, 3, 4, 5}

print(min(a, b, key= lambda x: sorted(x)[0]))
print(min(b, a, key= lambda x: sorted(x)[0]))