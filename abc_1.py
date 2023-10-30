# n = int(input("enter first number"))
# m = int(input("enter second number"))

# if n>m: 
#     print(n ," is greater ", m)
# else:
#     print( m, "is greater ", n)

# # x = int(input())

# sum of digit:
n=int(input("Enter Number:"))
temp=n
sum=0

while(temp!=0):
    rem=temp%10
    sum=sum+rem
    temp=temp//10
print("Sum of digit:",sum)

if sum==n:
    print("Palindrome")
else:
    print("Not Palindrome")
