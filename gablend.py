import bpy
import random

def create_random_gaobject(name, maxdist=2):
    return GAObject(create_random_object(name, maxdist))

def create_random_object(name, maxdist=2):
    bpy.ops.mesh.primitive_uv_sphere_add()
    random_object = bpy.context.active_object
    randomize_object(random_object, maxdist)
    random_object.name = name
    return random_object

def randomize_object(obj, maxdist=2):
    for vert in obj.data.vertices:
        randomize_vertex(vert, maxdist)
    
def randomize_vertex(vert, maxdist=2):
    vert.co.x += random.uniform(-maxdist, maxdist)
    vert.co.y += random.uniform(-maxdist, maxdist)
    vert.co.z += random.uniform(-maxdist, maxdist)
    

def mutate(gaobj, maxdist=2):
    verts = gaobj.count_vertices()
    for vert in gaobj.obj.data.vertices:
        chance = random.randint(1, verts)
        if chance == verts:
            randomize_vertex(vert, maxdist)
    
class GAObject:
    def __init__(self, obj, ffval=0):
        self.obj = obj
        self.ffval = ffval
    def count_vertices(obj):
        count = 0
        for vert in obj.data.vertices:
            count += 1
        return count