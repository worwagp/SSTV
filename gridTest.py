import PIL.Image
from PIL import ImageTk

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


########################## Variables ##########################
filePath = ""

########################## Functions ##########################
def AskForImageFile():
    global modeVar
    global SSTV_Modes

    filePath = tk.filedialog.askopenfilename(initialdir="", title="Select .png file", filetypes=(("PNG files", "*.png"), ("all files", "*.*")))

    selectedMode = modeVar.get()
    print("*********** FILE LOADED ***********")
    print(f"Selected mode: {selectedMode}")

    expectedWidth = SSTV_Modes[selectedMode]["width"]
    expectedHeight = SSTV_Modes[selectedMode]["height"]

    print(f"Expected image size: {expectedWidth}x{expectedHeight}px")

    imageObject = PIL.Image.open(filePath)
    print(f"Received image size: {imageObject.width}x{imageObject.height}px")

    if imageObject.width == expectedWidth and imageObject.height == expectedHeight:
        print("OK: Image size is matching with selected SSTV mode")
    else:
        print("NOK: Image size not matching with selected SSTV mode")

########################## TKInter ##########################
mainWindow = tk.Tk()

mainWindow.title("SSTV MP3 Generator")
mainWindow.geometry("600x600")
# mainWindow.resizable(0, 0)


for each in range(20):
    weight = 5
    mainWindow.columnconfigure(each, weight=weight)

for each in range(150):
    mainWindow.rowconfigure(each, weight=1)


SSTV_Modes = {"Martin1": {"width": 320, "height": 256},
              "Martin2": {"width": 160, "height": 256},
              "Martin3": {"width": 320, "height": 128},
              "Martin4": {"width": 160, "height": 128},
              "Scottie1": {"width": 320, "height": 256},
              "Scottie2": {"width": 320, "height": 128},
              "Scottie3": {"width": 320, "height": 128},
              "Scottie4": {"width": 160, "height": 128},
              "Robot8": {"width": 160, "height": 120},
              "Robot12": {"width": 320, "height": 120},
              "Robot24": {"width": 320, "height": 240},
              "Robot36": {"width": 320, "height": 240}}



modeLabel = tk.Label(mainWindow, text="SSTV Mode", font="Arial 10 bold")
modeLabel.grid(column=0, row=0, sticky=tk.W, padx=5)

modeVar = tk.StringVar()
modeVar.set("Martin1")
for index, SSTV_Mode in enumerate(SSTV_Modes.keys()):
    radioButton = tk.Radiobutton(mainWindow, text=SSTV_Mode, variable=modeVar, value=SSTV_Mode)
    radioButton.grid(column=0, row=1+index, sticky=tk.NW, padx=10)


modeSeparator = ttk.Separator(mainWindow, orient='vertical')
modeSeparator.grid(column=1, row=0, rowspan=len(SSTV_Modes) + 1,  ipady=666)

loadFileButton = tk.Button(mainWindow, text="Load Image", command=AskForImageFile)
loadFileButton.grid(column=2, row=0, sticky=tk.W, padx = 5)

# for each in range(10):
#     label1 = tk.Label(mainWindow, text=f"x_{each}")
#     label2 = tk.Label(mainWindow, text=f"x_{each}")
#     label3 = tk.Label(mainWindow, text=f"x_{each}")
#     label1.grid(column=each, row=0)
#     label2.grid(column=each, row=1)
#     label3.grid(column=each, row=2)

mainWindow.mainloop()