#AUTOMATE ===> Blender in LINUX Author@ Soumic Shekhar

import bpy
from ast import literal_eval as creatTuple

VidfilePath = "//Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv" # -> Enter Video file $PATH Here
TxtfilePath = "/home/soumics/Desktop/Automate_Blender/BlenderVideoEdit(py)/a.txt" # -> Enter marker file $PATH Here

def detect_fps_Format(fps): # -> get fps format from blender
    length = len(str((fps)))
    # print(length) 
    if (length <= 3 ):
        return (fps * 1000)
    return fps
        

def frame(frame): # -> Gets Frame Number

    print(frame)
    print(bpy.context.scene.render.fps)
    return int (( detect_fps_Format (bpy.context.scene.render.fps) * int(frame)) / 1000 ** 2)


def get_frame_markers(file): # -> Reads the marker txt file and creates a tuple from it [NB. Format Specific]

    with open(file, 'r') as infile: # -> Loads Marker file

        for line in infile:

            line = line.split()

            for l in line:

                frame_ms.append(creatTuple(l))


def cut_vid(): # -> Cuts Video at specific marked points

    for x in range((len(frame_ms) - 1), -1, -1): # -> Decriments through the Tuple

        bpy.ops.sequencer.cut(frame=frame(frame_ms[x][1]), type='SOFT', side='RIGHT')
        bpy.ops.sequencer.delete()
        bpy.ops.sequencer.select_active_side(side='LEFT') 
        bpy.ops.sequencer.cut(frame=frame(frame_ms[x][0]), type='SOFT', side='LEFT')

        #print(frame(frame_ms[x][1])) # -> debug
        #print(frame(frame_ms[x][0])) # -> debug
    
    # Delete the last Snip
    bpy.ops.sequencer.select_active_side(side='LEFT') 
    bpy.ops.sequencer.delete()
    # print (bpy.context.sequences) # -> debug

    bpy.context.sequences[4].select = True # -> select the audio file
    bpy.ops.sequencer.delete()


    

if __name__ == '__main__':

    # EDIT SEQUNECE
    print(">>>>>>>>>init<<<<<<<<<")

    bpy.context.area.type = 'SEQUENCE_EDITOR' # -> Invokes Sequence Editor
    bpy.ops.sequencer.movie_strip_add(filepath=VidfilePath, show_multiview=False, frame_start=0, channel=1) # -> Loads Video file

    frame_ms = []
    get_frame_markers(TxtfilePath)
    
    cut_vid()

    print('>>>>>>>>>done<<<<<<<<<')

