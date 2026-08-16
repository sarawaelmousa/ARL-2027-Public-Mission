import math

def monitor_following_distance(distances: list[float], speeds: list[float]) :
        avrg_speed = sum (speeds) / len(speeds)
        safe_dist = avrg_speed*0.5

        count = 0                # counter to get the seconds
        tailgate_dist = set()        #set of tailgate distances so i can arrange it and get the 1st value as min distance and the length of the set as incedents
        

        for n in distances :
            if n < safe_dist:
                count += 1
                tailgate_dist.add(n)
            else:
                pass

        tailgate_dist = sorted(tailgate_dist)
        tailgating_sec = count 
        min_dist = tailgate_dist[0]
        tailgate_inc = len(tailgate_dist)
    
        results = (tailgating_sec , min_dist , tailgate_inc)
    return results 

print (monitor_following_distance(distances: list[float], speeds: list[float]))

