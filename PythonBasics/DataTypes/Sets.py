# Creating a Set 
# Type 1 
s1 = set([1,2,3])
print(s1 ,": Type is", type(s1))

# type 2
s2 = {1, 2, 3, "Prathyush", (4,5,6), True}
print(s2, ": Type is", type(s2))

'''
we can't pass lists directly to set like this s3 = {[1,2,3]} we get and error 

TypeError: unhashable type: 'list' 
Since sets in Python cannot contain mutable types like lists. 
Sets only allow hashable (immutable) items, and lists are mutable.
'''
