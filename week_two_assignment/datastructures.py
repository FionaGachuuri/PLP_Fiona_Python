my_list = []
print("Before appending", my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending", my_list)

my_list.insert(1, 15)
print("After inserting", my_list)

other_list = [50,60,70]
my_list.extend(other_list)
print("After extending", my_list)

del(my_list[-1])
print("After deleting", my_list)

my_list.sort()
print("After sorting", my_list)

index_of_30 = my_list.index(30)
print("Index of 30", index_of_30)
