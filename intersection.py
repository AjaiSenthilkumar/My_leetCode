def numberofElementsInIntersection(a, b):      
        a.sort()
        b.sort()
        res = []
        i = 0
        j = 0
    
        while i < len(a) and j < len(b):
            if a[i] < b[j] :
                i+=1
            elif b[j] < a[i] :
                j += 1
            else :
                res.append(a[i])
                i+=1
                j+=1
    
        return len(res)
a = [85, 25, 1, 32, 54, 6]
b = [85, 2]
obj = numberofElementsInIntersection(a,b)