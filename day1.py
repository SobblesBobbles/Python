class day1 :
 	'documentation for day1'

 	staticCounter = 0;
 	name="default"

 	def __init__(self,name):
 		day1.staticCounter+=1;
 		self.name = name;
 		

 	def display(self):
 		print(day1.staticCounter);
 		print(day1.name+' is his original name.');
 		print(self.name+ ' is his name.');

 	def delete(self):
 		day1.staticCounter-=1;




person1 = day1('Stephen');

person1.display();
