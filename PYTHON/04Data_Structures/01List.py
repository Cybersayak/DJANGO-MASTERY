l1 = [23 , 10 , 45 , 67 , 89 , 9]

l1.sort() # Sorts the list in ascending order

print(" l1 list: " , l1)

print(l1[0:2 ]) # Prints the first two element of the sorted list

print(l1[2:]) # Prints the last two elements of the sorted list

print(l1[-2:]) # Prints the last two elements of the sorted list

print(l1[2:5]) # Prints the elements from index 2 to 4 of the sorted list


l2 = [34 , 56 , 78 , 90 , 12 , 45]
l3 = [ 43 , 65 , 87 , 98 , 22 , 42]

print (l1 + l2) # Concatenates the two lists and prints the result without sorting
print(sorted(l1 + l2))# Sorts the concatenated list in ascending order

l4 = l1 + l2 + l3 # Concatenates the three lists and assigns the result to l3
print(l4) # Prints the concatenated list without sorting

l3.pop(2) # Removes the element at index 2 from l3
print(l3) # Prints the modified list l3



for i in l2:
    print ("Elements of l2 are  : " , i) # Prints each element of the list l2

l3.append(69) # Appends the value 69 to the end of the list l3
print(" Updated l3 list: " , l3) # Prints the modified list l3