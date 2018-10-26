import bpy, time
from ast import literal_eval as creatTuple

print("init")
bpy.context.area.type = 'SEQUENCE_EDITOR'
bpy.ops.sequencer.movie_strip_add(filepath="//Tests/Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv", files=[{"name":"Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv", "name":"Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv"}], relative_path=True, show_multiview=False, frame_start=0, channel=1)



frame = []
def get_frame_markers():
    with open("/home/soumics/Desktop/Automate_Blender/Tests/a.txt", 'r') as infile:
        for line in infile:
            line = line.split()
            for l in line:
                frame.append(creatTuple(l))



def cut_vid():
    for x in range(len(frame)):
        bpy.ops.sequencer.cut(frame=int(frame[x][1]), type='SOFT', side='RIGHT')
        print(int(frame[x][1]))
        bpy.ops.sequencer.delete()
        bpy.ops.sequencer.select_active_side(side='LEFT') 
        bpy.ops.sequencer.cut(frame=int(frame[x][0]), type='SOFT', side='LEFT')
        print(int(frame[x][0]))
        if(x == len(frame)-1):
            bpy.ops.sequencer.select_active_side(side='LEFT') 
            bpy.ops.sequencer.delete()

get_frame_markers()
cut_vid()
print('done')
