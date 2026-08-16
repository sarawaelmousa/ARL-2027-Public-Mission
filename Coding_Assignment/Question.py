import test_following_distance.py 
import math


def monitor_following_distance(distances: list[float], speeds: list[float]) 
        avrg_speed = (speeds[0] + speeds[1] + speeds[2] + speeds[3] + speeds[4])/5
        safe_dist = avrg_speed*0.5

        count = 0
        tailgate_dist = set()
        
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
    
        result = (tailgating_sec , min_dist , tailgate_inc)
    return results 

