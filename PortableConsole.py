bl_info = {
    "name": "PortableConsole",
    "author": "Spectral Vectors",
    "version": (0, 0, 1),
    "blender": (2, 90, 0),
    "location": "F3 > PortableConsole or Shift+Ctrl+Alt+P",
    "description": "A popup panel to run Python in any area or context",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}

import bpy


class PortableConsoleOperator(bpy.types.Operator):
    """A popup panel that lets you execute Python commands in any context"""

    bl_idname = "addon.portable_console"
    bl_label = "Execute Python Command"
    bl_property = 'Command'

    Command: bpy.props.StringProperty(
        name='Command:',
        description='The Python command you wish to execute',
        default='',
    )

    def execute(self, context):
        exec(self.Command)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        self.layout.prop(self, 'Command')


def register():
    bpy.utils.register_class(PortableConsoleOperator)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.user

    km = kc.keymaps.new(
        name="Window",
        space_type='EMPTY',
        region_type='WINDOW'
        )
    kmi = km.keymap_items.new(
        "addon.portable_console",
        'P',
        'PRESS',
        shift=True,
        ctrl=True,
        alt=True,
        )
    kmi.active = True


def unregister():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.user
    keymap = kc.keymaps['Window'].keymap_items

    for key in keymap:
        if (key.idname == "addon.portable_console"):
            keymap.remove(key)

    bpy.utils.unregister_class(PortableConsoleOperator)


if __name__ == "__main__":
    register()
