import bpy
from bpy_extras.io_utils import ImportHelper

from .data import Data


class ExportDirectoryOT(bpy.types.Operator, ImportHelper):

    """Create render for all chracters"""
    bl_idname = "fz.select_output_dir"
    bl_label = "Select Directory"
    bl_options = {'REGISTER'}

    # Define this to tell 'fileselect_add' that we want a directoy
    directory: bpy.props.StringProperty(
        name="Output Path",
        description="Select output directory",
        subtype='DIR_PATH'
        )

    def execute(self, context):

        Data.output_dir = self.directory

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportDirectoryOT)


def unregister():
    bpy.utils.unregister_class(ExportDirectoryOT)
