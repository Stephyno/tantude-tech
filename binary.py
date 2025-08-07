def binary(arr,key):
    left=0
    right= len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]== key:
            return mid
        elif arr[mid]<key:
            left= mid+1 
        else:
            right= mid-1
    return -1
my_list=[1,2,5,6,7,8,9,10,13,]   
x=7
result= binary(my_list,x)

if result!=-1:
    print(f"find the index {result}")
else:
    print(not find)



        




