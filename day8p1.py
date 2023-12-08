import re
import math


direction = ""
network = {}
file_path = r'C:\Users\sadiga\Desktop\Python Exercises\day8Input.txt'
dest_node = list()
start_node = list()


def navigate(startPoint):
    total_steps = 0
    global dest_node, binary_direction
    terminate = False
    while (not terminate):
        for char in binary_direction:
            #print(f" bin direct = {binary_direction}")
            #print(f"character = {char}")
            next_node = network[str(startPoint)][int(char)]
            #print(f"next node = {next_node}")
            startPoint = next_node
            total_steps += 1
            if( str(next_node).endswith('Z')):
                terminate = True
                break

    print(f'inside func = {total_steps}')

    return total_steps


with open(file_path, 'r') as file:
    # Read file content line by line
    i=0
    for line in file:
        if i == 0:
            direction = line
            i += 1
        elif i == 1:
            #Do nothing
            i= i+1
        else:
            sections = line. split('=')
            #print(f'{sections[1].strip()}')
            string_tuple = sections[1].strip()
            parts = re.split('[(,)]', string_tuple)
        
            # Convert value to a list
            converted_list = [parts[1].strip(), parts[2].strip()]
            network[sections[0].strip()] = converted_list
            
    binary_direction = direction.replace('L', '0').replace('R', '1').strip()

for key in network:
    if key.endswith('A'):
        start_node.append(key)


total_count = [navigate(start_point) for start_point in start_node]
Least_steps = math.lcm(*map(int, total_count))

print(f"{Least_steps}")

print(f" outside total_count = {total_count}")