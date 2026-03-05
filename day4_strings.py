# Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings as arrays
print(a[4])

# Looping through strings
name = "Justin"
for x in name:
    print(x)

# String Length
print(len(name))

#Check if in string
print("se" in a)
#Returns True
#Using if
if "sed" in a:
    print("Yes, word is present!")
# Prints the text

#Check if not
print('se' not in name)
#Prints True
#Using if NOT
if "se" not in name:
    print("Invalid search")
#Prints the text

#Testing understanding
test = "This is a random test"
if "os" not in test:
    print("Right Sir!")
else:
    print("Sorry, Sir!")



#SLICING STRINGS i.e. Choosing what to show
# Slicing from one index to another (final one not included)
str = "This is a string I am slicing"
print(str[4:10])
# prints from pos 4 to 10

# Slicing from the start
print(str[:4])

#Slicing to End
print(str[17:])

#Negative indexing
print(str[-17:-5])