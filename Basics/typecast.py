"""
    Python3: Type Conversion.
    - Conversion of object from one data type to another data type.( in python specifically)
    - Converting the value of one data type to another data type is called type conversion.
    - Two types :
        - Implicit 
        - Explicit
"""
#%%
# - Implicit :
# - Python automatically converts one data type to another data type. 
integer_ = 700                      # variable with integer value.
float_ = 0.007 + integer_           # integer automatically converted to float when adding to float value.
print("\n Float : ", float_)

integer_ = integer_ + float_        # adding float to integer also converts integer to float.
print("\n Integer : ", integer_)

# try_str = integer_ + "hello"      # addition of intger with string is not posible.
# print(try_str)                    # generates TypeError: addition of intger with string is not posible.  
# - thats why we have to use builtin methods of type convertion(Explicit type convertions).

# %%
# - Explicit :
# - We use the predefined functions like int(), float(), str(), etc.
# - Also known as typecasting.
# - Because in python every datatype is an class so we have to use any valid datatype with function brackets.
# - Like, <datatype>.(<data to be converted>).
# - We can see datatype of any variable with type() method.

num_as_string = "123"
print("Before converting : ", num_as_string, "'s datatype is ", type(num_as_string))
num_from_string = int(num_as_string)
print("After converting : ", num_from_string, " To ", type(num_from_string))
# Like above statement we can convert othe types to other types with valid input.
# - float(10)
# - tuple([1,2,3])
# - dict([[1, 2], [1, 2]])
# etc.

