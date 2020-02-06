#built in sting functions
a="hello world"
n="HELLO"
b=a.capitalize()         #prints a string with each first char capital
print(b)          
print (a.capitalize())
print(a.upper())         #lower case is turned to upper case
print(n.lower())         #upper case is turned to lower case
print(a.count("hello"))  #Returns the number of times a specified value occurs in a string
print(a.endswith("d"))   #Returns true if the string ends with the specified value
print (a.encode())       #Returns an encoded version of the string
print(a.find("world"))   #Searches the string for a specified value and returns the position of where it was found
print(a.expandtabs(3))   #Sets the tab size of the string