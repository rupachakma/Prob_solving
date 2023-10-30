# n=int(input("Enter a Number:"))
# print("Your Number is",n)

# if n%2!=0:
#     print("Odd")
# else:
#     print("Even")


#another way(def):

# num=int(input("Enter how many item :"))
# newlist=[]

# for i in range(num):
#     i=int(input("Enter {} digit :".format(i)))
#     newlist.append(i)

# def even_odd(l):
#     evenlist=[]
#     oddlist=[]

#     for i in l:
#         if i % 2 == 0:
#          evenlist.append(i)

 
#         else:
#          oddlist.append(i)

#     print("Your even number is :",evenlist)
#     print("Your odd number :",oddlist)

# even_odd(newlist)



num=int(input("Enter how many item :"))
newlist=[]

for i in range(num):
    i=int(input("Enter {} digit :".format(i)))
    newlist.append(i)

evenlist=[]
oddlist=[]

for i in newlist:
    if i % 2 == 0:
       evenlist.append(i)

 
    else:
      oddlist.append(i)
print("Your even number is :",evenlist)
print("Your odd number :",oddlist)