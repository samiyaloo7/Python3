#%%
"""
    Python3: Strings & String Formating
    - String is a sequence of characters.
    - Various built-in functions that work with sequence work with strings as well.
    - Like,
        - len()
        - [](slicing).
        etc.
    
"""
# ------------------ String Methods -------------
string = " samiyal "
# method :
#   - <string>.replace(<what to replace>, <to be replaced with>).
print(string.replace("s", "S"))
#   - <string>.split(<string/char from where list be splited>).
print(string.split("i"))
#   -other comman string methods are
#       - lower() - changes to lowecase.
#       - upper() - changers to uppercase.
#       - split() - creates list of all the words in string.
#       - find()  - gives the index of first occurace of given string.
#       - format()  - used to formate string in defferent ways.
#       - capitalize(), count(), len(), index(), isalnum(), isnumeric(), isdigit(), isalfa(), isdecimal().
#       - and lots more()..
# %%
# ------------------ Strin Formating -------------
# Some string problems.
# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")

# Escape sequances
# \newline	Backslash and newline ignored
# \\	Backslash
# \'	Single quote
# \"	Double quote
# \a	ASCII Bell
# \b	ASCII Backspace
# \f	ASCII Formfeed
# \n	ASCII Linefeed
# \r	ASCII Carriage Return
# \t	ASCII Horizontal Tab
# \v	ASCII Vertical Tab
# \ooo	Character with octal value ooo
# \xHH	Character with hexadecimal value HH

# Exaples :
print("C:\\Python32\\Lib")
print("This is printed\nin two lines")
print("This is \x48\x45\x58 representation")

# Raw string to ignore escape sequance. (r or R at start of string)
print(r"This is \x48\x45\x58 representation(raw string)")

# Formating string using format() method.
# -Format strings contain curly braces {} as placeholders or replacement fields which get replaced.
# default(implicit) order
default_order = "{}, {} and {}".format('Sagar', 'Samiyal', 'Samiyalization')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('Sagar', 'Samiyal', 'Samiyalization')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{sml}, {sm} and {s}".format(s= 'Sagar', sm= 'Samiyal', sml= 'Samiyalization')
print('\n--- Keyword Order ---')
print(keyword_order)

#%%

# -= We can also format integers as binary, hexadecimal. =-
# - Integer ---------------
# - Integer to Binary representation.
print("\nBinary representation : {0:b} ".format(777))
# - Integer to octal representation.
print("\nOctal representation : {0:o} ".format(777))
# - Integer to Hex representation.
print("\nHexa representation : {0:x} ".format(777))

# - Float ---------------
# - like integer float can be represented in b, o, x...like above statements. 
# - in addition to it, it will be represented in to exponent.
# print("\nExponent of (1.2) is {0:e} ".format(1))  #- we can also do thar but it will take 1 as 1.0 .
print("\nExponent of (1.2) is {0:e} ".format(1.2))

# - We can control floating points numbers.
print("\nonly 3 digits after floating point {0:.3f}".format(7.7777777))

# - String alignment.
print("{:^15}".format("samiyal"))
print("{:<15}".format("samiyal"))
print("{:>15}".format("samiyal"))
print("|{0:<15}|{0:>15}|".format("samiyal"))

#%%
# -= Old Foramting Style =-
# - We can format string like old c language style using % operator.
x = 10
print("this is c style integer formating %d " %x)
print("this is c style integer formating %d " %101)
print("this is c style float formating %f " %101)
print("this is c style float formating %.3f " %101)

# -= Unicode(u"") string let you to pass unicode value to string. =-
# u"" for raw string.
unicode = u"\u00dc samiyal 😂"
# %%
