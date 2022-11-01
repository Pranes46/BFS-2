class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]: #tc - 0(mn), sc - 0(n)
        m = len(mat) #to calculate the no.of.row
        n= len(mat[0]) #to calculate the no.of.column
        directions = [[0,1],[1,0],[0,-1],[-1,0]] #directions array
        q = deque() #initializing deque for queue opertaion
 
        for i in range(m): #tarversing through the netire matrix and if the value is 1 we are appending it into the queue else if the value is 0 we are changing the value to -1.
            for j in range(n): 
                if mat[i][j] == 0: 
                    q.append((i,j)) 
                else: 
                    mat[i][j] = -1 

        dist = 0 
        while q:  #loop will run until the queue become empty
            size = len(q) 
            dist+=1 #increment the countto check the distance between 1's and 0's
            for _ in range(size): #level order traversal
                curr = q.popleft()   #popping out the first element in the queue
                for x,y in directions: #using directions array we are checking whether the curr element neighbor has 0 
                    nr = x+curr[0] #row
                    nc = y+curr[1] #column

                    if nr>=0 and nr<m and nc>=0 and nc<n and mat[nr][nc] == -1: #boundary check
                        mat[nr][nc] = dist 
                        q.append((nr,nc)) #append the index to q

        return mat #return matrix
        