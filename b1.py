def binary_search(matrix, target):
    low = 0
    high = len(matrix[0])*len(matrix)-1
    while low<=high:
        mid=(low+high)//2
        index = [mid//len(matrix[0]),mid%(len(matrix[0]))]
        val = matrix[index[0]][index[1]]
        if val == target:
            return(index)
        elif val<target:
            low = mid+1
        else:
            high = mid-1
    return(False)

if __name__ == '__main__':
    dim = [list(map(int,input().split()))]
    k = int(input())

    matrix = [list(map(int,input().split())) for i in range(dim[0][0])]
    result = binary_search(matrix, k)
    if result != False:
        print(True)
        print(result[0],result[1],sep=" ")
    else:
        print(False)