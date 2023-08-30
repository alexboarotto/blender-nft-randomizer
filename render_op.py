
import bpy
from bpy.types import Operator
from bpy.props import StringProperty

from .data import Data

class Render_OT(Operator):
    """Render"""
    bl_idname = 'fz.render'
    bl_label = 'Render images'
    
    @classmethod
    def poll(self, context):
        return Data.output_dir is not ''
    
 
    def execute(self, context):
        scene = context.scene

        bpy.context.scene.frame_current = 0

        # Set the render settings
        scene.render.image_settings.file_format = 'PNG'
        scene.render.filepath = Data.output_dir  # Output file path

        # Render the scene
        bpy.ops.render.render(write_still=True, animation=True)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(Render_OT)

def unregister():
    bpy.utils.unregister_class(Render_OT)