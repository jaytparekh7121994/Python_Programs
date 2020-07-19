sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

print(sq_list)
print(sq_iterator)

for items in sq_iterator:
    print(items)
