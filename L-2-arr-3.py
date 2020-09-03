#program to remove duplicate elements from an array

#defining the user function

def Remove(arr):
    final = []
    for num in arr:
        if num not in final:
            final.append(num)
    return final

arr = [10, 4, 3, 10, 3, 5, 2]
print(arr)
print(Remove(arr))
           

