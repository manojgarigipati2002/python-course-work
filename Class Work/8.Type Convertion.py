# Type Conversion Examples from Content

print("---- Converting from int ----")
int_a = 2
print(float(int_a))   # 2.0
print(str(int_a))     # '2'
print(bool(int_a))    # True
# list(int_a)        # Error
# set(int_a)         # Error
# tuple(int_a)       # Error
# dict(int_a)        # Error

print("\n---- Converting from float ----")
float_n = 3.1
print(int(float_n))   # 3
print(str(float_n))   # '3.1'
print(bool(float_n))  # True
# list(float_n)      # Error
# set(float_n)       # Error
# tuple(float_n)     # Error
# dict(float_n)      # Error

print("\n---- Converting from str ----")
string_c = 'power'
print(int('10'))      # 10
# print(int('10.9'))  # Error
# print(int(string_c)) # Error
print(float('10.8'))  # 10.8
print(bool(string_c)) # True
print(list(string_c)) # ['p', 'o', 'w', 'e', 'r']
print(tuple(string_c))# ('p', 'o', 'w', 'e', 'r')
print(set(string_c))  # {'p', 'o', 'w', 'e', 'r'}
# dict(string_c)     # Error

print("\n---- Converting from list ----")
list_d = [1, 2, 3, 4]
# int(list_d)        # Error
# float(list_d)      # Error
print(str(list_d))    # "[1, 2, 3, 4]"
print(bool(list_d))   # True
print(tuple(list_d))  # (1, 2, 3, 4)
print(set(list_d))    # {1, 2, 3, 4}
# dict(list_d)       # Error

print("\n---- Converting from tuple ----")
tuple_f = (1, 2, 3, 4)
# int(tuple_f)       # Error
# float(tuple_f)     # Error
print(str(tuple_f))   # "(1, 2, 3, 4)"
print(bool(tuple_f))  # True
print(list(tuple_f))  # [1, 2, 3, 4]
print(set(tuple_f))   # {1, 2, 3, 4}
# dict(tuple_f)      # Error

print("\n---- Converting from set ----")
set_e = {3, 4, 5, 6}
# int(set_e)         # Error
# float(set_e)       # Error
print(str(set_e))     # "{3, 4, 5, 6}"
print(bool(set_e))    # True
print(list(set_e))    # [3, 4, 5, 6]
print(tuple(set_e))   # (3, 4, 5, 6)
# dict(set_e)        # Error

print("\n---- Converting from dict ----")
dict_g = {1: 1, 2: 4, 3: 9}
# int(dict_g)        # Error
# float(dict_g)      # Error
print(str(dict_g))    # "{1: 1, 2: 4, 3: 9}"
print(bool(dict_g))   # True
print(list(dict_g))   # [1, 2, 3]
print(tuple(dict_g))  # (1, 2, 3)
print(set(dict_g))    # {1, 2, 3}

print("\n---- Converting from bool ----")
boolean = False
print(int(False))     # 0
print(int(True))      # 1
print(float(False))   # 0.0
print(float(True))    # 1.0
print(str(False))     # 'False'
# list(False)        # Error
# tuple(False)       # Error
# set(False)         # Error
# dict(False)        # Error

print("\n---- Converting list of tuples to dict ----")
d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
print(dict(d))        # {'name': 'teja', 'batch': '22', 'subject': 'python'}