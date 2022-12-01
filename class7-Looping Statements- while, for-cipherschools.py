#a loop is a code with a condition which when satisfied runs a repetative code
# it ia also same as condition statement line should end with colon and next line should have indent
a=int(input())
while a<10:
    print(a)
    a+=1

#we use while loop when we don't know how many iterations it will take
b=int(input())
for i in range(0,b+1):
    print(b)

#break,continue  and pass

#what break does is stops the loop when the given condition is fulfilled
c=int(input())
for i in range(0,5):
    if i==3:
        break
    print(i)

#what continue does is stops the loop where the condition is fulfilled and continues the loop by leaving that conditioned object
d=int(input())
for i in range(0,5):
    if i==3:
        continue
    print(i)

#pass is an empty statement it passes on to the next statement