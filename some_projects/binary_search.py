def binary_search(st, end, arr, target):
    while(st<=end):
        mid = int((end+st)/2)
        if arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            st = mid+1
        else:
            return mid
        
    return -1


if __name__ == '__main__':
    arr = [2,7,45,78,90,101,398]
    print(binary_search(0,len(arr)-1,arr, 2))
    print(len(arr)-1)