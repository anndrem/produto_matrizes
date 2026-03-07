def main():
    a = list([])
    n_rows = int(input("linhas: "))
    n_coluns = int(input("colunas: "))

#   criando uma matriz
    for i in range(n_rows):
        a.append(list([]))
        for j in range(n_coluns):
            a[i].append(int(input(f"coluna: {j + 1}\n linha: {i + 1}\n-")))
    
    res = int(input(f"deseja multiplica A por uma matriz B?\n"))

    if res == 1:
        b = list([])
        b_n_rows = int(input("linhas: "))
        b_n_coluns = int(input("colunas: "))

        if b_n_rows != n_coluns:
            return f"o numero de colunas de A dever ser igual o numero de colunas de b \n{n_rows} != {b_n_rows} "
        else:
            for i in range(b_n_rows):
                b.append(list([]))
                for j in range(b_n_coluns):
                    element = int(input(f"linha:{i + 1}\ncoluna: {j+ 1}\n-"))
                    b[i].append(element)
                    
        c = []
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

    else:
        return a
    
print(main())