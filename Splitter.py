import imageio
imageio.plugins.ffmpeg.download()
from tkinter import *
import csv
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfilename
from tkinter.messagebox import showerror
from tkinter.ttk import Progressbar
import threading



def movieMerger():

    videoPath = entry_videoPath.get()
    csvPath = entry_csvPath.get()
    outputPath = entry_outputPath.get()
    progressLabelMessage.set(outputPath)

    if videoPath == "" or csvPath == "":
        progressLabelMessage.set("Please Enter Valid File Path!")
        processButton['state'] = 'normal'
        return
    if outputPath == "" or outputPath == ".mp4":
        outputPath = videoPath+"_output.mp4"
        entry_outputPath.delete(0, END)
        entry_outputPath.insert(0, outputPath)

    progress.place(relx=0.5, rely=.8, anchor="c")
    progress.start()

    video= VideoFileClip(videoPath)

    clipsArray = []

    with open(csvPath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            startTime = float(row[0])
            endTime = float(row[1])
            clip = video.subclip(startTime, endTime)
            clipsArray.append(clip)

    final_clip = concatenate_videoclips(clipsArray)
    #final_clip.write_videofile(outputPath, fps=5, audio=False)
    final_clip.write_videofile(outputPath, audio=False)

    progress.stop()
    progress.place_forget()
    progressLabelMessage.set("Complete!")
    processButton['state'] = 'normal'


def real_time_merger():
    processButton['state'] = 'disabled'
    threading.Thread(target=movieMerger).start()


# csvPath = 'hello.csv'
# videoPath = 'E:\movie.avi'
#
# movieMerger(csvPath, videoPath)
def hello():
    mydir = asksaveasfilename( title="Select file", filetypes=(("mp4 files", ".mp4"), ("all files", ".*")))

    print(mydir)


def load_file(Type):
    progressLabelMessage.set("")
    fname = askopenfilename(filetypes=(("Expected files", ".mp4;*.avi;*.csv"),
                                       #("HTML files", ".html;.htm"),
                                       ("All files", ".")))

    if fname:
        try:
            if Type == 'csv':
                entry_csvPath.delete(0, END)
                entry_csvPath.insert(0, fname)
            elif Type == 'video':
                entry_videoPath.delete(0, END)
                entry_videoPath.insert(0, fname)

        except:                     # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return


def save_file_loc():
    progressLabelMessage.set("")
    mydir = asksaveasfilename(initialdir="/", title="Select file",
                              filetypes=(("mp4 files", ".mp4"), ("all files", ".*")))

    entry_outputPath.delete(0, END)
    entry_outputPath.insert(0, mydir+'.mp4')


root = Tk()
root.title('Pi Labs Surveillance')
root.geometry("900x450")
root.configure(background='DeepSkyBlue2')


# root.progressbar.place(relx=.5, rely=.5, anchor="c")
label_videoPath = Label(root, text="Video Path", bg="DeepSkyBlue2", font=("Consolas", 18))
label_csvPath = Label(root, text="CSV Path", bg= "DeepSkyBlue2", font=("Consolas", 18))
label_OutputPath = Label(root, text="Output", bg= "DeepSkyBlue2", font=("Consolas", 18))

button_load_videoPath = Button(root, text="load", font=("Consolas", 10), command=lambda: load_file('video'))
button_load_csvPath = Button(root, text="load", font=("Consolas", 10), command=lambda: load_file('csv'))
button_output_path = Button(root, text="load", font=("Consolas", 10), command=save_file_loc)

entry_videoPath = Entry(root, font=("Consolas", 15))
entry_csvPath = Entry(root, font=("Consolas", 15))
entry_outputPath = Entry(root, font=("Consolas", 15))

label_videoPath.place(relx=.33, rely=.1, anchor="c")
label_csvPath.place(relx=.34, rely=.2, anchor="c")
label_OutputPath.place(relx=.35, rely=.3, anchor="c")

entry_videoPath.place(relx=.53, rely=.1, anchor="c")
entry_csvPath.place(relx=.53, rely=.2, anchor="c")
entry_outputPath.place(relx=.53, rely=.3, anchor="c")

button_load_videoPath.place(relx=.69, rely=.1, anchor="c")
button_load_csvPath.place(relx=.69, rely=.2, anchor="c")
button_output_path.place(relx=.69, rely=.3, anchor="c")

processButton = Button(root, text="Process", font=("Consolas", 18), command=real_time_merger)
processButton.place(relx=0.5, rely=.5, anchor="c")

progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='indeterminate')

message = StringVar()
statusMessage = StringVar()
message.set("Pi Labs Bangladesh Ltd. ")
statusBottom = Label(root, bg="white", textvariable=message, bd=1, relief=SUNKEN, anchor=E, font=("Consolas", 10))
statusBottom.pack(side=BOTTOM, fill=X)

progressLabelMessage = StringVar()
progressLabelMessage.set("")
progressLabel = Label(root, textvariable=progressLabelMessage, bg="DeepSkyBlue2", font=("Consolas", 22))
progressLabel.place(relx=0.5, rely=.7, anchor="c")


root.mainloop()