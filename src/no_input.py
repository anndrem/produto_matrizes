
def compact():
    a = [
        [1,2], 
        [3,4]]
    b = [
        [1,2],
        [3,4],]
    c = []
    for i in range(len(a)):
        c.append(list([]))
    print(c)
    

    if len(a[0]) != len(b):
        return f"numero de colunas de A eh diferente do numero linhas de B\n{len(a[0])} != {len(b)}."
    

    i = 0
    j = 0
    for item in c:
        c_c = 0
        element = []
        k = 0
        l = 0
        while len(item) < len(b[0]):
            c_c += 1
            # novo ponteiro para alterar as colunas da matriz B
            print(f"ponteiros {c_c}:\nA\n-i = {i}\n-j = {j}\n\nB\n-k = {k}\n-l = {l}\n")
            # if l < len(b[0]) and i < len(a):
            element.append(a[i][j]*b[k][l])
            if j == len(b) - 1:
                item.append(sum(element))
                element.clear()
                k=0
                l+=1
                j=0
                print(f"info. loop:\n-len(item) = {len(item)}\n-len(b) = {len(b)}\n-c = {c}\n-continua = {len(item) < len(b[0])}\n")
            # elif l == len(b[0]) - 1:
            #     l = 0
            # elif i == len(a) - 1:
            #     i = 0
            else: 
                k+=1
                j+=1
            # print(f"len(item) = {len(item)}\nlen(b) = {len(b)}\n")
        # if i == len(a) - 1:
        #     return c
        # else:
        i += 1
        
    return c

print(compact())