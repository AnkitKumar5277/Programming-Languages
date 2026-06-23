import moviepy.editor # import karo moviepy.editor for video to audio ko convert karne k liye
from tkinter.filedialog import * # gui k liye dialog box open hoga

path = askopenfilename() # video ka path dhundo
select = moviepy.editor.VideoFileClip(path) # video ko select karo
covert = select.audio # .audio convert kardega

convert.write_audiofile("saved.mp3") # audio convert karne k liye
print("audio converted successfully ! ")
