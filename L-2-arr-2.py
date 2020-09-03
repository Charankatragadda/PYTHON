#Program to copy all array elements from one array to other in reverse order
#initalise array
arr1 = [1,2,3,4,5];

#create another array arr2 with size of arr1
arr2 = [None] * len(arr1);
length = len(arr1)
#copying all elements of one array to other
for i in range(0, length):
    arr2[i] = arr1[length-i-1];

#displaying elements of array arr1
print("elements of original array: ");
#for i in range(0, len(arr1)):
  #print(arr1[i]),
print(arr1)
print();

#displaying elements of array arr2
print("elements of new array: ");
for i in range(0, len(arr2)):
    print(arr2[i])
