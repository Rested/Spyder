
title = 'Spyt Downloader'


import sys
#sys.path[:0] = ['../../..']
import time
import Tkinter
from Tkinter import *
import Pmw
import tkFileDialog
import logging
import time
import gettext


class Demo:
    def __init__(self, parent):
        # Create the Balloon.
        global dll
        dll = []
        global downloading
        downloading=0
        self.balloon = Pmw.Balloon(parent)
        self.mainPart = Tkinter.Label(parent,
	text = 'Choose where to put the files:',
	background = 'black',
	foreground = 'white',
	padx = 0,
	pady = 0)
        self.mainPart.pack(fill='x',expand=1)
        self.messageBar = Pmw.MessageBar(parent,
                        entry_width = 40,
                        entry_relief='groove',
                        labelpos = 'w',
                        label_text = 'Mp3 Path:')
        self.messageBar2 = Pmw.MessageBar(parent,
                        entry_width = 40,
                        entry_relief='groove',
                        labelpos = 'w',
                        label_text = 'Flv Path:')
        self.messageBar.pack(fill = 'x', padx = 10, pady = 10)
        self.messageBar2.pack(fill = 'x', padx = 10, pady = 10)
        #make it so that if path file exists, set to them.
        self.messageBar.message('state', '/')
        self.messageBar2.message('state', '/')
        self.fbbb = Pmw.ButtonBox(parent,)
        self.fbbb.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
        self.fbbb.add('Change .mp3 path', command = self.mp3dir)
        self.fbbb.add('Change .flv path', command = self.flvdir)
        self.mainPart2 = Tkinter.Label(parent,
		text = 'Add items to download:',
		background = 'black',
		foreground = 'white',
		padx = 0,
		pady = 10)
        self.mainPart2.pack(fill='x',expand=1)
        self.entryst = Pmw.EntryField(label_text = 'Search Term:',labelpos = 'w', modifiedcommand= self.sts)
        self.entryst.pack(fill = 'x', padx = 10, pady = 0)
        self.entryt = Pmw.EntryField(label_text = '             Title:',labelpos = 'w', modifiedcommand= self.ts)
        self.entryt.pack(fill = 'x', padx = 10, pady = 0)
        self.entryar = Pmw.EntryField(label_text = '           Artist:',labelpos = 'w', modifiedcommand= self.ars)
        self.entryar.pack(fill = 'x', padx = 10, pady = 0)
        self.entryal = Pmw.EntryField(label_text = '         Album:',labelpos = 'w', modifiedcommand= self.als)
        self.entryal.pack(fill = 'x', padx = 10, pady = 0)
        self.bb = Pmw.ButtonBox(parent,)
        self.bb.pack(fill = 'both', expand = 1, padx = 10, pady = 0)
        self.bb.add('Add to Download list', command = self.addtodllist)
        self.mainPart = Tkinter.Label(parent,
		text = 'Enter Spotify URLs:',
		background = 'black',
		foreground = 'white',
		padx = 0,
		pady = 0)
        self.mainPart.pack(fill='x',expand=1)
        self.entrysp = Pmw.EntryField(
        label_text = 'Enter Spotify URLs:',
        labelpos = 'w', modifiedcommand= self.setvalspourls
        )
        self.entrysp.pack(fill = 'x', padx = 10, pady = 10)
        self.mainPart = Tkinter.Label(parent,
		text = 'Controls:',
		background = 'black',
		foreground = 'white',
		padx = 0,
		pady = 0)
        self.mainPart.pack(fill='x',expand=1)
        self.buttonBox = Pmw.ButtonBox(parent,
                labelpos = 'w',
                frame_borderwidth = 2,
                frame_relief = 'groove')
        self.buttonBox.pack(fill = 'none', expand = 1, padx = 10, pady = 10)
        self.buttonBox.add('Stop')#, command = self.add)
        self.buttonBox.add('Download', command = self.download)#, command = menuBar.enableall)
        #blacksquare progressbar
        self.progressbarbs = Pmw.MessageBar(parent, 
                        entry_width = 41,
                        entry_relief='groove',
                        labelpos = 'w',
                        label_text = ' Progress:')
        self.progressbarbs.pack(fill = 'none', padx = 2.5, pady = 0)
        bs = u"\u25A0" #black square for progressbarbs
        #30bs = 100%
        #this bar displays time left
        self.progressbart = Pmw.MessageBar(parent,
                        entry_width = 41,
                        entry_relief='groove',
                        labelpos = 'w',
                        label_text = 'Time Left:')
        self.progressbart.pack(fill = 'none', padx = 2.5, pady = 0)
        #current action message box
        self.progressbarca = Pmw.MessageBar(parent,
                        entry_width = 41,
                        entry_relief='groove',
                        labelpos = 'w',
                        label_text = '    Action:')
        self.progressbarca.pack(fill = 'none', padx = 2.5, pady = 0)
        #shows errors
        self.progressbare = Pmw.MessageBar(parent,
                        entry_width = 41,
                        entry_relief='groove',
                        labelpos = 'w',
                        label_text = '     Errors:')
        self.progressbare.pack(fill = 'none', padx = 2.5, pady = 0)

        self.progressbarbs.message('state', '')
    def addtodllist(self):
        dll.append(sterm)
        dll.append(title)
        dll.append(artist)
        dll.append(album)
        self.entryst.clear()
        self.entryt.clear()
        self.entryar.clear()
        self.entryal.clear()
    def mp3dir(self):
        dirnamemp3 = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
        if dirnamemp3 != '':
            self.messageBar.message('state', dirnamemp3)
        #also write dirnamemp3 to file. Same for dir name flv
    def flvdir(self):
        dirnameflv = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
        if dirnamemp3 != '':
            self.messageBar2.message('state', dirnameflv)
    def sts(self):
        if downloading == 0:
            global sterm
            sterm = self.entryst.getvalue()
    def ts(self):
        if downloading == 0:
            global title
            title = self.entryt.getvalue()
    def ars(self):
        if downloading == 0:
            global artist
            artist = self.entryar.getvalue()
    def als(self):
        if downloading == 0:
            global album
            album = self.entryal.getvalue()
    def setvalspourls(self):
        if downloading == 0:
            global spourls
            spourls = self.entrysp.getvalue()
    def stop(self):
        downloading = 0
        #do stuff to actually stop downloading
    def download(self):
        downloading = 1
        #dll[0] is search term1, 1 = title1, 2 = artist1, 3 = album1,
        # 4 = search term 2, 5 = title2, etc.
        print dll
        print spourls    

######################################################################


if __name__ == '__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title(title)

    exitButton = Tkinter.Button(root, text = 'Exit', command =root.destroy)
    exitButton.pack(side = 'bottom', pady = 5)
    widget = Demo(root)
    root.mainloop()


