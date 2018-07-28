
#BubbleSort

#array
array = [4,1,3,7,2,9,90,22,11,43,44,32];  

#outside loop
for i in range(0,len(array)-1):
	#inside loop
	for j in range(i,len(array)-1):
		#conditional
		if array[j]>array[j+1]:
			print('swappin '+str(array[j])+' and '+str(array[j+1]))
			print(array);
			#swapping process
			temp = array[j];
			array[j] = array[j+1];
			array[j+1] = temp;



#finished outlook
print(array);


