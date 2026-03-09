message = 'JuSTin\'s World'
print(message)

#How many characters in the sytring
print(len(message))

# To access a specific character
print(message[13])

#Slicing
#To access a range of characters from the start 
print(message[:6])

#To access a range of characters to the end
print(message[9:])

#To change case
print(message.lower())
print(message.upper())

#To count the number of characters in the string
print(message.count('s'))

#To find the index where certain characters are
print(message.find("World"))

#To replace characters in a string
print(message.replace('World', 'Kingdom'))

#Formatting strings
greeting = 'Hello'
name = 'Justin'
new_message = f'{greeting}, {name}. Welcome!'
print(new_message)