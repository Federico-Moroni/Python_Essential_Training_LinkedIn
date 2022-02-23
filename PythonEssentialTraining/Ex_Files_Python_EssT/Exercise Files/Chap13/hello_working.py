# x = (1, 2, 3, 4, 5)
# y = x
# print(x)
# print(y)

# REVERSED, SUM, ALL, MAX, MIN, ANY

# # y = reversed(x)
# # for i in y: # I can use this
# #     print(i)
# y = list(reversed(x)) # This is better
# print(y)
# print(sum(y)) # Sum of the list
# print(sum(y, 10)) # 10 will be the starting place
# print(max(y), min(y)) 
# print(any(y)) # If there is any True value then true. If not.. false.
# print(all(y)) # It will return True only if all of them are True

# ZIP

# x = (1,2,3,4,5)
# y = (6,7,8,9,10)
# z = zip(x, y) # zip returns an iterator with 2 values in each item
# for a, b in z: print(f'{a} - {b}')

#ENUMERATE

x = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(x): print(f'{i}: {v}')