# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog


def browseFile():
    filename = filedialog.askopenfilename(initialdir = "/", 
                               title = "Select a File", 
                               filetypes = (("PNG", "*.png"),
                                            ("JPG", "*.jpg"),
                                            ("JPEG", "*.jpeg")))
    # upload file into live folder
    
    runModel2()


def runModel1():
    
    import cv2
    import tensorflow as tf
    import numpy as np
    from tensorflow.keras.models import load_model
    falltracker = load_model('falltracker.h5', compile=False)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized = tf.image.resize(rgb, (120,120))
        
        yhat = falltracker.predict(np.expand_dims(resized/255,0))
        sample_coords = yhat[1][0]
        print(yhat[0][0])
        if yhat[0][0] < 1 and yhat[0][0] > 0.5:
            # Controls the main rectangle
            cv2.rectangle(frame, 
                          tuple(np.multiply(sample_coords[:2], [450,450]).astype(int)),
                          tuple(np.multiply(sample_coords[2:], [450,450]).astype(int)), 
                                (0,255,0), 2)   
            # Controls the label rectangle
            cv2.rectangle(frame, 
                          tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int), 
                                        [0,-30])),
                          tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                        [100,0])), 
                                (0,255, 0), -1)
            
            # Controls the text rendered
            cv2.putText(frame, 'noFall', tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                                   [0,-5])),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        if yhat[0][0] == 1:
            # Controls the main rectangle
            cv2.rectangle(frame, 
                          tuple(np.multiply(sample_coords[:2], [450,450]).astype(int)),
                          tuple(np.multiply(sample_coords[2:], [450,450]).astype(int)), 
                                (0,0,255), 2)
            # Controls the label rectangle
            cv2.rectangle(frame, 
                          tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int), 
                                        [0,-30])),
                          tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                        [80,0])), 
                                (0,0,255), -1)
            
            # Controls the text rendered
            cv2.putText(frame, 'fall', tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                                   [0,-5])),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
        cv2.imshow('Fall Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    print(0)



def window2():
    
    win2 = Toplevel(window)
    win2.title("Model 2")
    win2.geometry("320x480")
    win2.resizable(0, 0)
    win2.config(background="#C4C5DA")
    
    frame2 = Frame(win2, bg='#C4C5DA')
    
    select = Button(frame2, text='Choose an image',
                            fg='#C4C5DA', bg='#032A49', bd=0,
                            activeforeground='#C4C5DA',
                            activebackground='#616E9A',
                            font=("Courrier", 16),
                            command=browseFile)
    select.pack(pady=20, fill=X)

    stop2 = Button(frame2, text='Exit',
                         fg='#616E9A', bg='#C4C5DA', bd=0,
                         activeforeground='#CB9821',
                         activebackground='#C4C5DA',
                         font=("Courrier", 16),
                         command=window.destroy)
    stop2.pack(pady=20, fill=X)
    
    model2Sol = Label(frame2, text='Fall / No fall',
                              fg='#032A49', bg='#C4C5DA',
                              font=("Courrier", 20),
                              width=16)
    
    frame2.pack(expand=YES)
    

# menu window config

window = Tk()

window.title("Menu")
window.geometry("320x480")
window.resizable(0, 0)
window.config(background="#C4C5DA")


# main frame

frame = Frame(window, bg='#C4C5DA')


# title label

wTitle = Label(frame, text='Choose the model', 
                       fg='#032A49', bg='#C4C5DA',
                       font=("Courrier", 20),
                       width=16)
wTitle.pack(pady=30)


# model 1 button

model1 = Button(frame, text='Run model 1',
                        fg='#C4C5DA', bg='#032A49', bd=0,
                        activeforeground='#C4C5DA',
                        activebackground='#616E9A',
                        font=("Courrier", 16),
                        command=runModel1)
model1.pack(pady=20, fill=X)

"""
# model 2 button

model2 = Button(frame, text='Run model 2',
                        fg='#C4C5DA', bg='#032A49', bd=0,
                        activeforeground='#C4C5DA',
                        activebackground='#616E9A',
                        font=("Courrier", 16),
                        command=window2)
model2.pack(pady=20, fill=X)
"""

# exit button

stop = Button(frame, text='Exit',
                        fg='#616E9A', bg='#C4C5DA', bd=0,
                        activeforeground='#CB9821',
                        activebackground='#C4C5DA',
                        font=("Courrier", 16),
                        command=window.destroy)
stop.pack(pady=20, fill=X)


# display

frame.pack(expand=YES)

window.mainloop()