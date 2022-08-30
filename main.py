import pysstv.color
import pydub
import PIL.Image
from PIL import ImageTk

import tkinter as tk
from tkinter import filedialog

print("*******************************************")
imagePath = r"C:\Users\worwagp\PycharmProjects\SSTV\test.png" ## 320x256 - Scottie1
noImagePath = r"C:\Users\worwagp\PycharmProjects\SSTV\NoIMG.png" ## 320x256 - Scottie1
# imagePath = r"C:\Users\worwagp\PycharmProjects\SSTV\wrong_2.png" ## 320x256 - Scottie1
outputWAVPath = r"C:\Users\worwagp\PycharmProjects\SSTV\output.wav"
outputMP3Path = r"C:\Users\worwagp\PycharmProjects\SSTV\output.mp3"

samplingRate = 48000
bits = 16


imageObject = None
noImageObject = PIL.Image.open(noImagePath)


print("*******************************************")
mainWindow = tk.Tk()
mainWindow.title("SSTV ScottieS1 .mp3 generator")
mainWindow.geometry("600x600")


noImg = ImageTk.PhotoImage(image=noImageObject)
previewLabel = tk.Label(mainWindow, text='Image preview', image=noImg)
previewLabel.pack()
# show.config(image=tkimg)

def AskForImageFile():
    global imageObject
    # global previewLabel

    filePath = tk.filedialog.askopenfilename(initialdir="", title="Select .png file", filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
    imageObject = PIL.Image.open(filePath)

    isOK = True
    isOK &= imageObject.width == 320
    isOK &= imageObject.height == 256

    if isOK:
        preview = ImageTk.PhotoImage(image=imageObject)
        # previewLabel.config(image=preview)
        previewLabel = tk.Label(mainWindow, text='Image preview', image=preview)
        previewLabel.pack()

        SSTV = pysstv.color.ScottieS1(imageObject, samplingRate, bits)
        # SSTV.write_wav(outputWAVPath)

        # sound = pydub.AudioSegment.from_wav(outputWAVPath)
        # sound.export("abc.mp3", format="mp3") # probably due to lack of LAME codec
    else:
        print(f"ERROR: Incorrect image size - Image should has 320 pixels width (current file width: {imageObject.width}) and 256 pixels height (current file height: {imageObject.height})")

    #
loadImageButton = tk.Button(mainWindow, text="Select All", width=12,height=2, command=AskForImageFile)
loadImageButton.pack()




mainWindow.mainloop()