#Author: Terry Su
#Purpose: some useful notes and tips






#THE ALL() & ANY() FUNCTION

#The all() function returns True if all items in an iterable are true, otherwise it returns False.
#If the iterable object is empty, the all() function also returns True.

#Params:
#the iterable

#Note: When used on a dictionary, the all() function checks if all the keys are true, not the values.

#Examples:
x = [1,2,0]
print(all(x))

#conditions can also be used where
#all(condition(item) for item in iterable)

print(all(element < 5 for element in x))

#The any() function returns True if at least one item in an iterable are true, otherwise it returns False.

print(any(x))
print(any(element == 0 for element in x))






#THE ZIP() FUNCTION

#The zip() function returns a zip object, which is an iterator of tuples where the items of each iterator passed for respective indexes are paired together
#assuming all iterators have a value at that index

#Params:
#the iterables to zip

#Examples:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
c = [1,2,3]

x = zip(a, b, c)
print(tuple(x)) #use the tuple() function to display a readable version of the result






#THE .GET() FUNCTION

#The get() method returns the value of the item with the specified key.
#get() method takes maximum of two parameters:

#Params:
#key - key to be searched in a dictionary
#value (optional) - Value to be returned if the key is NOT found, would return None if not specified

#Examples:
dic = {'a':'b'}
print(dic.get('a'))
print(dic.get('f'))
print(dic.get('sdsdsd','cant find'))






#THE .SPLIT() FUNCTION ***useful for CCC inputs

#The split() method splits a string into a list.
#You can specify the separator, default separator is any whitespace.

#Params:
#separator (optional) - Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit (optional) -  Specifies how many splits to do. Default value is -1, which is "all occurrences"

#Examples:
txt = 'i am terry'
print(txt.split())
print(txt.split(' ', 1))

