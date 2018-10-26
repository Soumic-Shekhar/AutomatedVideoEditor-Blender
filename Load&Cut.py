import bpy, time
from ast import literal_eval as creatTuple

def frame(frame):
    return ( int(bpy.context.scene.render.fps)* int(frame) / 1000 ** 2)


def get_frame_markers():
    with open("/home/soumics/Desktop/Automate_Blender/BlenderVideoEdit(py)/a.txt", 'r') as infile:
        for line in infile:
            line = line.split()
            for l in line:
                frame_ms.append(creatTuple(l))


def cut_vid():
    for x in range(len(frame_ms)):
        bpy.ops.sequencer.cut(frame=int(frame(frame_ms[x][1])), type='SOFT', side='RIGHT')
        bpy.ops.sequencer.delete()
        bpy.ops.sequencer.select_active_side(side='LEFT') 
        bpy.ops.sequencer.cut(frame=int(frame(frame_ms[x][0])), type='SOFT', side='LEFT')
        if(x == len(frame_ms)-1):
            bpy.ops.sequencer.select_active_side(side='LEFT') 
            bpy.ops.sequencer.delete()

if __name__ == '__main__':
    print("init")
    bpy.context.area.type = 'SEQUENCE_EDITOR'
    bpy.ops.sequencer.movie_strip_add(filepath="//BlenderVideoEdit(py)/Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv", files=[{"name":"Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv", "name":"Nas Daily about the student movement in Bangladesh right Now 😰-xgqaOFRP0Qk.mkv"}], relative_path=True, show_multiview=False, frame_start=0, channel=1)
    frame_ms = []
    get_frame_markers()
    cut_vid()
    print('done')

