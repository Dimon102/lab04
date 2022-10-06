from collections import Counter

array1 = ["Bob", "Alex", "Bob", "John"]
array2 = ["Bob",  "John"]
array3 = ["Richard",  "Johnson"]

c = Counter(array1)

for i in range(len(array1)):
    print("{0} овторяется в списке {1} {2} раз(а)".format(array1[i], array1, c[array1[i]]))