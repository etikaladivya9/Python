# i=6
# while i>=0:
#     print('* ' *i)
#     i-=1


# for i in range (1,6):
#     for j in range(1,6):
#       if i>=j:
#        print('* ', end=" ")
     
#     print('')      

# for i in range (1,6):
#     for j in range(1,6):
#       if j>=i:
#        print('* ', end=" ")
#     print('')        

# for i in range(1,6):
#   for j  in range(1,6):
#     print("* " ,end= " ")
#   print('')  

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(" " * (5 - j) + "* " * j)
#     #  print(" ")   

# for i in range (1,6):
#     for j in range(1,6):
#       if i<=j:
#        print('* ', end=" ")
#     print('')       

# for i in range(65,71):
#    for j in range(65,71):
#       if i>=j:
#          print(chr(j),end=' ' )
#    print(' ')
# a=65
# for i in range(1, 6):
#     for j in range(i):
#         print(chr(a), end=" ")
#         a += 1
#     print()
  
# n = 5

# # Upper Pyramid
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)

# # Lower Pyramid
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)
# n = 5

# for i in range(n):
#     print(" " * (n - i - 1), end="")
#     for j in range(1, n + 1):
#         print(j, end=" ")
#     print()

# num=int(input('enter a number'))
# n=1
# for i in range(1,num+1):
#     n *=i
#     print(num,n)
# print(n)

# num = int(input("Enter a number: "))

# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")
   
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c= a + b
#     a = b
#     b = c   

# num = int(input("Enter a number: "))

# original = num
# reverse = 0
# length = len(str(num))
# for i in range(length):
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10

# if original == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")
    
# k=1
# for i in range(1, 6):
#     for j in range(i):
#         print(k, end=" ")
#         k += 1
#     print()
# n = 5

# # Upper Pyramid
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)
# print(" ")    

# n=int(input('enter a num'))
# for i in range(1,n):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,'is a prime number')

# print('-----------------------------------------')
# for i in range(1,101):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,'is a prime number')      



# text = "HAPPY"
# result = ""

# for ch in text:
#     if ch not in result:
#         result += ch

# print(result)


year=int(input('Enter the Year :'))
if year%100==0:
    if year%400==0:
        print(year,'is a leap year')
    else:
        print(year,'is not a leap year')
elif year%4==0:
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')        