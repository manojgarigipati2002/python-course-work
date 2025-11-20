# List operations example for VS Code

# Creating lists
l = []
l = list()
l = [1, 2, 3, 4, 5, 6]
l = list([1, 2, 3, 4, 5])
print(l)

# Nested list
l = [[1, 2], [3, 4], [5, 6]]
print(l)

# Duplicate values
l = [1, 1, 1, 1, 1, 1, 2]
print(l)

# List concatenation and repetition
print([1, 2, 3] + [4, 5, 6])
print([1, 2] * 5)

# Membership
elements = ['ajay', 'krishna', 'shekar', 'santhosh', 'harsha', 'varun', 'shiva']
print(elements)
print(elements[2])
print(elements[-3])
print(elements[-2])
print(elements[-1])
print(elements[1:3])
print(elements[-1:-4:-1])
print(elements[::2])
print(elements[1::2])
print(elements[::-1])

# Nested list indexing
l = [[1, 2], [3, 4], [5, 6]]
print(l[0], l[1], l[2])
print(l[0][0], l[1][1], l[2][0])

# Modifying elements
l = [10, 20, 30, 40, 50]
print(id(l))
print(l)
l[1] = 20.3
l[2] = 30 + 4j
l[3] = 'string'
print(l)
print(id(l))

# append, extend, insert
l.append([1, 2, 3])
l.append((10, 202, 30))
l.append(70)
l.append(80)
print(l)
l.extend([100, 90, 20, 10])
print(l)
l.insert(0, 10)
l.insert(5, {1: 2, 2: 4, 3: 6, 4: 8})
l.insert(8, {1, 2, 3, 4})
print(l)

# remove
l.remove(10)
print(l)
l.remove((10, 202, 30))
l.remove({1, 2, 3, 4})
l.remove(100)
print(l)

# pop
print(l.pop(2))
print(l.pop(1))
print(l.pop(1))
print(l.pop())
print(l.pop())
print(l.pop())
print(l)

# del and clear
l = [10, 50, [1, 2, 3], 70]
del l[2]
print(l)
l.clear()
print(l)

# index and count
l = [10, 20, 30, 40, 50, 60, 70, 80]
print(l.index(30))
print(l.index(80))
l.append(10)
print(l.index(10))
print(l.count(10))

# sort and reverse
l.sort()
print(l)
l = [8, 2, 3, 4, 1, 8, 3, 4]
print(sorted(l))
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)

# aliasing vs copy
a = [1, 2, 3, 4, 5]
b = a
b.append(6)
print(a)
c = a.copy()
c.append(9)
print(a, c)

# max, min, len
l = [1, 2, 3, 3, 4, 4, 8, 8]
print(max(l), min(l), len(l))

# any, all tests
l = [0, 0.0, '', [], (), {}, set(), False]
print(any(l))
print(all(l))
l.append(1)
print(any(l))
print(all(l))
a = [1, 2, 3, 4, 5, 6]
print(all(a))
