import bpy
import random

randomize(shape, dist):
    for vert in shape.data.vertices:
        vert.co.x += random.randint(-dist,dist) 
        vert.co.y += random.randint(-dist,dist)
        vert.co.z += random.randint(-dist,dist)

create_random_object():
    bpy.ops.mesh.primitive_uv_sphere_add()
    randomize(bpy.data.objects["Sphere"], 2)
    
