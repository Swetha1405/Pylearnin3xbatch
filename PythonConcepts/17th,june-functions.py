def assign_name(name="swetha"):
    print("Hello", name)


assign_name()
assign_name(name="rani ")


# f1
def f1(a, b, c):
    return a - b - c


result=f1(3, 4, 5)
print(result)
print(f1(2,3,4 ))

#*args

def sum_four(a=1,b=2,c=5,d=10):
    return a+b+c+d

result=sum_four(1,2,3,4)
result1=sum_four(b=2,a=3,c=4,d=9)
result2=sum_four(2,3,5,6)
result3=sum_four()
print(result)
print(result1)
print(result2)
print(result3)

def arg_a(*args):
   for i in args:
       print(i,end="\n ")


arg_a("swetha","sai","sri")

#pizza toppings

def make_pizza(*toppings):
        for topin in toppings:
         print(topin,end="\n")

swetha=make_pizza("brocalli","onion","mushrooms")
sravya=make_pizza("paneer")





