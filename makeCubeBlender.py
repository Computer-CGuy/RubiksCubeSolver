import bpy
from rcube import *
cube = np.zeros((12,9),np.int32)
cube = init(cube)
ob = bpy.data.objects["cube"]
print(ob.vertex_groups)
v = 0
# 1, 2, 3 ,4 ,5 ,6

arr =  [(0,0,0,1),
        (0,0.328,0.0625,1),
        (0.485,0,0,1),
        (0,0.060,0.418,1),
        (1,0.1,0,1),
        (1,0.665,0,1)]
for n in ob.vertex_groups:
    v+=1
    #print(n.name)
    bpy.ops.object.vertex_group_set_active(group=n.name)
    bpy.ops.object.vertex_group_select()
    x,y = n.name.split(" ")
    print(cube[int(x)][int(y)])
    mat = bpy.data.materials.new(name=n.name) 

    mat.diffuse_color = arr[cube[int(x)][int(y)]-1]
    ob.data.materials.append(mat)
    bpy.context.object.active_material_index = v  
    bpy.ops.object.material_slot_assign()
    bpy.ops.mesh.select_all(action='DESELECT')
print(v)
