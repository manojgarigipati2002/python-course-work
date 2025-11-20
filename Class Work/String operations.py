# String operations example for VS Code

# Empty strings
s = ''
s = ""
s = ''' '''
s = "' '"

# String concatenation
name = 'Ajay'
name1 = 'Krishna'
print(name + name1)
print(name + ' ' + name1)

# String repetition
print(name * 10)
print('*' * 100)
print('-' * 10)

# String indexing
name = 'Ajay Kumar'
print(name[3])
print(name[-2])
print(name[-5])
print(name[1])

# Slicing
names = 'AjayKrishnaSatishNishithaPreethiRuchitha'
print(names[0:4])
print(names[4:11])
print(names[11:17])
print(names[17:25])
print(names[25:32])
print(names[32:40])
print(names[::-1])

# Membership
print('Ajay' in names)
print('priya' in names)
print('sahithi' not in names)

# Case conversions
print(names.upper())
print(names.lower())
print(names.swapcase())

# Capitalization and title
l = 'python programming language'
print(l.capitalize())
print(l.title())

# Center, left, right justification
print(l.center(50, '*'))
print(l.ljust(50, '-'))
print(l.rjust(50, '-'))

# zfill examples
print('2'.zfill(6))
print('202'.zfill(6))
print('202123'.zfill(6))

# find and rfind
print(names.find('a'))
print(names.rfind('a'))
print(names.find('Ajay'))
print(names.find('z'))

# index example
print(names.index('K'))
print(names.index('a'))

# count
print(names.count('a'))
print(names.count('i'))

# replace examples
print(names.replace('a', '*'))
print(names.replace('sh', '00'))
print(names.replace('Ajay', 'Anirudh'))

# maketrans and translate
trans_table = str.maketrans('aeiou', '*****')
print(names.translate(trans_table))

trans_table2 = str.maketrans('AEIOUaeiou', '1234500000')
print(names.translate(trans_table2))
