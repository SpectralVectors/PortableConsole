import bpy

bl_info = {
    "name": "PortableConsole",
    "author": "Spectral Vectors",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "F3 > PortableConsole or Shift+Ctrl+Alt+P",
    "description": "A popup panel to run Python in any area or context",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}


class PortableConsoleProperties(bpy.types.PropertyGroup):

    Command: bpy.props.StringProperty(
        name='Command',
        description='The Python command you wish to execute',
        default='',
    )

    Print: bpy.props.StringProperty(
        name='print()',
        description='Prints the entered data to the console',
        default='',
    )

    Script: bpy.props.PointerProperty(
        type=bpy.types.Text
    )


class PortablePrintOperator(bpy.types.Operator):
    """Prints Data to the System Console"""

    bl_idname = "addon.portable_print"
    bl_label = "Print to System Console"

    def execute(self, context):
        props = context.scene.portable_console_properties
        exec(f"print({props.Print})")
        return {'FINISHED'}


class ExecuteCommandOperator(bpy.types.Operator):
    """Execute Python commands in any context"""

    bl_idname = "addon.execute_command"
    bl_label = "Execute Command"

    def execute(self, context):
        props = context.scene.portable_console_properties
        exec(props.Command)
        return {'FINISHED'}


class RunScriptOperator(bpy.types.Operator):
    """Runs the selected script in the current context"""

    bl_idname = "addon.run_script"
    bl_label = "Run Script"

    def execute(self, context):
        props = context.scene.portable_console_properties
        exec(props.Script.as_string())
        return {'FINISHED'}


class PortableConsoleOperator(bpy.types.Operator):
    """A popup panel that lets you execute Python commands in any context"""

    bl_idname = "addon.portable_console"
    bl_label = "Portable Python Console"

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        props = context.scene.portable_console_properties
        layout = self.layout
        box = layout.box()
        column = box.column()
        column.prop(props, 'Command')
        column.operator('addon.execute_command')
        box = layout.box()
        column = box.column()
        column.prop(props, 'Print')
        column.operator('addon.portable_print')
        box = layout.box()
        column = box.column()
        column.prop_search(props, 'Script', bpy.data, 'texts', text='Script')
        column.operator('addon.run_script')


classes = [
    PortableConsoleProperties,
    PortablePrintOperator,
    ExecuteCommandOperator,
    PortableConsoleOperator,
    RunScriptOperator,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.user

    km = kc.keymaps['Window']
    kmi = km.keymap_items.new(
        "addon.portable_console",
        'P',
        'PRESS',
        shift=True,
        ctrl=True,
        alt=True,
    )
    kmi.active = True

    bpy.types.Scene.portable_console_properties = bpy.props.PointerProperty(
        type=PortableConsoleProperties
    )


def unregister():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.user
    keymap = kc.keymaps['Window'].keymap_items

    for key in keymap:
        if (key.idname == "addon.portable_console"):
            keymap.remove(key)

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
