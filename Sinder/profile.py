## testing json formats in python.
## have the json format inputting the data but need to figure out the appending scenario.

class Profile :
    name= "undefined name"
    age =18;
    bio = "undefined bio"
    image = "undefined image";
    password = "undefined password";

import json



p = Profile();

p.name = raw_input("Enter name :");
p.password = raw_input("Enter password : ");
p.bio = "Hey there. My name is Stephen.";
p.image = "https://www.github.com/SobblesBobbles/Python";



i = 1;
data = {};
data['user'+str(i)] = {
    'name' : p.name,
    'password' :p.password
    }
i=i+1;
data['user'+str(i)] = {
    'name':"testName",
    'password' :"TestPassword"
    }



filename = 'database.json';
file= open(filename,'a');

send = json.dumps(data)

file.write(send);
file.close();







##with open('database.json','a') as data1:
####    information = {'user'+str(i):{'name':p.name,'password': p.password}};
##    i=i+1;
##    dataRead = dataRead+information;
##    dataRead.write(json.dumps(dataRead))
##    data1.close()



##with open('database.json','w') as writeFile:
##    json.dump(dataRead,writeFile);



