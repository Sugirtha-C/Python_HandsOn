#sets- unordered, unchangeable, unique , hetrogenous

my_set={11,15,17,21,25,28,27}
print(my_set)

my_set1=set((11,22,54,67,67,87))
print(my_set1)

number_list=[20,30,40,50,60]
my_set2=set(number_list)
print(my_set2)

my_set3={11,45,34,56,78}
for i in my_set3:
    print(i)
print(len(my_set3))

#adding elements
book_set={"Potter","Ice and Fire"}
#add
book_set.add("harry")
book_set.update(["geronimo","Grufalo"])
print(book_set)

#remove- will throw error if item is not present
book_set.remove('Potter')
#discard - will remove items which is ther/not there
book_set.discard('Ice and Fire')
book_set.discard('Rings')
#pop- random item will be removed
print(book_set)

#union of sets
a={1,2,3,4,5}
b={3,4,6,7,5}

#union:
c = a | b
print(c)
#intersection:
d= a & b
print(d)
#difference:
e= a - b
print(e)
f=b-a
print(f)
#symmeetric difference:
g= a ^ b
print(g)
g=b^a
print(g)