def listTotuple(list):
    #input:[[1,2],[2,3],[1,3]]
    #output:((1,2),(2,3),(1,3))
    tup = []
    for item in list:
        tu1 = tuple(item)
        tup.append(tu1)
    return tuple(tup)

if __name__ == "__main__":
    lis = [[1,2],[2,3],[1,3]]
    a = listTotuple(lis)
    print (a)