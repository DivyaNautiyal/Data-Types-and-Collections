'''
Membership operators test for membership in a sequence (string, list, tuple, set and dictionary). You will learn about strings, sets, tuple etc in the upcoming chapters.

Operator: in
Description: Evaluates to true if it finds a variable in the specified sequence and false otherwise
Example: x in y, here in results in a 1 if x is a member of sequence y
 
 
Operator: not in
Description: Evaluates to true if it does not finds a variable in the specified sequence and false otherwise
Example: x not in y, here not in results in a 1 if x is not a member of sequence y '''



# given variable
name = "oreo"

# Code starts here
vanilla=name in ['Vanilla','Chocolate']
print(vanilla)



# check for memberships
oreo='Oreo' in ['Oreo','Dark Chocolate']
# Display variables
print(oreo)
