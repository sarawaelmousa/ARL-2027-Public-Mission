import math


def monitor_following_distance(distances, speeds):
    
    modified_speeds=set() # set i created to get the max speed from

    if not speeds:
        avrg_speed=0.0
    else:
        for n in speeds:
            modified_speeds.add(n)
        modified_speeds = sorted(modified_speeds)
       #avrg_speed = sum(modified_speeds) / len(modified_speeds) [the old func i used]
        avrg_speed = modified_speeds[-1]
        

    safe_dist = avrg_speed*0.5

    count = 0                # counter to get the seconds of tailgating
    tailgate_dist = set()    #set of tailgate distances so i can know the incedent times from the length
    modified_dist = set()    #the set i made to get the minimum distance it contain all the distances either safe or not

    if not distances:
        min_dist=0.0
        tailgate_inc=0
        tailgating_sec=0
    else:
       for n in distances :
            if n < safe_dist:
                count += 1
                tailgate_dist.add(n)
                modified_dist.add(n)

            else:
                modified_dist.add(n)
                
    tailgating_sec = count
    modified_dist = sorted(modified_dist)
    min_dist = modified_dist[0] if modified_dist else 0.0
    tailgate_inc = len(tailgate_dist)
    
    
    results = (tailgating_sec, min_dist, tailgate_inc)
   # print (results)

    return results