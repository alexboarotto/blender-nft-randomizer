from email.policy import default
import bpy

from . data import Data


class FZRandomizerPanel(bpy.types.Panel):
    bl_idname = "SCENE_PT_FZ_Randomizer"
    bl_label = ""
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="FZ Randomizer")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.operator("fz.select_dir", text = "Import JSONs")

        layout.prop(scene, "CharacterCollection")

        layout.operator("fz.generate_animation", text="Generate Animation")

        layout.row()
        layout.row()

        layout.operator("fz.select_output_dir", text = "output directory")

        layout.operator("fz.render", text = "Render")


def register():
    bpy.utils.register_class(FZRandomizerPanel)
    bpy.types.Scene.CharacterCollection =  bpy.props.PointerProperty(type=bpy.types.Collection)


def unregister():
    bpy.utils.unregister_class(FZRandomizerPanel)
    del bpy.types.Scene.CharacterCollection

