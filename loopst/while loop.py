# Sum of n natural numbers
'''n=int(input('enter number :'))
i=1
s=0
while i<=n:
   s+=i
   i+=1
   print(s)

   #even numbers from 1 to 10
#n=int(input('enter number :'))
i=0
while i<=100:
    if i%2==0:
       print(i,'is a even number')
    i+=1 
# find the factors of given numbers
n=int(input('enter number :'))
i=1
while i<=n:
    if n%i==0:
        print(i,'is the factors of ',n )
    i+=1   
# find the given num is prime number or not
n=int(input('enter number :'))
i=1
count=0
while i<=n:
    if n%1==0:
        count+=1
    i+=1 
if count==2:      
        print(n,'is a prime number', )
else:
        print(n,'is a not prime number', )

#fobbanoci
n=int(input('enter number :'))

i=1
a=0
b=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1 '''

#n=int(input('enter number :'))
i=1
while i<=101:
    count=0
    j=1
    while j<=i:
        if i%j==0:
          count+=1
        j+=1
    if count==2:
        print(i,'is a prime number') 
    i+=1           

name='divya'
vovels='aeiouAEIOU'
i=0
while i<len(name):
    if name[i] in vovels:
        print('*')
    else:
        print(name[i])
    i+=1        









