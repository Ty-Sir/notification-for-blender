import bpy
import aud

device = aud.Device()
completion_sound = aud.Sound('ENTER_FILE_PATH_TO_WAV_FILE_HERE')


def play_completion_sound(dummy):
    device.play(completion_sound)


bpy.app.handlers.render_complete.append(play_completion_sound)
