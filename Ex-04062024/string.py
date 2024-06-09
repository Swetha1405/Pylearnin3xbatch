name="harry"
name1='haerrynsns    ...............'
first_name="swetha"
last_name="avadanam"
print(first_name+ " "+last_name)
print(first_name ,last_name)

#raw string \n is taken for next line
dir=r'c:\nmd\fds'
print(name1,name)
print(dir)

#f - formatting the replace values of the variable
# {} placeholders
print(f'Your full name is {first_name} {last_name}')

num=2
print(f"{num}x1={num*1}")
print(f"{num}x2={num*2}")
print(f"{num}x3={num*3}")
print(f"{num}x4={num*4}")
print(f"{num}x5={num*5}")

name="swetha"
print(name)
print(type(name))
print(id(name))
print(len(name))
a=name.count("s")
print(a)
print(name[3]) #index value?

#none
#none
name= None
print(name)
name="Swetha"
print(type(name))
print(name)


#list
shopping_list=[1,2,3,4,5]
print(shopping_list)
print(shopping_list[0])
print(shopping_list[-1])
shopping_list.append(8)
print(shopping_list)
shopping_list.insert(5,9)

print(shopping_list)
shopping_list.extend([10,11])
print(shopping_list)
print(shopping_list.remove(5))
print(shopping_list)
print(shopping_list.pop())
shopping_list.sort()
shopping_list.reverse()
print(shopping_list)
my_list=[1,2,3,True,3.24,"Swetha"]
print(type(my_list))
shopping_list[0]='Swetha'
print(shopping_list)
