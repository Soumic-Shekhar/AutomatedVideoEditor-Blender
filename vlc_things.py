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

# Clean up the dialog box 
root.destroy()

# Open a text file with the same name in write mode to record data
notepad = open("{0}.txt".format(video_file[:video_file.index('.')]), "w")

# Make the media player
player = vlc.MediaPlayer(video_file)

# Define listener functions

# on_press is called even when held down
def on_press(key):
    
    if key == Key.right:
        t = player.get_time()
        player.set_time(t + 5000)
        
    if key == Key.left:
        t = player.get_time()
        player.set_time(t - 5000)

# on_release is only called when the button is released after pressing
def on_release(key):
    
    if key == Key.space:
        player.pause()

    # for alphanumeric keys use KeyCode as shown below
    if key == KeyCode.from_char("a"):
        t = vlc.libvlc_media_player_get_time(player)
        print("start - {0}".format(t))
        notepad.write("'{0}',".format(t))

    if key == KeyCode.from_char("d"):
        t = vlc.libvlc_media_player_get_time(player)
        print("end - {0}".format(t))
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
