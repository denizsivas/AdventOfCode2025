"""
Question 1 - Solving the dial

Example:
For example, suppose the attached document contained the following rotations:

L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
Following these rotations would cause the dial to move as follows:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32.
Because the dial points at 0 a total of three times during this process, the password in this example is 3.

"""

# Read the input txt file and convert it to a list

# config
printer = True

with open('input_q1.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()
    if printer == True:
        print("The read lines are:" + '\n')
        print(lines)

# start from the 50 index
count_of_zeros = 0
zero_passes = 0
curr_pos = 50
for line in lines:
    # determine the rotation direction
    if line[0] == 'R':
        # turns clockwise
        new_pos = int(curr_pos) + int(line[1:])
    else:
        # turns counterclockwise
        new_pos = int(curr_pos) - int(line[1:])
    new_pos = new_pos % 100
    curr_pos = new_pos
    if new_pos == 100 or new_pos == 0:
        count_of_zeros += 1
    if line[0] == 'R':
        print('Counterclockwise rotation -- New Position: ' + str(new_pos))
    else:
        print('Counterclockwise rotation -- New Position: ' + str(new_pos))

print('The number of stationary zeros: ' + str(count_of_zeros))

print('Password: ' + str(int(count_of_zeros)))