'''
    Python3 - Literals
    - Literal is a raw data given in a variable or constant
    - <Variable Name> = <Literal>
    - Types of literals in python.
        - Numeric Literals
        - String Literals
        - Boolean Literals
        - Special Literals
        - Literals Collections.
'''
#%%
# - Numerical Literals.
#   - int, float, complex.

# Int Literals
# - all the hex, octal, binary are converted into decimal values.
a = 0b1010 #Binary Literals(0bXXX).
b = 100 #Decimal Literal.
c = 0o310 #Octal Literal(0oXXX).
d = 0x12c #Hexadecimal Literal(0xXXX).

# Float Literals
float_1 = 10.5 
# - 1.5f3 is expressed with exponential and is equivalent to 1.5 * 10 ^ 3.
float_2 = 1.5e3     

# Complex Literals 
# - imaginary literal (x.imag) and real literal (x.real) to create imaginary and real parts of complex numbers.
x = 7.77j

# output : 
print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)
#%%
# - String Literals.
# - A character lireral : a character literal is a single character surrounded by single or double quotes.
# - A string literal : is a sequence of characters surrounded by quotes.
# - We can use both single, double, or triple quotes for a string.

# - Examples :
string = "Samiyal"
character = "S"
# r"" for raw string.
raw_string = r" Samiyal /n Yadav "
# u"" for raw string.
unicode = u"\u00dc samiyal 😂"

print(string)
print(character)
print(raw_string)
print(unicode) 
# %%
# - Boolean Literals.
# - A Boolean literal can have any of the two values: True or False.

# Examples:
Codding = True
Boaring = False
# - we can use the True and False in numeric expressions as the value.
pluse_fun = Codding + 7

print("Codding is fun : ", Codding)
print("is it boaring : ", Boaring)
print("level : ", pluse_fun)

# %%
# - Special Lirerals.
# - Python contains one special literal i.e. None.
num_apple = None
print("how many apples you have : ", num_apple)
# %%
# - Literal Collections.
# - Four different literal collections List literals, Tuple literals, Dict literals, and Set literals.

lst = ["VS Code", "Atom", "PyCharm", "Android Studio"]      # list of advanced Editors/IDEs.
Dist = {"Python": "VS Code", "Android": "Android Studio", "JS": "Atom"}     # Dictionary..
set_of_langs = {"Python", "JAVA", "JS"}     #set of languages.
tpl = (1, 2, 3)     #tuple.

# output:
print("\n-> List of code editors and IDEs : ", lst)
print("\n-> Dictionary of laguage with it's preferd tool : ", Dist)
print("\n-> set of languages : ", set_of_langs)
print("\n-> Tuple example : ", tpl)

