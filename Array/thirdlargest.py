def thirdlargest(arr):

    largest = 0
    seclarg = 0
    thirdlarg = 0


    for i in range(len(arr)):
        if arr[i] > largest:
            thirdlarg = seclarg
            seclarg = largest
            largest = arr[i]
        elif arr[i] > seclarg and arr[i] < largest:
            thirdlarg = seclarg
            seclarg = arr[i]
        elif arr[i] > thirdlarg and arr[i] < seclarg:
            thirdlarg = arr[i]
    
    return thirdlarg


arr = [1,2,3,5,6,1,2,3]

print(thirdlargest(arr))