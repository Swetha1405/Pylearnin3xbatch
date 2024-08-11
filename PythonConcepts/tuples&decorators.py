#tuple-collection of items-immutable
t=tuple()
print(t)

#tuples used in apiurls
apiurl=tuple(['google.com','yaaho.com'])
print(apiurl)

#Conver list to tuple
t1=print(["sashi","swetha","sreevalli"])
print(t1)
#
hero1=("lakshmi","suma","kiram")
hero2=("sashi")
new_hero=(hero1,hero2)
print(new_hero)
print(new_hero[0]) #hero1
print(new_hero[1]) #hero2
print(new_hero[0][0],new_hero[0][1]) #hero1 0,1 element

#Covert tuple to list and then to tuple again
tuple1=(1,2,3)
#t.append()
print(tuple1)
my_list=list(tuple1)
print(my_list)
my_list.append(5)
tuple2= tuple(my_list)
print(tuple2)

