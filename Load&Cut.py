#AUTOMATE ===> Blender in LINUX Author@ Soumic Shekhar

import bpy
from ast import literal_eval as creatTuple

VidfilePath = "//Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv" # -> Enter Video file $PATH Here
TxtfilePath = "/home/soumics/Desktop/Automate_Blender/BlenderVideoEdit(py)/a.txt" # -> Enter marker file $PATH Here

marked_frames = []

def detect_fps_Format(fps): # -> get fps format from blender
    length = len(str((fps)))
    # print(length) 
    if (length <= 3 ):
        return (fps * 1000)
    return fps

def frame_length(start, end):
    return (end - start)    


def frame(frame): # -> Gets Frame Number

    # print(frame) # -> debug
    # print(bpy.context.scene.render.fps) # -> debug
    return int (( detect_fps_Format (bpy.context.scene.render.fps) * int(frame)) / 1000 ** 2)


def get_frame_markers(file): # -> Reads the marker txt file and creates a tuple from it [NB. Format Specific]

    with open(file, 'r') as infile: # -> Loads Marker file

        for line in infile:

            line = line.split()

            for l in line:

                marked_frames.append(creatTuple(l))


def Edit_vid(): # -> Cuts Video at specific marked points

    for x in range((len(marked_frames) - 1), -1, -1): # -> Decriments through the Tuple

        # Innificient
        bpy.ops.sequencer.cut(frame=frame(marked_frames[x][1]), type='SOFT', side='RIGHT')
        bpy.ops.sequencer.delete()
        bpy.ops.sequencer.select_active_side(side='LEFT') 
        bpy.ops.sequencer.cut(frame=frame(marked_frames[x][0]), type='SOFT', side='LEFT')
    
    # Delete the last Snip
    bpy.ops.sequencer.select_active_side(side='LEFT') 
    bpy.ops.sequencer.delete()
    # print (bpy.context.sequences) # -> debug

    bpy.context.sequences[-1].select = True # -> select the audio file
    bpy.ops.sequencer.delete()

    push_to_frame_zer0()

    
def push_to_frame_zer0(): # -> Aligns all the video to start from frame 0

    bpy.context.sequences[0].select = 1 # -> selects clip closest to frame 0
    bpy.ops.sequencer.snap(frame = 0) # -> moves it to frame zero
    bpy.context.sequences[-1].select = 0 # -> deslects it [NB. clip indexes swaps after very operations]

    bpy.ops.sequencer.gap_remove(all=True) # -> removes all intermediate gaps 


if __name__ == '__main__':

    # EDIT SEQUNECE
    print(">>>>>>>>>init<<<<<<<<<")

    bpy.context.area.type = 'SEQUENCE_EDITOR' # -> Invokes Sequence Editor
    bpy.ops.sequencer.movie_strip_add(filepath=VidfilePath, show_multiview=False, frame_start=0, channel=1) # -> Loads Video file

    get_frame_markers(TxtfilePath) # -> loads maker file
    
    Edit_vid()

    print('>>>>>>>>>done<<<<<<<<<')

