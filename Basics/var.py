#%%
'''
    Python3 - Identifier.
    - A variable is a named location used to store data in the memory.
    - think of variables as a container that holds data that can be changed later in the program.
    - Python is a type-inferred language, so you don't have to explicitly define the variable type.
    - Applies All c++ variable declatation rules
    Like,
        - Variable name can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _. 
        - Names like myClass, var_1 and print_this_to_screen, all are valid example.
        - Can be starts with string or (_).
        - Never start with number but can contain number.
        - "Key Words" can not be used as variable name.
        - Cannot use special symbols like !, @, #, $, % etc.
        - can be of any length.
    - and it is case-sansative.
    - ---
    - Note : 
        - In Python, we don't actually assign values to the variables. 
        - Instead, Python gives the reference of the object(value) to the variable.
'''
#  --------------- Variable ------------
#  Declaration....
name = "samiyal"        # Initializing variable. using assignment operator(=).
#  Using or accessing vairable..
print(name)
name = "samiyal yadav"      # Changing the exiting value.
print(name)
# Assigning mutiple values to multipel variables at once.
name, gender, marks = "samiyal", "male", 77.77
print("Name : ", name, "\nGender : ", gender, "\nMarks : ", marks)
#%%
# ------- Variables : 'Constants' ------- 
# - A constant is a type of variable whose value cannot be changed.
# - Constants are written in all capital letters and underscores separating the words.
# - Naming them in all capital letters is a convention to separate them from variables, however, it does not actually prevent reassignment.
# - To prevent CONSTANTs from reassignment we have to create anotehr file containg all constats calld constant.py.
# Note:
#   - Rule for naming convention for constants are same as variables. but it must be in capital letters.

# Assume, constant.py
PI = 3.14
# as PI is in constant.py file we have to import it
# -> import constant
# and use is like,
# -> print(constant.PI) # in this case we can chage it constant.PI = 3.15.
# PI = 3.15     
print(PI)

# %%
