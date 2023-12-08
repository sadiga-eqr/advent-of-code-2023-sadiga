
#raceTime = {'t1' : 57, 't2' : 72, 't3' : 69, 't4' : 92}
#raceDistance = {'d1' : 291, 'd2': 1172, 'd3': 1176, 'd4': 2026}

raceTime = {'t1' :57726992}
raceDistance = {'d1' : 291117211762026}


time_list = list(raceTime.keys())
dist_list = list(raceDistance.keys())
multiplier = 1
#for i in range(len(time_list)):
totalPossibilities = 0
for j in range(raceTime['t1']):
    distanceTraveled = (raceTime['t1'] - (j+1)) * (j+1)
    if(distanceTraveled > raceDistance['d1']):
        totalPossibilities += 1
#multiplier = multiplier * totalPossibilities


print(f'Total multiplier value = {totalPossibilities}')

