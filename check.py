from Rubiks_cube import *
cube = np.zeros((12,9),np.int32)
cube = init(cube)
print(cube)
check = np.zeros((12,9),np.int32)
check = init(check)
#keystrokes
strokes = [Ri,Li,Fi,Bi,Ui,Di]

moves = [R,U,Ri,Ui]
cn = 0
while (not np.array_equal(check,cube)) or (cn==0):
    for x in moves:
        cube = np.copy(x(cube))
        print(cube)
    cn += 1
print(cn)
