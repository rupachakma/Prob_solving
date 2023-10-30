# mylist=[]

# for i in range(2):
#     i = int(input("Enter {} Items:".format(i)))
#     mylist.append(i)
# print("Before Swapping:",mylist)

# if mylist[0] > mylist[1]:
#     temp=mylist[0]
#     mylist[0]=mylist[1]
#     mylist[1]=temp
# print("After Swapping:",mylist)


num=int(input("How Many Item:"))
list=[]

for i in range(num):
    i=int(input("Enter  {} Item".format(i)))
    list.append(i)

print("Before Sorting:",list)

for i in range(len(list)):
    for j in range(0,len(list)-1):
        if list[j]>list[j+1]:
         temp=list[j]
         list[j]=list[j+1]
         list[j+1]=temp
print("Afte sorting :",list)
