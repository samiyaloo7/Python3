
#%%
""" 
    Python3 :  'Statements'
    - Instructions that a Python interpreter can execute are called statements.
    - For example, a = 1 is an assignment statement. if statement, for statement, while statement, etc.
    - Slingle line statement : c = a + b
    - multiline statement : if statement, for statement, while statement, etc. 
"""
#  Singleline Statement -
print("this is a statement to be executed by interpreter.")

#%%
#  Muliline Statements -
# - In Python, the end of a statement is marked by a newline character. 
# - Explicit line continuation.
#   - But we can make a statement extend over multiple lines with the line continuation character (\)
name = "samiyal"\
    + " "\
    +"yadav" 

print(name)

#%%
# - implicit line continuation.
#   - line continuation is implied inside parentheses ( ), brackets [ ], and braces { }.
name = ("samiyal"
        +" "+
        "yadav")

print(name)

# or...
name = ["samiyal",
        " ",
        "yadav"]

print(name)

# or...
name = {
        "samiyal",
        " ",
        "yadav"
    }

print(name)

#%%
# And we can do reverse like multiple statements in one line..
# - using (;) samicolon.
fruit = "apple"; print(fruit)
# %%
""" 
    Python3 :  'Indentation'
    - Python uses indentation to define a block of code. 
    - A code block starts with indentation and ends with the first unindented line.
    - The amount of indentation is up to you, but it must be consistent throughout that block.
    - Generally, four whitespaces are used for indentation and are preferred over tabs.
    - ---
    - Note : Incorrect indentation will result in IndentationError.
"""
# Understanding indentation.....
def indentation_example() :
    # indeted to define code block ------- start of code block ---------
    print("inside the method's code block")
    # ------- end of code block ---------
    
# Indentation can be ignored in line continuation, 
if(True) : print("true") 
else : print("false")
# but it's always a good idea to indent.
if(False) :
    print("False")
else :
    print("true") 
    indentation_example()
# %%
"""
    Python3 :  'Comments'
    - hash (#) symbol to start writing a comment.
    - It extends up to the newline character.
    - Single-line and Multi-line comment.
"""
# This is a single line comment...

# This 
# is
# milti-line
# comment....

"""Triple quotes are used for muti-line comments..
    - Triple (') or...
    - Triple (") quotes can be used."""
#%%
""" 
    Python3 :  'Docstrings'
    - A docstring is short for documentation string.
    - string literals that appear right after the definition of a function, method, class, or module.
    - Triple quotes are used while writing docstrings.
    - The docstrings are associated with the object as their __doc__ attribute.
    - We can access the docstrings by __doc__ attribute.
"""
# Example :
def docstr_exmple() :
    """ this is docstring of docstring example"""

print(docstr_exmple.__doc__)
# %%
