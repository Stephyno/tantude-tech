def linear(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1       
my_list=[2,3,5,6,8,11,13,14]
x=11
result=linear(my_list,x)
if result != -1:
    print(f"found the index value {result}")
else:
    print("not found")    
