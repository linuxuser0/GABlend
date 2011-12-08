import bpy
import random

def create_random_gaobject(name, dist=2):
    return GAObject(create_random_object(name, dist))

def create_random_object(name, dist=2):
    bpy.ops.mesh.primitive_uv_sphere_add()
    random_object = bpy.context.active_object
    randomize_object(random_object, dist)
    random_object.name = name
    return random_object

def randomize_object(shape, dist=2):
    for vert in shape.data.vertices:
        randomize_vertex(vert, dist)
    
def randomize_vertex(vert, dist=2):
    vert.co.x += random.uniform(-dist, dist)
    vert.co.y += random.uniform(-dist, dist)
    vert.co.z += random.uniform(-dist, dist)
    

def mutate(obj, dist=2):
    verts = count_vertices(obj)
    for vert in obj.data.vertices:
        chance = random.randint(1, verts)
        if chance == verts:
            randomize_vertex(vert, dist)
            
def count_vertices(obj):
    count = 0
    for vert in obj.data.vertices:
        count += 1
    return count
    
class GAObject:
    def __init__(self, obj, ffval=0):
        self.obj = obj
        self.ffval = ffval
    def set_ffval(ffval):
        this.ffval=ffval
    def set_obj(obj):
        self.obj=obj
    def get_ffval():
        return ffval
    def get_obj():
        return obj
    
    