'''1.single inheritance

class parent:
    def __init__(self):
       pass 
    def display(self):
        print('parent class')
class Child(parent):
    def __init__(self):
        super().__init__()
    def show(self):
        print('cjild class')   
c=Child() 
c.display()
c.show()

2.Multiple Inheritance        

class Parent1:
    def __init__(self):
        pass
    def display(self):
        print('parent1 class')
class Parent2:
    def __init__(self):
        pass
    def show(self):
        print('parent2 class')
class Child(Parent1,Parent2):
    def __init__(self):
        super().__init__()
    def req(self):
        print('Thise is child class')   

c=Child()
c.display()  
c.show()
c.req()  

3.Multilevel Inheritance


class Parent:
    def __init__(self):
        pass
    def display(self):
        print('this is parent')
class Child(Parent):
    def __init__(self):
        super().__init__()
    def show(self):
        print('this is child class')
class grandchild(Child):
    def __init__(self):
        super().__init__()
    def req(self):
        print('this is grandchild class') 
c=grandchild()
c.display()
c.show()
c.req()

4.Hybrid Inheritance


class Parent1:
    def __init__(self):
        pass
    def display(self):
        print('thise is class parent1')
class Parent2(Parent1):
    def __init__(self):
        super(). __init__()
    def show(self):
        print('this is parent2')
class Parent3(Parent1):
    def __init__(self):
        super().__init__()
    def req(self):
        print('this is parent3')
class parent4(Parent3,Parent2):
    def __init__(self):
        super().__init__()
    def res(self):
        print('this is p4')                         

c=parent4()
c.display()
c.show()
c.req()
c.res()

5.Hierarchical Inheritance


'''
class Parent:
    def __init__(self):
        pass
    def display(self):
        print("This is Parent class")
class Child1(Parent):
    def __init__(self):
        super().__init__()
    def show(self):
        print("This is Child1 class")
class Child2(Parent):
    def __init__(self):
        super().__init__()
    def view(self):
        print("This is Child2 class")
c1 = Child1()
c2 = Child2()

c1.display()   
c1.show()      
c2.display()
c2.view()      