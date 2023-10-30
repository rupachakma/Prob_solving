

def summation(l1):
    sum=0
    for i in l1:
        sum=sum+i
    print("summation is:",sum)

n= int(input("How Many Items!:"))
mylist=[]

for i in range(1,n+1):
    i=int(input("Enter {} Number Items:" .format(i)))
    mylist.append(i)

def searching(l1):
 
    search=int(input("Which Number do you want to find:"))
    Found=0
    for i in l1:
      if i == search:
        Found=Found+1
    if Found==0:
        print("Found")
    else:
        print("{} Number items Found {} times".format(search,Found))


print(mylist)
summation(mylist)
searching(mylist)


