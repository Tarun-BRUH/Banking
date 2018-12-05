def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        Left = arr[:mid]   
        Right = arr[mid:]  
  
        mergeSort(Left)  
        mergeSort(Right) 
  
        i = j = k = 0
           
        while i < len(Left) and j < len(Right): 
            if Left[i] < Right[j]: 
                arr[k] = Left[i] 
                i+=1
            else: 
                arr[k] = Right[j] 
                j+=1
            k+=1
          
        while i < len(Left): 
            arr[k] = Left[i] 
            i+=1
            k+=1
          
        while j < len(Right): 
            arr[k] = Right[j] 
            j+=1
            k+=1

def insertionsort(tbslist):
    for i in range(1,len(tbslist)):
        v = tbslist[i]
        j=i
        while tbslist[j-1] > v and j>=1:
            tbslist[j]=tbslist[j-1]
            j-=1

        tbslist[j]=v
        print(tbslist)
        
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return mid
