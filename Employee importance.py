"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:     #TC - O(n), SC - O(n)
        
        
        adj = {}  #adjacency list
        totalImportance = 0  #to calculate the total importance
        q = deque()  #initializing deque to use the queue
        q.append(id)  #we are appending the first id in ithe queue
        for emp in employees:  #to append the key,val pair in the adjacency list, with id as key and importance,subordiante as values
            adj[emp.id] = [emp.importance, emp.subordinates]
            
        while q:  #loop will run until the queue become empty, we are using bfs here
            currEmployee = q.popleft() #poping the first element in the queue
            totalImportance+= adj[currEmployee][0]  #calculating the importance from thta popped val
            
            for subordinate in adj[currEmployee][1]:  #we are checing whether the popped node has any subordiante, if subordinate exists we are appending it in the queue and continuing the process
                q.append(subordinate)
                
        return totalImportance  #we are returning the total imp after queue bceomes empty
        
        
        
        