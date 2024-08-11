# #range 0-99
for counter in range(1,100,3):
   print (counter)
   if counter==55:
    break

print("outside of the program")
#pass=skip
for i in range(1,10):
    if i==4 or i==5:
        pass
    else:
        print(i)
print ("printed")

#and and or
for i in range(1,10):
    if i%3==0:
        print(i)
    else:
        print(i*2)

#multiple conditions

browser= "chrome"
match browser:
    case "chrome":
        print("execute chrome broswer")
    case "firefox":
        print("execute firefox")
    case _:

        print("No idea")

#builtin function, defined functions
def allowed_to_attend(name,password):
    if name=="swetha":
        if password=="Yes":
         print("you are allowed")
        else:
            print("not allowed")

