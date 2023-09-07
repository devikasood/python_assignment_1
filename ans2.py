arr1 = []

n1 = int(input("Enter number of elements : "))
for k in range(0, n1):   
	ele1 = int(input())
	arr1.append(ele1)
print(arr1)

arr2 = []

n2 = int(input("Enter number of elements : "))
for l in range(0, n2):   
	ele2 = int(input())
	arr2.append(ele2)


print(arr2)
arr_final = arr1 + arr2
print(arr_final)
