import numpy as np
import random as r
check = np.zeros((12,9),np.int32)
steps = []
solved = False
#Making the Rubiks Cube Grid
def init(array):
    array.fill(0)
    array=limit(1,0,3,3,6,array)
    array=limit(2,3,3,6,6,array)
    array=limit(3,6,3,9,6,array)
    array=limit(4,9,3,12,6,array)
    array=limit(5,3,0,6,3,array)
    array=limit(6,3,6,6,9,array)
    return array
#Solving

#Box Fill
def limit(val,x,y,x1,y1,array):
    k=y
    while x < x1:
        y=k
        while y<y1:
            array[x][y]=val#r.randint(1,9=6)
            #print(x,x1)
            y+=1
        x+=1
    return array
# R Rotate
def clockwise(x,y,array):
    ret = np.copy(array)
    #ret[(x),(y-1):(y+2)]=array[x:(x+3),y]
    ret[x,y:(y+3)]=array[(x):x+3,y]
    ret[x:(x+3),(y+2)]=array[x,y:(y+3)]
    #ret[(x),y:y+3]=array[x:(x+3),(y+2)]
    #print(ret,x)
    #ret[(x+2),(y+2):(y-1):-1]=array[x:x+3,y+2]
    ret[(x+2),(y):(y+3)]=array[x+2:x-1:-1,y+2]
    #ret[(x),y:(y+3)]=array[x+2:(x-1):-1,y]
    ret[x:x+3,y]=array[x+2,y:y+3]
    return ret
def clockwiseU(x,y,array):
    ret = np.copy(array)
    #ret[(x),(y-1):(y+2)]=array[x:(x+3),y]
    ret[x,y:(y+3)]=array[(x):x+3,y]
    ret[x:(x+3),(y+2)]=array[x,y:(y+3)]
    #ret[(x),y:y+3]=array[x:(x+3),(y+2)]
    #print(ret,x)
    ret[(x+2),(y+2):(y-1):-1]=array[x:x+3,y+2]
    #ret[(x+2),(y):(y+3)]=array[x+2:x-1:-1,y+2]
    #ret[(x),y:(y+3)]=array[x+2:(x-1):-1,y]
    ret[x:x+3,y]=array[x+2,y:y+3]
    return ret
    """ret[3,9:5:-1]=array[3:6,6]
    ret[3:6,8]=array[3,6:9]
    ret[5,9:5:-1]=array[3:6,8]
    ret[3:6,6]=array[5,6:9]
    """#ret[5,0:3]=array[5:2:-1,2]
   # ret[3:6,0]=array[5,0:3]
    #ret[3,0:3]=array[5:2:-1,0]
    #ret[3:6,2]=array[3,0:3]
def R(array):
    ret = np.copy(array)
    ret[0:3,5]=array[3:6,5]
    ret[3:6,5]=array[6:9,5]
    ret[6:9,5]=array[9:12,5]
    ret[9:12,5]=array[0:3,5]
    #Clockwise Rotation
    """ret[3,9:5:-1]=array[3:6,6]
    ret[3:6,8]=array[3,6:9]
    ret[5,9:5:-1]=array[3:6,8]
    ret[3:6,6]=array[5,6:9]"""
    ret = clockwise(3,6,ret)
    return ret
def L(array):
    ret = np.copy(array)
    ret = clockwise(3,0,ret)
    ret[0:3,3]=array[9:12,3]
    ret[3:6,3]=array[0:3,3]
    ret[6:9,3]=array[3:6,3]
    ret[9:12,3]=array[6:9,3]

    #Anti-Clockwise Rotation
    #ret[5,0:3]=array[5:2:-1,2]
    #ret[3:6,0]=array[5,0:3]
    #ret[3,0:3]=array[5:2:-1,0]
    #ret[3:6,2]=array[3,0:3]
    return ret
def D(array):
    ret = np.copy(array)
    ret[5,3:6]=array[5,0:3]
    ret[5,6:9]=array[5,3:6]
    ret[9,3:6]=array[5,9:5:-1]
    ret[5,0:3]=array[9,5:2:-1]
    ret = clockwise(6,3,ret)
    return ret
def U(array):
    ret = np.copy(array)
    ret = clockwiseU(0,3,ret)
    ret[3,3:6]=array[3,6:9]
    ret[3,0:3]=array[3,3:6]
    ret[11,5:2:-1]=array[3,0:3]
    ret[3,6:9]=array[11,5:2:-1]

    return ret
def F(array):
    ret = np.copy(array)
    ret = clockwise(3,3,ret)
    ret[3:6,6]=array[2,3:6]
    ret[3:6,2]=array[6,3:6]
    ret[2,3:6]=array[5:2:-1,2]
    ret[6,3:6]=array[5:2:-1,6]
    return ret
def B(array):
    ret = np.copy(array)
    ret = clockwise(9,3,ret)
    ret[5:2:-1,8]=array[8,3:6]
    ret[8,3:6]=array[3:6,0]
    ret[0,3:6]=array[3:6,8]
    ret[5:2:-1,0]=array[0,3:6]
    return ret
def solve(SOP,solved):
    a = [R,L,D,U,F,B]
    b = ['R','L','D','U','F','B']

    """if solved==False:
        if np.array_equal(SOP,array):
            #print(SOP,array)
            solved = True
            return "GUD"
            #steps.append(b[])
        else:
            for x in range(6):
                if a[x](SOP)solve(a[x](SOP),solved)
    """
#init(array)
#SO = np.array([0,0,0,1,1,4,0,0,0],[0,0,0,1,1,4,0,0,0],[0,0,0,1,1,4,0,0,0],[5,5,5,2,2,1,6,6,6],[5,5,5,2,2,1,6,6,6],[5,5,5,2,2,1,6,6,6], [0,0,0,3,3,2,0,0,0],[0,0,0,3,3,2,0,0,0],[0,0,0,3,3,2,0,0,0],[0,0,0,4,4,3,0,0,0],[0,0,0,4,4,3,0,0,0],[0,0,0,4,4,3,0,0,0])
keystrokes=[R,L,F,B,U,R,D]
def shuffle(keystrokes,arr):
    for x in keystrokes:
        arr = x(arr)
    return arr
#array=shuffle(keystrokes,array)
#a = [R,L,D,U,F,B]
#array = a[1](array)

"""num = int()
key_down = str()

while True:

    while keyboard.is_pressed('r'):
        key_down = 'R'
        num = 0
    while keyboard.is_pressed('l'):
        key_down = 'L'
        num = 1
    while keyboard.is_pressed('d'):
        key_down = 'D'
        num = 2
    while keyboard.is_pressed('u'):
        key_down = 'U'
        num = 3
    while keyboard.is_pressed('f'):
        key_down = 'F'
        num = 4
    while keyboard.is_pressed('b'):
        key_down = 'B'
        num = 5
    if key_down != 'k':
        os.system('cls')
        #print(key_down.upper())
        print(a[num](array))
        #sys.stdout.write('\r',a[num](array),end='')
        #os
        #sys.stdout.write(str(a[num](array)))
       # sys.stdout.flush()

        array = a[num](array)
        key_down = 'k'


   solved=False
SO = np.zeros((12,9),np.int32)
init(SO)
SO = R(array)
#print(SO)
checker = np.copy(array)
print(solve(SO,solved))"""
#print(steps)
#Code starts here
#po=np.array([
#solve(po,0)
#print()
