class animal :

    def __init__(self,name ):
        print(name ," is a living being." )
    def setAge(self,age):
        self.age = age

dog = animal("choco")
print(dog.getName)