# list=[1,2,3,4,5,6,7,9]
# Search=3
# found=0  
# left,right=0,len(list)-1
# while(left<=right):
#     mid=(left+right)//2
#     if list[mid]==Search:
#         found=1
#         break
#     elif list[mid]<Search:
#         left=mid+1
#     else:
#         right=mid+1
# if found:
#     print("found")
# else:
#     print("not found")

n=int(input("enter items :"))
list=[]
for i in range(n):
    i=int(input("enter {} digit :".format(i)))
    list.append(i)
for i in range(len(list)):
    for j in range(0,len(list)-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("mylist is ",list)

search=4
found=0
left,right=0,len(list)-1
while(left<=right):
    mid=(left+right)//2
    if list[mid]==search:
        found=1
        break
    elif list[mid]<search:
        left=mid+1
    else:
        right=mid+1
if found:
    print("found")
else:
    print("not found")
