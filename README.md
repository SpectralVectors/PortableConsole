![PortableConsole](/PortableConsole.png)
# PortableConsole
A popup panel that lets you execute Python commands in any context or area in Blender

## How It Works
F3 search for PortableConsole, or use the built-in shortcut Shift+Ctrl+Alt+P.

This opens a panel in whatever context your cursor inhabits where you can type or paste Python code.

## Why Make This
Every Blender Addon developer at some point encounters a context error while developing a script.

There are a few ways to get around these errors, but I've found that they're a little overkill when I want to test a small part of a larger script/addon.

_e.g. you may wish to break down part of your node-based addon and just test the node-linking logic, perhaps a small part of a larger macro is broken and you want to take it step-by-step within Blender, or maybe you don't feel like writing out the overrides and area switching..._

This was a handy way for me to be able to test scripts from object creation, mesh editing, custom nodes, USB serial communication etc. without using an IDE or debugging tools.

If you can run it in the Text Editor or the Python Console, then you can run it in the PortableConsole!
