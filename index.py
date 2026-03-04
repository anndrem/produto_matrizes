def main():
    a = list([])
    n_rows = int(input("linhas: "))
    n_coluns = int(input("colunas: "))

#   criando uma matriz
    for i in range(n_rows):
        a.append(list([]))
        for j in range(n_coluns):
            a[i].append(int(input(f"coluna: {j + 1}\n linha: {i + 1}\n")))
    
    res = int(input("deseja multiplica A por uma matriz B?"))

    if res == 1:
        b = list([])
        b_n_rows = int(input("linhas: "))
        b_n_coluns = int(input("colunas: "))

        if b_n_rows != n_coluns:
            return f"o numero de colunas de A dever ser igual o numero de colunas de b \n{n_rows} != {b_n_rows} "
        else:
            for i in range(b_n_coluns):
                b.append(list([]))
                for j in range(b_n_coluns):
                    element = int(input(f"coluna: {i + 1}\nlinha:{j + 1}\n"))
                    b[i].append(element)
                    
        c = []
        for i in range(len(a[0])):
                c.append(list([]))
        
        i = 0
        j = 0
        for item in c:
            element = []
            k = 0
            l = 0
            while len(item) < len(b):
                # novo ponteiro para alterar as colunas da matriz B
                element.append(a[i][j]*b[k][l])
                if j == 1:
                    item.append(sum(element))
                    element.clear()
                    k+=1
                    l=0
                    j=0
                else: 
                    l+=1
                    j+=1
            i+=1
        return c

    else:
        return a
    
print(main())