import bpy
import random

def create_random_object(name, dist):
    bpy.ops.mesh.primitive_uv_sphere_add()
    random_object = bpy.context.active_object
    randomize_object(random_object, dist)
    random_object.name = name
    return random_object

def randomize_object(shape, dist):
    for vert in shape.data.vertices:
        randomize_vertex(vert, dist)
    
def randomize_vertex(vert, dist):
    vert.co.x += random.uniform(-dist, dist)
    vert.co.y += random.uniform(-dist, dist)
    vert.co.z += random.uniform(-dist, dist)
    

def mutate(obj, dist):
    verts = count_vertices(obj)
    for vert in obj.data.vertices:
        chance = random.randint(1, verts)
        if chance == verts:
            randomize_vertex(vert, dist)
            
