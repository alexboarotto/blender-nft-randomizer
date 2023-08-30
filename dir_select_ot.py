import json
import os
import bpy
from bpy_extras.io_utils import ImportHelper

from . data import Data

class ImportDirectoryOT(bpy.types.Operator, ImportHelper):
    """Create render for all chracters"""
    bl_idname = "fz.select_dir"
    bl_label = "Select Directory"
    bl_options = {'REGISTER'}

    # Define this to tell 'fileselect_add' that we want a directoy
    directory: bpy.props.StringProperty(
        name="JSON Path",
        description="Select JSON directory",
        subtype='DIR_PATH'
    )

    def numerical_sort(self, value):
        try:
            num_part = int(value.split('.')[0])
            return num_part
        except ValueError:
            return float('inf') 

    def execute(self, context):
        # Get the list of filenames and sort them using the custom numerical_sort function
        sorted_filenames = sorted(os.listdir(self.directory), key=lambda x: self.numerical_sort(x))
        print(sorted_filenames)

        json_files = []

        for filename in sorted_filenames:
            if filename.endswith(".json"):
                filepath = os.path.join(self.directory, filename)
                try:
                    with open(filepath) as file:
                        data = json.load(file)
                        json_files.append(data)
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

        Data.data = json_files

        return {'FINISHED'}

def register():
    bpy.utils.register_class(ImportDirectoryOT)

def unregister():
    bpy.utils.unregister_class(ImportDirectoryOT)
