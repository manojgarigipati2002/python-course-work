# Input Operations in Python

# --- Basic input examples ---
name = input("Enter the name: ")
print("Name:", name)

age = int(input("Enter the age: "))
print("Age:", age)

discount = float(input("Enter the discount: "))
print("Discount:", discount)

# --- Input a normal string ---
names = input("Enter names: ")
print("Names string:", names)

# --- Split input into list of strings ---
names = input("Enter names (space-separated): ").split()
print("List of names:", names)

# --- Convert input to list of integers ---
int_list = list(map(int, input("Enter numbers (int): ").split()))
print("Integer List:", int_list)

# --- Convert input to list of floats ---
float_list = list(map(float, input("Enter numbers (float): ").split()))
print("Float List:", float_list)

# --- Convert input to tuple of strings ---
tuple_str = tuple(input("Enter words: ").split())
print("Tuple of strings:", tuple_str)

# --- Convert input to tuple of integers ---
tuple_int = tuple(map(int, input("Enter tuple numbers (int): ").split()))
print("Tuple of integers:", tuple_int)

# --- Convert input to tuple of floats ---
tuple_float = tuple(map(float, input("Enter tuple numbers (float): ").split()))
print("Tuple of floats:", tuple_float)

# --- Convert input to set of integers ---
set_int = set(map(int, input("Enter set numbers (int): ").split()))
print("Integer Set:", set_int)

# --- Convert input to set of floats ---
set_float = set(map(float, input("Enter set numbers (float): ").split()))
print("Float Set:", set_float)

# --- Convert input to set of strings ---
set_str = set(input("Enter words for set: ").split())
print("String Set:", set_str)

# --- Using eval (works with dict, list, tuple etc.) ---
d = eval(input("Enter eval data (dict/list/tuple/string): "))
print("Eval Output:", d)

# --- Unpacking input ---
s = input("Enter name and email: ").split()
print("Unpacked:", s)

a, b = input("Enter two values: ").split()
print("a =", a)
print("b =", b)

# --- Unpacking into integers ---
a, b = list(map(int, input("Enter two integers: ").split()))
print("a =", a, "b =", b)

# --- Multiple assignment ---
a, b, c = 10, 20, 30
print("Multiple assignment:")
print("a =", a, "b =", b, "c =", c)

# --- Escape sequences ---
print("a =", a, "\nb =", b, "\nc =", c)
print("a =", a, "\tb =", b, "\tc =", c)

# --- Using sep ---
print("a=", a, "\tb=", b, "\tc=", c, sep="")

# --- Using f-strings ---
print(f"a={a}\nb={b}\nc={c}")
print(f"a={a}\tb={b}\tc={c}")

# --- Formatting with % operator ---
a = 10
b = 23.4
c = "string"

print("Using %% formatting:")
print("a=%d\nb=%f\nc=%s" % (a, b, c))
print("a=%d\nb=%.2f\nc=%s" % (a, b, c))

# --- Using format() ---
print("a={} \tb={} \tc={}".format(a, b, c))
print("a={2}\tb={1}\tc={0}".format(a, b, c))
