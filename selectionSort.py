
#Selection sort

#array
array = [4,1,3,7,2,9,90,22,11,43,44,32];  

#outside loop
for i in range(0,len(array)):
	#inside loop
	for j in range(i,len(array)):
		#conditional
		if array[i]>array[j]:
			print('swappin '+str(array[i])+' and '+str(array[j]))
			print(array);
			#swapping process
			temp = array[i];
			array[i] = array[j];
			array[j] = temp;
	print('round'+str(i));


#finished outlook
print(array);


