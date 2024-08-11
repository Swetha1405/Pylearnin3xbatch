#double the list
my_list1=[1,2,3,4]
temp_list=[]
for i in my_list1:
    temp_list.append(i*2)


print(temp_list)

#using maps
#  1.take each item from the list
# 2.execute the function
# 3.return the same num of elements
my_list2=[1,2,5,4]
double_item=lambda num:num*2

double_list=list(map(double_item,my_list2)) #it willtake the inp and creates list to see the array
print(double_list)

