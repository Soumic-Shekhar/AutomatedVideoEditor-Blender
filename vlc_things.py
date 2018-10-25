from os import path
import vlc
from pynput.keyboard import Key, Listener, KeyCode
from tkinter import filedialog
from tkinter import *

# Open a system dialog box to select a video file
root = Tk()
root.filename =  filedialog.askopenfilename(title = "Select video file")
print (root.filename)

# Assign the file location to a variable
video_file = root.filename

# Open a text file in write mode to record data
notepad = open("{0}.txt".format(video_file), "w")

# Clean up the dialog box 
root.destroy()


# Define listener functions

# on_press works even when held down
def on_press(key):
    print('{0} pressed'.format(key))

    if key == Key.right:
        t = vlc.libvlc_media_player_get_time(player)
        vlc.libvlc_media_player_set_time(player, t+5000)
        
    if key == Key.left:
        t = vlc.libvlc_media_player_get_time(player)
        vlc.libvlc_media_player_set_time(player, t-5000)

# Make the media player
player = vlc.MediaPlayer(video_file)

# on_press works only when a key is released      
def on_release(key):
    print('{0} release'.format(key))
    if key == Key.space:
        player.pause()

    # for alphanumeric keys use KeyCode as shown below
    if key == KeyCode.from_char("a"):
        t = vlc.libvlc_media_player_get_time(player)
        notepad.write("'{0}',".format(t))

    if key == KeyCode.from_char("d"):
        t = vlc.libvlc_media_player_get_time(player)
        notepad.write("'{0}'\n".format(t))
        
    if key == Key.esc:
        # Stop listener
        player.stop()
        notepad.close()
        return False

# Start the video
player.play()

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

