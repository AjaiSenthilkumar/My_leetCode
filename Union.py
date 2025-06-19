def findUnion( a, b):
        # code her
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        res = []
        
        while i<n and j < m :
            if a[i] <= b[j] and a[i] not in res:
                res.append(a[i])
                i += 1
            elif b[j] not in res :
                res.append(b[j])
                j += 1
        return res

a = [85, 25, 1, 32, 54, 6]
b = [85, 2]
obj = findUnion( a, b)
print(obj)