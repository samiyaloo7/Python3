"""
    Python3: Datatypes
    - Every value in Python has a datatype.
    - Since everything is an object in Python programming.
    - data types are actually classes.
    - variables are instance (object) of these classes.
    - There are many dataypes in python some are listed below.
    Like,
        - Number
            - Integer
            - Float
            - Complex Numbers
            - Binary
            - Octal
            - Hexadecimal
        - Sequence
            - String
            - List
            - Tuple
        - Boolean
        - Mappting
            - Dictionarie
        - Set
        - None
    - ---
    - Note :
        - We can use the type() function to know which class a variable or a value belongs to.
"""
#%%


# --------- Numeric ---------
# - Integers can be of any length, it is only limited by the memory available.
# - A floating-point number is accurate up to 15 decimal places. 
# - floating-point is numbers after dot(.).
# - Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part
num = 123       # Integer / Decimal.
print("number : ", num)
flt = 1.2      # Float.
print("Float : ", flt)
complx = 1 + 7j     # python recognizes complex numbers.
print("Complex number : ", complx)
Binary = 0b010101
print("Binary : ", Binary)
Octal = 0o327
print("Octal : ", Octal)
Hex = 0x0fe
print("Hexadecimal : ", Hex)

#%%


# --------- Sequence ---------
# String ..
# - A string is a sequence of characters.(sequence of Unicode characters)
# - We can use single quotes or double quotes to represent strings.
# - Multi-line strings can be denoted using triple quotes, ''' or """.
# - Just like list we can use slicing operator [] with strings.
string = "Samiyal"      # we can use ',",''',""" for string.(but it is imutable)
print("\nstring : ",string)
print("\nspecific character of string : ", string[0])
print("\npart of the string only : ", string[:3])
# print("\nstring (negative indexing) ", string[-1::-1]) # prints reverse of string.
print("\nstring (negative indexing) ", string[3:-1])
# -String operationns-
# -changeing value..
# We can not change single character from string. We can reassign.
# string[0] = "s" # this will return an error.
# So we can reassign.
string = " Samiyalization "
# But there is method to change the part of the string.
string = string.replace(" ", "_")
print("\nstring after reassignment : ",string)
# -concatination.
string = " samiyal " + " yadav" # Using (+) we can concatinate the string.(like other sequence types)

# -checking charater is in string.
if("sam" in string) :
    print("sam is in ", string, "string")
else :
    # prints below line because sam and Sam is not same.
    print("sam is not in ", string, "string")
# -iterating through string.
for s in string :
    print("\ncharacters from string using loop : ", s)
    
# -delting/removing..
# we can not delete specific character from string. (but we can do so using replace method)
string = string.replace("_","")
print("\nstring after removing _ :", string)
# but we can delete whole string.
del string
# -String operationns-

#%%


# List ..
# - All the items (elements) inside square brackets [], separated by commas.
# - Can have any number of items and they may be of different types (integer, float, string etc.).
# - A list can also have another list as an item. This is called a nested list.
# - To check if item is in list, we can use statement: in <list>.
# - We can populate the list using for loop
#       - odd = [x for x in range(10) if x % 2 != 0]
lst1 = [ "Instagram", "Youtube", "LinkedIn" ]    # [] for list.
print("\nlist 1 : ", lst1)
lst2 = [ "samiyalo07", "samiyalization", "samiyal" ]    # [] for list.
print("\nlist 2 : ", lst2)
lst = [lst1, lst2, [ "test1", 2, 3 ]]
print("\nMegalist : ", lst)
print("\nMegalist[1,1](first value) : ", lst[0][0])
print("\nMegalist[1,1] : ", lst[1][1])
print("\nMegalist[1,1](nagative indexing/last value) : ", lst[-1][-1])
# print("\nMegalist[1,1] : ", lst1[1.1]) not valid.
# print("\nMegalist[1,1] : ", lst2[10]) not valid because there is no 10th index.
# -list operations-
# change value
lst[2][0]="test"
print("\nAfter changing lst item : ", lst)
# add value
lst2.append("sagar")
lst2.insert(0,"test")
print("\nAfter adding lst2 item : ", lst2)
# remove value
del lst[2][2]
lst[2].remove(2)
print("\nAfter removing element of lst : ", lst)
# list traversal
for x in lst1 : 
    print("\n list data from loop : ", x)
# Note - There are other methods like sort, pop, revers, clear, copy, count, extend, index.
# -list operations-


#%%


# Tuple .. (Ganerally used with same type of data)
# - Tuple is an ordered sequence of items same as a list.
# - The only difference is that tuples are immutable.(but it can be reassigned).
# - Items (elements) inside parentheses (), separated by commas.
# - A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).
# - Faster than lists as they cannot change dynamically.
# - Parentheses are optional, however, it is a good practice to use them.

# tpl = ("hello") # is not a tuple.
# To create tuple with one element, we have to do..
# tpl = ("hello",) # this will create a tuple with one element.

tpl = (1, 1.2, 3.14)    # 
# tpl = 1,2,3,4, # this is also valid.
# tpl = (1, 2, [3, 4, 5]) # is also a valid tuple.
# for above example we can change tpl[2][0] = "boom". because there is list at 2 index, and list is mutable.
print("\ntuple : ",tpl)
print("\npi : ",tpl[2])
print("\ntuple slicing[0:2] : ", tpl[0:2])
print("\ntuple(negative indexing)) : ", tpl[-2])
# Tuple packing nad uppacking..
test_tpl = 1, "samiyal", 7.7
print("\npacked tuple : ", test_tpl)
test_tpl = 1, "samiyal", 7 # tuple allows ressignment.
one, two, three = test_tpl
print("\nunpacked one : ", one)
print("\nunpacked two : ", two)
print("\nunpacked three : ", three)
# To combine or join two or more tuples we can use (+). tu repeat N number of times(<tuple>*N).
print("\nboth the tuples : ", tpl+test_tpl*2) 
# -Tuple operations-
# check element existance in tuple.
print("\n checking 7 is in test_tpl tuple", 7 in test_tpl)
# delete/remove the tuple using del key word.
del test_tpl
# triversing through the tuple.
for t in tpl :
    print("\n tpl value from loop: ", t)
# -Tuple operations-


#%%


# --------- Set ---------
# - Set is an unordered collection of unique items.
# - Set is defined by values separated by comma inside braces { }.
# - Set are unordered collection, indexing has no meaning. Hence, the slicing operator [] does not work.
set_ = { "samiyal", 7, 12, 1997  }   # kind of dictionary but without keys.
print(set_)
# print(set_[1]) this will return an error because set in imutable. we can replace but not edit it's value.
#%%


# --------- Dictionary ---------
# - Dictionary is an unordered collection of key-value pairs.
# - It is generally used when we have a huge amount of data.
# - Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.
# - dictionaries are defined within braces {} with each item being a pair in the form key:value. 
# - Key and value can be of any type.
# - We use key to retrieve the respective value.
dist = { "name": "samiyal", "b_day": 7, "b_month": 12, "b_year": 1997 }
print(dist)
print(dist["name"])
print(dist["b_day"])
#%%


# --------- Boolean ---------
bool = True
print(bool)
bool = False
print(bool)
bool += True    # 1 because bool is 0 (False) thast is why 0+1=1. 
print(str(bool))

# %%
# =========================== Type Conversion ==========================
# - We can convert between different data types by using different type conversion functions like int(), float(), str(), etc.
# - method :
#   - float()   # any to float, other then [-9-0-9] with floating point can not be converted to float.
#   - int()     # convert to int, other then [-9-0-9] can not be converted to integer.
#   - str()     # any to string.
#   - sequeance to another :
#       - set()     # list or tuple to set
#       - tuple()     # list or set to tuple 
#       - list()     # set or tuple to list
#   - dist([,],[,]..)    # to convert to dictionary, must give in to key value pair.

num_as_str = "123"
int_ = 12
float_ = 12.3

# origianal values.
print("\noriginal values ..")
print("\nnumber as string : ", num_as_str)
print("\ninteger : ", str(int_))   # converting integer to string in order to print it.
print("\nfloat : ", str(float_))   # converting float to string in order to print it.

# converted values.
print("\nconverted values ..")
print("\nstring to int : ", int(num_as_str))
print("\nstring to float : ", float(num_as_str))

# Collection conversion ..
# - one Sequence type can be converted to another sequence type like set-tuple, list-set, string-list.
print("\n set to tuple : ", tuple({1, 2, 3}))
print("\n list to set : ", set([1, 2, 3]))
print("\n stirng to list : ", list("hello"))
print("\n list to dictionary : ", dict([[1, 1], [2, 2], [3, 3]]))