from pythonosc import osc_message_builder
from pythonosc import udp_client
from mcpi.minecraft import Minecraft
from time import sleep

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
mc = Minecraft.create()

player_x, player_y, player_z  = mc.player.getTilePos()

def bulldozer(x, y, z):
    mc.setBlocks(x - 30, y - 3, z - 30, x + 30, y + 20, z + 30, 0)
	
def black_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 1, y - 1, z + 8, 49)

def white_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44, 7)
	
def make_octave(x, y, z):
    for i in range(0, 19, 3):
        white_key(player_x + i, player_y, player_z)
    for i in range(2, 18, 3):
        if i != 8:
            black_key(player_x + i, player_y, player_z)

def play_note(note):
    sender.send_message('/play_this', note)
    sleep(0.5)
	
bulldozer(player_x, player_y, player_z)
make_octave(player_x, player_y, player_z)
mc.player.setPos(player_x + 8, player_y + 3, player_z + 12)

while True:
    new_x, new_y, new_z = mc.player.getTilePos()
	block_below = mc.getBlock(new_x, new_y - 1, new_z)
    if block_below != 44 and block_below != 49:
        block_below = mc.getBlock(new_x, new_y, new_z)
	relative_position = player_x - new_x
	white_notes = [60, 62, 64, 65, 67, 69, 71]
    black_notes = [61, 63, 0,  66, 68, 70]
	if block_below == 44:
        notes_along = relative_position // -3
        play_note(white_notes[notes_along])
	 if block_below == 49:
        notes_along = ((relative_position - 1) // -3) - 1 
        play_note(black_notes[notes_along])
	