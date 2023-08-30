from . import panel
from . import generate_animation_op
from . import dir_select_ot
from . import output_dir_select_ot
from . import render_op

bl_info = {
    "name": "FZ Randomizer",
    "blender": (3, 0, 0),
    "category": "Object",
    "support": "COMMUNITY",
}

def register():
    panel.register()
    generate_animation_op.register()
    dir_select_ot.register()
    output_dir_select_ot.register()
    render_op.register()

def unregister():
    panel.unregister()
    generate_animation_op.unregister()
    dir_select_ot.unregister()
    output_dir_select_ot.unregister()
    render_op.unregister()