'''range(stop) starting=0,step=1
range(start,stop) step=1
range(start,stop,step)

-----------------------------------------
for elements in sequence:
      print(elements)


'''
#for i in range(5):
    #print

#for i in range(1,6):
   # print(i)    


#for i in range(1,20,3):
    #print(i)  

#value=int(input('enter a value: '))

#for i in range(1,11,1):
    #print(value,'*',i,'=',value*i)

#s=input('given string is palindrome or not:')
#ev=''
#for i in range(len(s)-1,-1,-1):
 #      rev+=s[i]
#if s==rev:
 #      print(s,'is a palendrome')       
#else:
 #      print('not a palendrome')    
 # 
'''i=0
sum=0
while i<11:
    sum+=i
    i+=1
    print(sum)


sum=0
for i in range(1,11):
    sum+=i
    print(sum)

i=0

while i<6:
    j=1
    while j<i:
        print('*',end=' ')
        j+=1
    print('')
    i+=1

for i in range(1,6):
    for j in range(1,6):
       # 
        if j<=i:
            j-=1
            print('*',end=' ')
    print('')        
i+=1'''
# for i in range(0,10):
#     for j in range(0,50):
#           print(i+j)
# reverse a string
# name=int(input('enter a string'))
# rev = " "
# for i in name:
#     rev = i + rev
#     print(rev)
# print(rev)

# reverse a  number
number=int(input('enter a number'))
while number>0:
    res=number%10
    print(res,end='')
    number//=10

# number=tuple(map(int,input('enter a num').split()))
# rev =()
# for i in number:
#     rev=(i,)+rev
# print(rev)

# for i in range(1,6):
#     print(' '*(5-i),'* ' *i)


  