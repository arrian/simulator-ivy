# from maya import cmds
# from maya import mel
# from maya import OpenMayaUI as omui 
# from PySide.QtCore import * 
# from PySide.QtGui import * 
# from shiboken import wrapInstance 

# mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
# mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Plane():
    def __init__(self, position = Vector(0,0,0), normal = Vector(0,1.0,0)):
        self.position = position
        self.normal = normal

class Light():
    def __init__(self, position = Vector(0,10.0,0), strength = 1.0):
        self.position = position
        self.strength = strength



class PlantNode():
    def __init__(self):
        self.children = []

class PlantKeyframe():
    def __init__(self):
        self.nodes = []
        self.leaf_nodes = []
        self.growth_nodes = []

    def get_mesh(self, progress = 0.0, next_keyframe = None):
        pass

    def grow(self):
        pass

class Plant():
    def __init__(self, growth_speed = 1.0, complexity = 1.0, scale = 1.0):
        self.keyframes = []
        self.keyframe_growth = 0.0
        self.obstacles = []
        self.lights = []

    def get_growth(self):
        return len(self.keyframes) + self.keyframe_growth

    def get_mesh(self, step = None):
        if step is None:
            step = self.get_growth()

        index = int(step / 1.0)
        progress = step % 1.0
        keyframe = self.keyframes[index]
        next_keyframe = self.keyframes[index + 1] if len(self.keyframes) >= index else None

        return keyframe.get_mesh(progress, next_keyframe)

    def grow(self, size = 0.1):
        pass

    def raycast(self, position, normal):
        pass

# class Ivy(QWidget):
#     def __init__(self, *args, **kwargs):
#         super(Ivy, self).__init__(*args, **kwargs)
#         self.setParent(mayaMainWindow)
#         self.setWindowFlags(Qt.Window)
#         self.setObjectName('Ivy_uniqueId')
#         self.setWindowTitle('Create polygon')
#         self.setGeometry(50, 50, 250, 150)
#         self.initUI()
#         self.cmd = 'polyCone'
        
#     def initUI(self):
#         self.combo = QComboBox(self)
#         self.combo.addItem( 'Cone' )
#         self.combo.addItem( 'Cube' )
#         self.combo.addItem( 'Sphere' )
#         self.combo.addItem( 'Torus' )
#         self.combo.setCurrentIndex(0)
#         self.combo.move(20, 20)
#         self.combo.activated[str].connect(self.combo_onActivated)

#         self.button = QPushButton('Create', self)
#         self.button.move(20, 50)
#         self.button.clicked.connect(self.button_onClicked)
        
        
#     def combo_onActivated(self, text):
#         self.cmd = 'poly' + text + '()'
        
#     def button_onClicked(self):
#         mel.eval( self.cmd )
            
# def main():
#     ui = Ivy()
#     ui.show()
#     return ui
    
# if __name__ == '__main__':
#     main()


import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginCmdName = "spHelloWorld"

# Command
class scriptedCommand(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)
        
    # Invoked when the command is run.
    def doIt(self,argList):
        print "Hello World!"

# Creator
def cmdCreator():
    return OpenMayaMPx.asMPxPtr( scriptedCommand() )
    
# Initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, '7 Simplex', '0.1.0')
    try:
        print(dir(mplugin))
        mplugin.registerCommand( kPluginCmdName, cmdCreator )
    except:
        sys.stderr.write( "Failed to register command: %s\n" % kPluginCmdName )
        raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand( kPluginCmdName )
    except:
        sys.stderr.write( "Failed to unregister command: %s\n" % kPluginCmdName )