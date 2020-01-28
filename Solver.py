import asyncio
import multiprocessing as mp
from multiprocessing import Process
from Rubiks_cube import *
# R , L , D , U , F ,B
cube = np.zeros((12,9),np.int32)
a = [R,L,D,U,F,B]
solved = False
check = np.copy(init(cube))
layers = 0
ans = []
saver = True
#@asyncio.coroutine
def solve(cube,last,nl):
    global solved,a,check,saver,ans
    if(np.array_equal(cube,check)):
        print(cube)
        solved = True
        for p in ans:
            p.terminate()
        return 1
    if not solved:
        processes = []
        for x in a:
            #print(x(cube))
            if(x==last):
                if(nl>2):
                    
                    continue
                processes.append(mp.Process(target=solve,args=([x(cube),x,nl+1])))
            else:
                processes.append(mp.Process(target=solve,args=([x(cube),x,1])))
            #print(processes)
            if saver:
                ans = processes
                saver = False
        for p in processes:
            p.start()
        # Exit the completed processes
        for p in processes:
            p.join()
    else:
        return 0
if __name__ == '__main__':
    cube  = init(cube)
    print(solve(R(cube),R,0))
#def get():
#    return await asyncio.gather(solve(R(cube)))
#loop = asyncio.get_event_loop()
# = (await asyncio.gather(solve(U(cube))))

#print(asyncio.run(solve(solve(F(cube)))))
