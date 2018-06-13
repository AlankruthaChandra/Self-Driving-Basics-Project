import math
from heapq import heappush, heappop 

def heuristic(M, a, b):
    return math.sqrt((M.intersections[b][0] - M.intersections[a][0])**2 + (M.intersections[b][1]- M.intersections[a][1])**2)

def shortest_path(M,start,goal):
   
    open_list =[] #active nodes to be visited
    closed_set = set() #to store nodes that are already visited
    
    
    cameFrom = {} #parent node
    gscore = {}
    fscore = {}
    gscore[start] = 0
    fscore[start] =  gscore[start] + heuristic(M, start, goal) 
    heappush(open_list, (fscore[start], start)) #push item into open_list
    
    while open_list:
        current = heappop(open_list)[1] #pop item that has smallest fscore value
        'print(current)'
        
        if current == goal:
            return reconstruct_path(cameFrom , current)
        
        closed_set.add(current)
        
        for neighbor in M.roads[current]:
            new_g = gscore[current] + heuristic(M, current, neighbor) #gscore of neighbor  and its heuristic
            'print (gscore[current])'
            
            if neighbor in closed_set and new_g >= gscore[neighbor]:#checking if the neighbor is already visited
                continue
            
            if neighbor not in [i[1]for i in open_list] or new_g < gscore[neighbor]:#checking if the neighbor not in open_list and also the new_gscore is with in the gscore[neighbor]
                gscore[neighbor] = new_g
                fscore[neighbor] = new_g + heuristic(M,  goal, neighbor)
                
                cameFrom[neighbor] = current
                heappush(open_list, (fscore[neighbor], neighbor))#push neighbor and its fscore value in open_list
                'print (open_list)'
            'print(cameFrom)'      
                
    return False
    

def reconstruct_path(cameFrom , current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
        
        '''print('total_path:', total_path)'''
        
    return total_path[::-1]
    