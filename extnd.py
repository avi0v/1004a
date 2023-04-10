'''a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=['a','b','c','d','e','f','g','h']
print(a,' ',b)

#list1.extend(list2) or list2=[list itself]

a.extend(b)
print(a,' ',b)

a[1]=b
print(a)

a[1].extend(b)

print(a) '''

# empty list 

a=[]
a.extend(list('abcdefghi'))
print(a)