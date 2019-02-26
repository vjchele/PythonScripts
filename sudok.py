s = [[8,5,0,0,0,2,4,0,0],
         [7,2,0,0,0,0,0,0,9],
         [0,0,4,0,0,0,0,0,0],
         [0,0,0,1,0,7,0,0,2],
         [3,0,5,0,0,0,9,0,0],
         [0,4,0,0,0,0,0,0,0],
         [0,0,0,0,8,0,0,7,0],
         [0,1,7,0,0,0,0,0,0],
         [0,0,0,0,3,6,0,4,0]]
backtracks = 0
n = 9
def printSudoku(s):
    for i in range(0,n):
        for j in range(0,n):
            print(s[i][j], end=" ")
        print()


def findNext(s):
    for i in range(0,n):
        for j in range(0,n):
            if s[i][j] == 0:
                return i,j
    return -1,-1

def isValid(s,i,j,e):
    value = all(e!=k for k in s[i])
    if value:
        value = all(e!=s[x][j] for x in range(0,n))
        if value:
            k,m = 3* (i//3), 3* (j//3)
            for i in range(k,k+3):
                for j in range(m,m+3):
                    if s[i][j]==e:
                        return False
            return True
    return False

def isValidModified(s,i,j,e):
    k,m = 3* (i//3), 3* (j//3)
    for a in range(k,k+3):
        for b in range(m,m+3):
            if s[a][b]==e:
                return False
    value = all(e!=k for k in s[i])
    if not value:
        return False
    return all(e!=s[x][j] for x in range(0,n))
    
    

def solveSudoku(s):
    global backtracks
    i,j = findNext(s)
    if i==-1:
        return True

    for e in range(1,n+1):
        if isValidModified(s,i,j,e):
            s[i][j] = e
            if solveSudoku(s):
                return True
            backtracks+=1
            s[i][j] = 0
    return False
            
        
 

printSudoku(s)
print("-----------")
solveSudoku(s)

print("Number of backtracks {0}".format(backtracks))

print("-----------")

printSudoku(s)

