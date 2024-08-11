#lambda usage to add num
def action(a,b,c):
    return a+b+c

l=action(3,5,9)
print(l)

l=lambda a,b,c:a+b+c
print(l(1,2,9))

#other usage of lambdA
l2=lambda num: "Even" if num%2==0 else "Odd"
print(l2(3))