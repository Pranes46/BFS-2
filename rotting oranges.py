class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:  #tc - 0(mn), sc - 0(n)
        
        m = len(grid)  #calculating the number of rows
        n = len(grid[0])  #calculating the num of columns
        time = 0  #times used to rot the fresh oranges
        freshcount = 0  #to count how many fresh oranges we have 
        q = deque()  #implement queue, we are doing bfs here
        dir_ =[[-1,0],[0,1],[1,0],[0,-1]]  #direction array to traverse the matrix
        
        for i in range(m):  #this loop will traverse through matrix and will append the all the rotten oranges indexes into the queue and will count the freshorange
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                    
                elif grid[i][j] ==1:
                    freshcount+=1
                    
        while q and freshcount!=0:  #loop will run until the q becomes empty and freshorange is not equal to 0
            time+=1  #increasing the time by 1 unit cause we are processing the orange
            size = len(q)  #to do level order traversal
            for _ in range(size): 
                curr = q.popleft()  #popping the first element
                
                for r,c in dir_:  #to access the neighbor oranges for the elemnt we popped out from the queue
                    nr = r+curr[0]  #toknow the row
                    nc = c+curr[1] #to know the column
                    
                    if nr>=0 and nr<m and nc>=0 and nc<n: #boundary check
                        if grid[nr][nc] == 1:  #if the grid value is equal to one we are chaning to 2. 
                            grid[nr][nc] = 2
                            freshcount-=1  #after changing the orange we are decrementing thr fresh count
                            q.append((nr,nc))
                            
        if freshcount == 0: #if the freshcount is 0 that means all the oranges are rotten
            return time  #returning time
        
        else:
            return -1  #if we couldnt rot all the orange we are returning -1
                            
                
        