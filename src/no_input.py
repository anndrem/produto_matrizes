
def compact():
    a = [
        [1,2], 
        [3,4]]
    b = [
        [1,2],
        [3,4]]
    c = []
    for i in range(len(a[0])):
        c.append(list([]))
    

    if len(a[0]) != len(b):
        return f"numero de colunas de A eh diferente do numero linhas de B\n{len(a[0])} != {len(b)}."
    

    i = 0
    j = 0
    for item in c:
        element = []
        k = 0
        l = 0
        while len(item) < len(b):
            # novo ponteiro para alterar as colunas da matriz B
            element.append(a[i][j]*b[k][l])
            if j == len(b[0]) - 1:
                item.append(sum(element))
                element.clear()
                k=0
                l+=1
                j=0
            else: 
                k+=1
                j+=1
        i+=1
        
    return c

print(compact())