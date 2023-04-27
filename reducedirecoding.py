# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water,
# it's important to save yourself some energy, otherwise you might die of thirst!

# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]

def reduce_directions(alist):
    opposite_directions = {
        'NORTH': 'SOUTH',
        "SOUTH": "NORTH",
        "EAST": 'WEST',
        'WEST': 'EAST'
    }
    
    direction_stack = []
    for direction in alist: #O(N)
        if direction_stack and direction_stack[-1] == opposite_directions[direction]:
            direction_removed = direction_stack.pop() #O(1)
            print(direction_removed)
        else:
            direction_stack.append(direction)
    return direction_stack

print(reduce_directions(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

  #any list or collection, if we remove, its the last one added