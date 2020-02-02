from rcube import *
cube = np.zeros((12,9),np.int32)
cube = init(cube)
print(cube)
check = np.zeros((12,9),np.int32)
check = init(check)
#keystrokes
strokes = [Ri,Li,Fi,Bi,Ui,Di]
def sample():
    global cube
    update(cube)
    return 0.1

moves = [R,U,Ri,Ui]
cn = 0
update(cube)
bpy.app.timers.register(sample)
"""while (not np.array_equal(check,cube)) or (cn==0):
    
    cn += 1
print(cn)
"""


def solve():
    global cube
    global cn
    if((not np.array_equal(check,cube)) or (cn==0)):

        for x in moves:
            cube = np.copy(x(cube))
        cn+=1
    else:
        cn = 0
    return 0.2
bpy.app.timers.register(solve)