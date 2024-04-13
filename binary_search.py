


def binary_search(arr,x,low,high):
    mid=(low+high)//2
    if x==arr[mid]:
        return mid
    elif x>arr[mid]:
        return binary_search(arr,x,mid+1,high)
    else:
        return binary_search(arr,x,low,mid-1)
arr=[11,22,33,44,55,66,77,88,99]
x=88
low=0
high=len(arr)-1
bin_search=binary_search(arr,x,low,high)
print(bin_search)

    