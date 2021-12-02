
def part1():
    h = 0   #Horizontal position
    v = 0   #vertical position

    with open("/localdisk/github/Python-Projects/adventofcode/dive.txt", "r") as f:
        data = f.read().split()

        for ii in range(0, len(data) - 1, 2):
            #print(ii)
            action = data[ii]
            val = int(data[ii+1])
            print(action, val)
            if (action == "forward"):
                h += val
            elif (action == "up"):
                v -= val
            elif (action == "down"):
                v += val


    print(h,v)
    print(h*v)

"""
In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. 
The commands also mean something entirely different than you first thought:
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

"""

def part2():
    aim = 0
    h = 0
    d = 0
    with open("/localdisk/github/Python-Projects/adventofcode/dive.txt", "r") as f:
        data = f.read().split()

        for ii in range(0, len(data) - 1, 2):
            action = data[ii]
            val = int(data[ii+1])
            print(action, val)
            if (action == "forward"):
                h += val
                d += (aim * val)
            elif (action == "up"):
                aim -= val
            elif (action == "down"):
                aim += val
    print(h,d,aim)
    print(h*d)

part2()