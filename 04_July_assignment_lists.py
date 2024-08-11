
"""
1.Write a program to add item 7000 after 6000 in the following Python List
Given:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#To insert outside the sublist
inner_list= list1[2]
inner_list.insert(3,7000)
print(inner_list)
print(list1)

#To insert inside the sublist

list2= [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
inner_sub_list=list2[2]
inner_most_sublist= inner_sub_list[2]
inner_most_sublist.append(7000)
print(inner_most_sublist)
print(list2)

"""
2.You have given a Python list. 
Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
Given:
list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output:
[5, 10, 15, 200, 25, 50, 20]
Show Hint
Use list method index(20) to get the index number of a 20
"""
question_2 = [5, 10, 15, 20, 25, 50, 20]
print(question_2.index(20))
question_2[3]= 200
print(question_2)

"""
You have given a nested list. 
Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
Given List:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]
Expected Output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
"""

question_3 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
inner_list=question_3[2]
second_inner_list = inner_list[1][2]
new_items=['h','i','j']
second_inner_list.extend(new_items)
print(second_inner_list)
print(question_3)

"""
4.
Write a program to add two lists index-wise.
 Create a new list that contains the 0th index item from both the list, 
 then the 1st index item, and so on till the last element. 
 any leftover items will get added at the end of the new list.
Given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Use the zip() function. 
This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.
"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
added_list=list(zip(list1,list2))
print(added_list)

"""
5.
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
Given:
tuple1 = (11, 22, 33, 44, 55, 66)
Expected output:
tuple2: (44, 55)
"""
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2= tuple1[3:5]
print(tuple2)