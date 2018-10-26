#AUTOMATE ===> Blender in LINUX Author@ Soumic Shekhar

import bpy
from ast import literal_eval as creatTuple

VidfilePath = "//Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv" # -> Enter Video file $PATH Here
TxtfilePath = "/home/soumics/Desktop/Automate_Blender/BlenderVideoEdit(py)/a.txt" # -> Enter marker file $PATH Here

def frame(frame): # -> Gets Frame Number
    return ( int(bpy.context.scene.render.fps)* int(frame) / 1000 ** 2)


def get_frame_markers(file): # -> Reads the marker txt file and creates a tuple from it [NB. Format Specific]
    with open(file, 'r') as infile: # -> Loads Marker file
        for line in infile:
            line = line.split()
            for l in line:
                frame_ms.append(creatTuple(l))


def cut_vid(): # -> Cuts Video at specific marked points
    for x in range(len(frame_ms)):
        bpy.ops.sequencer.cut(frame=frame(frame_ms[x][1]), type='SOFT', side='RIGHT')
        bpy.ops.sequencer.delete()
        bpy.ops.sequencer.select_active_side(side='LEFT') 
        bpy.ops.sequencer.cut(frame=frame(frame_ms[x][0]), type='SOFT', side='LEFT')
        if(x == len(frame_ms)-1):
            bpy.ops.sequencer.select_active_side(side='LEFT') 
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

