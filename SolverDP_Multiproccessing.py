import asyncio
import multiprocessing as mp
from multiprocessing import Process
from Rubiks_cube import *
from os import getpid
# R , L , D , U , F ,B
cube = np.zeros((12,9),np.int32)
a = [R,L,D,U,F,B]
solved = False
check = np.copy(init(cube))
l = 0
ans = []
saver = True
h = ["a","b"]
o = {}
processes = []
ender = " "
stop = False
maxMoves = 13
def solve(cube,level,last,moves):
    global keystrokes
    global stop
    global o
    global ender
    global maxMoves
    if(stop):
        return False
    if(np.array_equal(check,cube)):
        ender = mp.current_process()
        stop = True
        return True
    if(moves>maxMoves):
        return False
    processes = []
    for x in keystrokes:
        if(x==last):
            if(level>2):
                continue
            p = mp.Process(target = solve,args =[x(cube),level+1,x,moves+1])
            """if(o[str(mp.current_process())]==None):
                o[str(mp.current_process())] = []
            o[str(mp.current_process())].append(x.__name__)
            """
            p.start()
            processes.append(p)
        else:
            p = mp.Process(target = solve,args =[x(cube),1,x,moves+1])
            """if(o[str(mp.current_process())]==None):
                o[str(mp.current_process())] = []
            o[str(mp.current_process())].append(x.__name__)
            """
            p.start()
            processes.append(p)
if __name__ == '__main__':
    solve(R(cube),0,R,0)
    for p in processes:
      p.join()
    print(ender)
