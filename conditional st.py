'''
Docstring for conditional st

1.if condition:
2.if felse
3.else if lader
4.nested if
5.terinaary
6.math

'''
'''username='sai'
password='abc@11'

if username=='sai' and password=='abc@11':

    print('uservalid')
   
if condition:
        block of code(statement)
    else:
        block of code(statement)


bal=2000
    
if bal>0:
     print('draw the amount')  
else:
     print('bal is 0')     

else if condition: 
if condition:
     block
elif condition:  
    block
elif condition:       
   block  
else:
   block   

'''
'''travel='no'
if travel=='bus':
     print('by bus')
elif travel=='train' :  
    print('by train')
elif travel=='car':
   print('by car')
elif travel=='bike':
    print('by bike')
else:
    print('stop') '''   

'''user=input('enter user name:')   
if user=='divya' :
    print (user ,'you are welcome')
elif user=='hasi' :
    print (user ,'you are welcome') 
elif user=='abhi' :
    print (user ,'you are welcome')  
else:
    print (user ,'none') '''  
'''
nested if condition:
    if condition:
    
      if codition;
      print()
      else:
      print()
else:
print()

'''  

'''marks=int(input('enter your marks:'))

if marks>25:
    if marks>=80:
      next=marks+(marks*0.15)
      print(next,'these are your total markes')
    elif marks<=79 and marks>=51:
      next=marks+(marks*0.10)
      print(next,'these are your total markes')
    elif marks<=50 and marks>=30:
      next=(marks+marks*0.7)
      print(next,'these are your total markes')
    elif marks<=29 and marks>=26:   
      next=marks+(marks*0.2)
      print(next,'these are your total markes')
    else:
       print(marks,'these are your total markes')  
else:
    print('your are fail')'''

marks = int(input('enter your marks: '))

if marks > 25:
    if marks > 80:
        next = marks + (marks * 0.15)
        print(next,'these are your total markes')
    elif marks <= 79 and marks >= 51:
        next = marks + (marks * 0.10)
        print(next,'these are your total markes')
    elif marks <= 50 and marks >= 30:
        next = marks + (marks * 0.07)
        print(next,'these are your total markes')
    elif marks <= 29 and marks >= 26:
        next = marks + (marks * 0.02)
        print(next,'these are your total markes')
    else:
        print(marks,'these are your total markes')
else:
    print('you are fail')

