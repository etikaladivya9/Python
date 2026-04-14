class Sample:
    def __init__(self):
        self.name='Achiversit'
        self.age=22
    def display(self):
        print(f'{self.name},{self.age}')    
a=Sample()  
b=Sample()      
print(a.name)
print(a.age)
a.display()
print(b.name)
print(b.age)
b.display()


class One:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def req(self):
        print(f'{self.name}{self.age}') 
nameee=One('abc',22)
print(nameee.name)
print(nameee.age)
nameee.req()

