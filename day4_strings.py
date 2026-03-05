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


# MODIFY STRINGS
#Uppercase
case = "           This is a string I will be modifying             "
print(case.upper())

#lowercase
print(case.lower())

#Remove whitespaces
print(case.strip())

#Replace string
print(case.replace("is a", "is the new"))

#split - case sensitive, does not return the specified separator
print(case.split("s"))


#CONCATENATE STRINGS
z = "Hello"
y = "learner"
conc = z + " " + y
print(conc)



# Python Format Strings - f-strings
age = 26
txt = f"My name is Justin, I am {age} years old"
print(txt)

#Placeholders -variables, operations, functions and modifiers
#Variable
price = 300
txt = f"The price for a months' course is {price} Kenyatta Dollars"
print(txt)

#modifier - add a collon then legal formatting type
newprc = 2938
newtxt = f"The new price for the course is {newprc:.2f}" #.2f means fixed point num with 2 dp
print(newtxt)

#operators
newtxt = f"The offer price is {20 * 40} Dollars"
print(newtxt)


#self assessment
assess = "   hello, nAIrobi!   "
print(len(assess)) #prints the length of the string
print(assess.upper()) #returns the whole string in uppercase
print(assess.lower()) #returns the whole string in lowercase
print(assess.strip()) #Removes whitespaces
print(assess.strip().capitalize()) #Removes whitespaces and capitalizes the first letter of string
print(assess.replace("nAIrobi", "coders")) #replaces a word in the string with a given word
print(assess.split(",")) #splits the string into a list at the provided separator
print("nAIrobi" in assess) #Checks if a word is in the string, returns true or false
print(assess[2:9]) #slices the string at the provided indexes