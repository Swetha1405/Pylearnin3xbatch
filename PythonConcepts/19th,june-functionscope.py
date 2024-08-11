# def outerfunction():
#     var=10;
#     def innerfunction():
#         print(var)
#
#     innerfunction()
#
#
# outerfunction()

#list
numbers=[1,2,3]

def list_one(swetha):
    swetha.append(4)
    swetha[1]=30
    return (swetha)

def list_two(sravya):
    sravya.append(10)
    sravya[1]=100
    return(sravya)

numbers.append(30)
l=list_one(numbers)
l2=list_two(numbers)
print(l)
print(l2)


