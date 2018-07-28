class Person:
    __firstName="undefined";
    __secondName = "undefined "
    __age = 0;
    __address = "undefined"
    __county = "undefined location"
    __country = "undefined country"
    __sex = "undefined sex"
    __salary = 0;
    __department= "undefined department"
    __phoneNumber = 0;
    
   
    def __init__(self,firstName,secondName):
        self.__firstName = firstName;
        self.__secondName = secondName;


    def setAge(self,age):
        self.__age = age;
    def getAge(self):
        return self.__age;
    def setAddress(self,address):
        self.__address = address;
    def returnAddress(self):
        return self.__address;
    def setCounty(self,county):
        self.__county = county;
    def getCounty(self):
        return self.__county;
    def setCountry(self,country):
        self.__country = country;
    def getCountry():
        return self.__country;
    def setPhone(self,phoneNumber):
        self.__phoneNumber= phoneNumber;
    def getPhone(self):
        return self.__phoneNumber;
    def setSex(self,sex):
        self.__sex = sex;
    def getSex():
        return self.__sex;
    def setSalary(self,salary):
        self.__salary = salary;
    def getSalary():
        return self.__salary;
    def setDepartment(self, department):
        self.__department = department;
    def getDepartment():
        return self.__department;

    
    def printInformation(self):
        print("Name: "+self.__firstName);
        print("Last Name: "+self.__secondName);
        print("Age: "+str(self.__age));
        print("Address: "+self.__address);
        print("County: "+self.__county);
        print("Country: "+self.__country);
        print("Sex: "+self.__sex);
        print("Salary: "+ str(self.__salary));
        print("Department: "+self.__department);
        

p = Person("Stephen","O'Brien");
p.setAge(27);
p.setAddress("59 Mountain View, Naas");
p.setCounty("Kildare");
p.setCountry("IE- Ireland");
p.setSex("Male");
p.setSalary(50000);
p.setDepartment("IT Department");
p.printInformation()




