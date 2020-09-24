"""
    Python3: I/O and Import
"""
#%%

# -: Importing in python :-
# - A module is a file containing Python definitions and statements. 
# - Python modules have a filename and end with the extension .py.
# - We can import builtin module or custom module by import keyword.
# - Below are the import examples.

# 1.
# import whole module.
# import keyword
# import math
# print(keyword.kwlist)

# 2.
# import module and set a reference variable.
# import keyword as k
# print(k.kwlist)

# 3.
# import only needed definition or variable from a module.
# from keyword import kwlist
# print(kwlist)
# from math import sqrt, pi
# print("\n squareroot of (4) : ")
# print("\n ", sqrt(4))
# print("\n value of pi : ")
# print("\n ", pi)

# 4.
# importing multiple modules in oneline.
# import keyword, math 
# print("\n keywords : ")
# print("\n ", keyword.kwlist)
# print("\n math.pi : ")
# print("\n ", math.pi)

# or...
# import keyword as k, math as m
# print("\n kwlist : ", k.kwlist)
# print("\n pi : ", m.pi)

# %%
# -: Input & Output In Python :-
# - Generally functions like input() and print() are used for input and output.

# 1. output
# print() method is used.
# Syntext:
#   - print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False).
#   Where,
#       - *objects : is represents "str", var, or both.
#       - sep : separator of objects.(default '')
#       - end : is printed at the end of object/objects.(default '\n')
#       - file : specifies object where to show the output.(default sys.stdout)
#       - 
# We can also output data to a file using(>> in terminal) or file operations. 

# 1.1 printing out direct string.
# print("printing direct string using print.")

# 1.2 printing from variable.
# string_to_print = "string from the variable."
# print(string_to_print)

# 1.3 printing both string and variable value in one method.
# print("string -> ", string_to_print)

# 1.4 with all the parameters.
import sys
print("----")
print("samiyal","yadav", sep="_", end=" | ", file=sys.stdout, flush=False)
print("samiyal","yadav", sep="_", end="\n", file=sys.stdout, flush=False)
print("----")
# %%
