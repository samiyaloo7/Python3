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
# ------------------ Strin Methods -------------
string = " samiyal "
# method :
#   - <string>.replace(<what to replace>, <to be replaced with>).
print(string.replace("s", "S"))
#   - <string>.split(<string/char from where list be splited>).
print(string.split("i"))
#   -split()
print(string.strip("i"))
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
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

# %%
