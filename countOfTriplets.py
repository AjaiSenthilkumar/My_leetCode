def countTriple(arr) :
    arr.sort()
    n = len(arr)
    count = 0
    for i in range(n - 1,0,-1) :
        low = 0
        high = n - 1
        while low < high :
            target = arr[i]
            s = arr[low] + arr[high] 
            if s == target :
                count += 1
                low += 1
                high -= 1
            elif s < target :
                low += 1
            elif s > target :
                high -= 1
    return count

obj = countTriple([7,3,2,5,4,1])
print(obj)