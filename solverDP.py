from Rubiks_cube import *
import random
cube = np.zeros((12,9),np.int32)
cube = init(cube)
for x in range(30):
    a = random.choice(keystrokes)
    cube = np.copy(np.copy(a(cube)))
print(cube)
check = np.zeros((12,9),np.int32)
check = init(check)
maxMoves = 13
stop = False
s = []
def solve(cube,level,last,moves):
    global keystrokes
    global stop
    if(stop):
        return False
    if(np.array_equal(check,cube)):
        stop = True
        return True
    if(moves>maxMoves):
        return False
    for x in keystrokes:
        if(x==last):
            if(level>2):
                continue
            if(solve(x(cube),level+1,x,moves+1)):
                s.append(str(x.__name__))
                return True
        else:
            if(solve(x(cube),1,x,moves+1)):
                s.append(str(x.__name__))
                return True
solve((((cube))),0,R,0)
print(s)
