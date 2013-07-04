def monge(k,num1,num2):
    m = len(num1)
    n = len(num2)
    matrix = [[0 for x in xrange(m)] for x in xrange(n)]
    i,j = 0,0
    while i < m and j < n:
        matrix[i][j] = num1[i] + num2[j]
        print "Matrix element at position (%d,%d) is %d" %(i,j,matrix[i][j])
        if matrix[i][j] == k:
            print "found at (%d,%d)" %(i,j)
            return
        elif matrix[i][j] < k:
            j += 1
        elif matrix[i][j] > k:
            i += 1
    print "Not Found"
        
    #populating all elements in monge array
    '''for i in range(m):
        for j in range(n):
            matrix[i][j] = num1[i] + num2[j]
            print "matrix element at position (%d,%d) is %d " %(i,j,matrix[i][j])
            
    #Then Finding the element from array
    x,y = 0,0
    while x < m and y < n:
        if matrix[x][y] == k:
            print "found at (%d,%d)" %(x,y)
            return
        elif matrix[x][y] < k:
            y += 1
        elif matrix[x][y] > k:
            x += 1'''
                

    #Brute-force Approach
    '''for i in range(m):
        for j in range(n):
            if num1[i]+ num2[j] == k:
                print "found"
                return
            elif num1[i]+ num2[j] < k:
                j += 1
            elif num1[i] + num2[j] > k:
                i += 1'''


if __name__ == '__main__':
    list1 = [8,6,5,4,3]
    list2 = [1,2,5,7,9]
    print "Enter the element k"
    search = int(raw_input())
    monge(search,list1,list2)
    
