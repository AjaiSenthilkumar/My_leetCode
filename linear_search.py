def LinearSearch(arr,target) :

    for i in range(len(arr)) :
        if target == arr[i] :
            return i
    return -1


print(LinearSearch([2,4,5,6,73,9],73))