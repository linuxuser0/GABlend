import bpy
import random

def randomize(shape, dist):
    for vert in shape.data.vertices:
        vert.co.x += random.randint(-dist,dist) 
        vert.co.y += random.randint(-dist,dist)
        vert.co.z += random.randint(-dist,dist)

def create_random_object(name, dist):
    bpy.ops.mesh.primitive_uv_sphere_add()
    random_object = bpy.context.active_object
    randomize(random_object, dist)
    random_object.name = name
    return random_object
    