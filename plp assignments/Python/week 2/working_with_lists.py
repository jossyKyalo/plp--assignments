# creating an empty list
my_list=[]

#appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting an element at a specific position
my_list.insert(1, 15)

#extending the list with multiple elements
my_list.extend([50, 60, 70])

# removing the last element 
my_list.pop()

# sorting the list in ascending order
my_list.sort()

# finding the index of a specific element
index_thirty = my_list.index(30)

print("List after operations:", my_list)
print("Index of 30 in the list:", index_thirty)
