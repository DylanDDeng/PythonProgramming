class Animal: 
    def __init__(self,animal): 
        self.animal = animal 

    def eat(self): 
        print('动物会吃') 

class Cat(Animal): 
    def __init__(self,animal,age): 
        super(Cat,self).__init__(animal) 
        self.age = age 
        print('猫不吃鱼',self.animal, self.age)

    def eat(self): 
        print('猫吃鱼') 

def fun(obj): 
    obj.eat()  

# Cat('cat','20')