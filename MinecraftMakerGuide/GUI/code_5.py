# import libraries
from appJar import gui
from mcpi.minecraft import Minecraft

# connect to Minecraft
mc = Minecraft.create()

# 1 - CHAT FUNCTION
def sendChat(btn):
    msg = app.getEntry("Chat")
    mc.postToChat(msg)

# 2 - MOVEMENT FUNCTION
def move(btn):
    x, y, z = mc.player.getPos()
    if btn == "LEFT":
        x -= 1
    elif btn == "RIGHT":
        x += 1
    elif btn == "FORWARD":
        z -= 1
    elif btn == "BACKWARD":
        z += 1
    elif btn == "JUMP":
        y += 1
        z -= 1 

    mc.player.setPos(x, y, z)

# 3 - STATUS FUNCTION
def updateStatus():
    x, y, z = mc.player.getPos()
    app.setStatusbar("X: " + str(x), field=0)
    app.setStatusbar("Y: " + str(y), field=1)
    app.setStatusbar("Z: " + str(z), field=2)

# 4 - BLOCKS FUNCTION
BLOCKS = {"Stone": 1, "TNT": 46, "Torch": 50, "Diamond": 57}
def drop(btn):
    x, y, z = mc.player.getPos()
    z = z - 1
    height = mc.getHeight(x,z)

    playerBlock = app.getOptionBox("Block")
    blockId = BLOCKS[playerBlock]

    mc.setBlock(x, height, z, blockId)

# 5 - MENU FUNCTION
def clickMenu(choice):
    if choice == "Create":
        mc.saveCheckpoint()
        app.infoBox("Save", "Checkpoint saved.")
    elif choice == "Restore":
        if app.yesNoBox("Restore", "Are you sure? All changes will be lost!"):
            mc.restoreCheckpoint()
    elif choice == "Normal":
        mc.camera.setNormal()
    elif choice == "Fixed":
        mc.camera.setFixed()
    elif choice == "Follow":
        mc.camera.setFollow()

# create the GUI - must come first
app = gui("appJar Minecraft")
app.setLocation(100,100)

# 1 - CHAT WIDGETS
app.addLabelEntry("Chat", row=0, column=0)
app.addButton("Send", sendChat, row=0, column=1)

# 2 - MOVEMENT WIDGETS
app.startLabelFrame("Movement", row=1, column=0, colspan=2)
app.setSticky("NESW") # make buttons stick to all sides
app.addButton("FORWARD", move, row=0, column=1)
app.addButton("LEFT", move, row=1, column=0)
app.addButton("JUMP", move, row=1, column=1)
app.addButton("RIGHT", move, row=1, column=2)
app.addButton("BACKWARD", move, row=2, column=1)
app.stopLabelFrame()

# 3 - STATUS WIDGETS
app.addStatusbar(fields=3)
app.registerEvent(updateStatus) # call updateStatus in a loop

# 4 - BLOCKS WIDGETS
app.addLabelOptionBox("Block", list(BLOCKS), row=2, column=0)
app.addButton("Drop", drop, row=2, column=1)

# 5 - MENU WIDGETS
app.addMenuList("Checkpoint", ["Create", "Restore"], clickMenu)
app.addMenuList("Camera", ["Normal", "Fixed", "Follow"], clickMenu)

# start the GUI - must come last
app.go()
