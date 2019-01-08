'''
Created on 07 dic 2018

@author: mpasteri

'''

#https://www.python-course.eu/python3_object_oriented_programming.php
class Robot:
 
    def __init__(self, name=None):
        self.name = name   
        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")


#--------------------------------------------------------------
class A():
#---------------------------------------------------------------
# Class attributes: They will be shared by all the instances of the class.  
    colore="Giallo" 
#---------------------------------------------------------------
    __contami = 0    
    
    
#---------------------------------------------------------------    
#  name    Public  
#These attributes can be freely used inside or outside of a class definition.
#  _name    Protected
#Protected attributes should not be used outside of the class definition, unless inside of a subclass definition. 
# __name    Private
#This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.
#---------------------------------------------------------------    
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
        self.nome = "Pippo"
        type(self).__contami += 1

    
    def stampaQuesto(self):
        print(self._prot)

    def __stampaQuello(self):
        print('Questo non ve lo dico.')



#---------------------------------------------------------------
# Static method, is a method which we can call via the class name or via the instance name without the 
# necessity of passing a reference to an instance to it. 
#---------------------------------------------------------------
    @staticmethod
    def numDiIstanze():
        return A.__contami

#---------------------------------------------------------------
   
x = Robot()
x.say_hi()

y = Robot("Marvin")
y.say_hi()

#----------------------------------------------------------
a=A()
print(a.pub)
print(a.stampaQuesto())
print(a.colore)
print(a.nome)
print(a.numDiIstanze())


b=A()
b.nome = "Pluto"
print(b.colore)
print(b.nome)
print(b.numDiIstanze())
print(A.numDiIstanze())

print(b.__stampaQuello())




#----------------------------------------------------------




