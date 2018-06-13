import math 
    
def heuristic_function(a,b):
    
    return math.sqrt((M.intersections[b][0] - M.intersections[a][0])**2 + ((M.intersections[b][1] -M.intersections[a][1])**2)
                     
def shortest_path(M,start,goal):
    frontier = M.roads[start]
                     
    camefrom = {}
    
    
    cost_so_far = {}
    camefrom[start] = none
    cost_so_far[start] = 0
                     
    while not frontier.empty():
        current = frontier.get()
                     
                   
                    
    
    s_list = M.roads[start]
    g_list = M.roads[goal]
    
    x1 = M.intersections[start][0]
    y1 = M.intersections[start][1]
    
    x2 = M.intersections[goal][0]
    y2 = M.intersections[goal][1]
    
    h = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    for each in s_list:
        
        visited = {}
        each_x2 = M.intersections[s_list[each]][0]
        each_y2 = M.intersections[s_list[each]][1]
        
        h` = math.sqrt((each_x2 - x1)**2 + (each_y2 - y1)**2)
        
        g` = math.sqrt((each_x2 - x2)**2 + (each_y2 - y2)**2)
        
        visited.append(each:(h`+ g`))
        
        return visited
    
    k = min(visited, key = visited.get)
    
    path = []
    
    path.append(k)
    
    m_list = M.roads[k]
    
    
        
        
        
     
        
        
        
    
    
    
    print (h)
   
    print (intersections_start, intersections_goal)
    
    print("shortest path called")
    return