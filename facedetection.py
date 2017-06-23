from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

filename = None

# Callback function for "Detect faces" button
def detect_faces():
    img = cv2.imread(filename, 1)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=float(e1_value.get()), minNeighbors=int(e2_value.get()))
    for x,y,w, h in faces:
        img=cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0))
        
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img2)
        
    facedetected = ImageTk.PhotoImage(im_pil)
    label.image = facedetected
    label.configure(image=facedetected)

# Callback function for "Open file" menu bar item
def openimage():
    global filename
    filename = filedialog.askopenfilename(parent=window)
    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    label.image = photo
    label.configure(image=photo)
    e1_value.set("1.05")
    e2_value.set("5")
    
# GRAPHICAL USER INTERFACE
window = Tk()
window.wm_title("Face detection")
window.geometry("800x800")
# Create menu
menubar = Menu(window)
# Create file menu item
openmenu = Menu(menubar, tearoff=0)
openmenu.add_command(label="Open image", command=openimage)
# Create File menu
menubar.add_cascade(label="File", menu=openmenu)
# set Window menubar
window.config(menu=menubar)

# Row 0: Scale factor
label1 = Label(text="Scale factor:")
label1.grid(row=0,column=0, sticky=E)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1, sticky=W)

# Row 1: Min neighbors
label2 = Label(text="Minimum neighbors:")
label2.grid(row=1,column=0, sticky=E)

e2_value=StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=1,column=1, sticky=W)

# Row 2: Button
button = Button(window,text="Detect faces", command=detect_faces)
button.grid(row=2, column=0, columnspan=2, sticky="", pady=5)

# Row 3: Label with image
label = Label(width=800,height=600)
label.image = None # keep a reference!
label.configure(image= None)
label.grid(row=3,column=0, columnspan=2, stick="", pady=5)

window.mainloop()