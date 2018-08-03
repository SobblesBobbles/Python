# This file includes the classs definition of 'Person'.
# Params : Name, Age
# Functions: Init, setName, setAge, getAge, getName
class Person:
    name = ""
    age = 0

    def __init__ (self):
        name="undefined";
    def setName(self,n):
        self.name = n;

    def getName(self):
        return self.name;

    def setAge(self,a):
        self.age = a;
        
    def getAge(self):
        return self.age;
    
    def printSelf(self):
        print("Name : "+self.name);
        print("Age  : "+str(self.age));



# printList prints the list's objects by their attributes: name, age.
# params: L which is a List
def printList(L):
    for x in range (0,len(L)):
        print ("Name: "+L[x].getName());
        print ("Age : "+str(L[x].getAge()));
    return;



## object creation
p1 = Person();
p1.setName("Roger Waters");
p1.setAge(70);

p2 = Person();
p2.setName("David Gilmour");
p2.setAge(41);

p3 = Person();
p3.setName("Bick Bason");
p3.setAge(78);

p4 =Person();
p4.setName("Wichard Wright");
p4.setAge(61);

p5 = Person();
p5.setName("Syd Barret");
p5.setAge(81);


# creates a list and pushes the person objects onto it. 
L = list();

L.append(p1); L.append(p2); L.append(p3); L.append(p4); L.append(p5);


# sorting function of a list, it uses attribute 'age' to sort through the objects.
L.sort(key = lambda x: x.age);


print('**********Sorted by Age********');

## when passing to a function, we need to declare that L being passed is going to become L in the formal params of func. 
printList(L =L);

L.sort(key = lambda y :y.name);

print("*********Sorted by Name********");




printList(L =L);




