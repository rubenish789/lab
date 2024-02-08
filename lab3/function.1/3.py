def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chicken = numheads - rabbits
    print(int(rabbits), int(chicken))