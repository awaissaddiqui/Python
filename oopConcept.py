# class Awais:
#      def __init__(self, age, id):
#           self.age = age
#           self.id = id
#      @classmethod #decorator
#      def zero(cls):
#          return cls(0,0)     
#      def __str__(self): # this is called magic method
#           return f"{self.age} , {self.id}"
     
#      def __eq__(self, other):
#           return self.age==other.age and self.id==other.id
           
#      def __gt__(self, other):
#           return self.age > other.age and self.id > other.id

#      def display(self):
#           print(f"Awais age is {self.age} and id is {self.id}")

# student=Awais(32,11)
# student2=Awais(42,31)
# print(student == student2)
# print(student > student2)
# print(student < student2)
 
# std = Awais.zero()
# print(std)
# std.display()

### Property : 
#              A property is an object that set infront of an attribute 
# and allow us to get and set the value of an attribute. 

                    # Inheritance
# isinstance()
# issubclass()

class Animal:

     def __init__(self):
          print("Animal Constructor")
          self.age = 2
     def eat(self):
          print("eat")

class Mammal(Animal):
     def __init__(self):
          print('Mammal Constructor')
          self.weight = 3
          super().__init__()
     def walk(self):
          print("Walk")
m = Mammal()
print(m.age)     
print(m.weight)     
