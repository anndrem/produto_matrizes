
def compact():
    a = [
        [1,2, 3], 
        [4,1,2]]
    b = [
        [1,2],
        [3,4],
        [1,2]]
    c = []

    if len(a[0]) != len(b):
        return f"numero de colunas de A eh diferente do numero linhas de B\n{len(a[0])} != {len(b)}."
    
    for i in range(len(a)):
        c.append(list([]))
    

    i = 0
    j = 0
    for item in c:
        element = []
        k = 0
        l = 0
        while len(item) < len(b[0]):
            element.append(a[i][j]*b[k][l])
            if j == len(b) - 1:
                item.append(sum(element))
                element.clear()
                k=0
                l+=1
                j=0
            else: 
                k+=1
                j+=1
        i += 1
        
    return c

print(compact())