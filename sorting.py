import array

arr = array('i',[5,6,7,3,4,9,2,1,8])
for x in range(len(arr)):
	for y in range(len(x)):
			if arr[x] > arr[y]:
				arr[x],arr[y]=arr[y],arr[x]
