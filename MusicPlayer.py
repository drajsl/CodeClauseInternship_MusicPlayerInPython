import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

root=Tk()
root.title('Music player')
root.iconbitmap('Music.ico')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

playlist=Listbox(root,selectmode=SINGLE,bg="wheat1",fg="navy",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\CodeClause\Music Player\Data')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('arial',20),bg="darkgreen",fg="royalblue3",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="darkolivegreen2",fg="royalblue3",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="darkolivegreen4",fg="royalblue3",padx=7,pady=7)
Resumebtn.grid(row=1,column=2)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="maroon",fg="royalblue3",padx=7,pady=7)
stopbtn.grid(row=1,column=3)

mainloop()