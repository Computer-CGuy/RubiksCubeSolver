from Rubiks_cube import *
cube = np.zeros((12,9),np.int32)
cube = init(cube)
for x in keystrokes:
    print(str(x))
    print(x(cube))
#print(cube)
