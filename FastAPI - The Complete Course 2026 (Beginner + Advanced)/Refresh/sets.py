my_set = {1,2 ,3 ,4 ,5 ,1 ,2}

print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

my_set.discard(3) # remove 3
print(my_set)
#my_set.clear() # clear all
#print(my_set)
my_set.update([7 ,8])#add some data
print(my_set)