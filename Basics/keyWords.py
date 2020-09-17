#%%
'''
    Python3 - "Key words & identifiers.
    - Keywords are the reserved words in Python.
    - We cannot use a keyword as a variable name, function name or any other identifier.
    - keywords are case sensitive.
    - There are 33 keywords in Python 3.(specifically - 3.7 and it can be chaged as per the versions)
    - All the keywords are in lowercase except -True, False and None.
'''
# ------------------ Key Words ----------------
# we can see all the key words using python's builtin module keyword.
# we have to import it.
import keyword as k
# kwlist is the variable wich contains the list of all keywords.
print(k.kwlist)
# another usefull thing from keyword module is iskeyword() method.
# witch let's you check given arg is a keyword or not.
print(k.iskeyword("hello")) # returns False because hello is not a keyword.
print(k.iskeyword("False")) # returns True because False is not a keyword.
#%%

'''
    Python3 - Identifier.
    - An identifier is a name given to entities like class, functions, variables, etc. 
    - It helps to differentiate one entity from another.
    - Rules,
        - Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _. 
        - Names like myClass, var_1 and print_this_to_screen, all are valid example.
        - starts with string or (_).
        - never start with number but can contain number.
        - "Key Words" can not be used as variable name.
        - cannot use special symbols like !, @, #, $, % etc.
        - identifier can be of any length.
        etc.
    - and it is case-sansative.
'''
# a valid identifier.
name = "samiyal"
# - $name, @name, 7name, n@me are not valid.
# - name2, name2for, name_for are valid. 