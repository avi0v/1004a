# sort 
# listname.sort() -default in accending or alphabetic like oxfprd dict
# listname.sort(reverse=True)  - desending 
#listname.sort(reverse=False)  - accending

a=list('aDUUDUQWFSBwqudvywqvdyuqvwd')
print(a)
'''['a', 'D', 'U', 'U', 'D', 'U', 'Q', 'W', 'F', 'S', 'B', 'w', 'q', 'u', 'd', 'v', 'y', 'w', 
'q', 'v', 'd', 'y', 'u', 'q', 'v', 'w', 'd']'''
a.sort()
print(a)

a.sort(reverse=True)
print(a)

print(a.count('w'))

print(a.index('w'))

