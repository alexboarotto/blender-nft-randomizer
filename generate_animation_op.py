import math
from time import sleep
import bpy
from bpy.types import Operator

from .data import Data


# Operation to create new interaction zone of the specified type
class GenerateAnimationOP(Operator):
    """Generate Animation"""
    bl_idname = "fz.generate_animation"
    bl_label = "Generate Animation"

    @classmethod
    def poll(self, context):
        return Data.data is not None
    
    def hide_collection(self, collection):
        for obj in bpy.data.collections[collection.name].all_objects[:]:
            obj.hide_render = True
            obj.hide_viewport = True
            obj.keyframe_insert("hide_viewport", frame=bpy.context.scene.frame_current)
            obj.keyframe_insert("hide_render", frame=bpy.context.scene.frame_current)

        for child_collection in collection.children:
            self.hide_collection(child_collection)

    def execute(self, context):
        # Clear animation data for each object
        for obj in bpy.data.objects:
            obj.animation_data_clear()


        # Access the value of the deferred property from the scene
        collection = context.scene.CharacterCollection if not context.scene.CharacterCollection is None else bpy.data.collections[0]
        # Do something with the collection
        if collection is not None:
            print("Selected collection:", collection.name)
        else:
            print("No collection selected")

        self.hide_collection(bpy.data.collections[collection.name])

        bpy.context.scene.frame_start = 0
        bpy.context.scene.frame_end = len(Data.data)-1
        bpy.context.scene.frame_current = 0

        for index, nft in enumerate(Data.data):
            bpy.context.scene.frame_current = index
            self.hide_collection(collection)
            for att in nft["attributes"]:
                obj_key = att["value"]
                obj = bpy.data.objects.get(obj_key, None)
                if obj is not None:
                    if index <= 0:
                        print(obj)
                    obj.hide_render = False
                    obj.hide_viewport = False
                    obj.keyframe_insert("hide_viewport", frame=bpy.context.scene.frame_current)
                    obj.keyframe_insert("hide_render", frame=bpy.context.scene.frame_current)
                else:
                    print(f"Object '{obj_key}' not found in bpy.data.objects.")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(GenerateAnimationOP)

def unregister():
    bpy.utils.unregister_class(GenerateAnimationOP)