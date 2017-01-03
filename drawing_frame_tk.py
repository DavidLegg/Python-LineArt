import tkinter
import os
from random import randint
from tkinter.filedialog import asksaveasfilename as ask_filename
from PIL import Image
from subprocess import call

class DrawingFrame(tkinter.Canvas):
  def __init__(self, parent, drawing, **kargs):
    super().__init__(parent,width=kargs.get('width',810),height=kargs.get('height',540),bg=drawing.background_color())
    self._drawing = drawing
    self.bind('<Button-1>', self.redraw)
    self.bind('<Button-3>', self.save)
    self.pack()

  def redraw(self, event=None):
    self.delete(tkinter.ALL)
    # rectangle as background for saving the image later.
    self.create_rectangle(0,0,self.winfo_width(),self.winfo_height(),fill=self._drawing.background_color())
    self._drawing.draw(self)

  def save(self, event=None, name=None):
    filename  = ask_filename(filetypes=[('PNG Files','*.png')],initialdir='./Images/') if not name else name
    if filename == '':
      return
    tempfile  = filename.split('.')[0] + '.eps'
    tempfile2 = tempfile[:-4] + '_TEMP.png'
    filename  = tempfile[:-4] + '.png'
    self.postscript(file=tempfile,colormode='color')
    call(["gs","-dSAFER","-sDEVICE=png16m","-r600","-o",tempfile2,tempfile])
    with Image.open(tempfile2) as im:
      center_x = im.width  // 2
      center_y = im.height // 2

      def find_border(mn,mx,dir,below):
        while (mn + 1 < mx): # avoids infinite loop if they get 1px away
          mid   = (mn + mx) // 2
          coord = (mid, center_y) if dir == 'x' else (center_x, mid)
          if im.getpixel(coord) == (255,255,255):
            # mid is in the whitespace, need to move more centrally
            if below:
              mn = mid
            else:
              mx = mid
          else:
            # mid is in the image, need to move less centrally
            if below:
              mx = mid
            else:
              mn = mid
        return mx if below else mn # crop closely

      top    = find_border(0,center_y,'y',True)
      bottom = find_border(center_y,im.height,'y',False)
      left   = find_border(0,center_x,'x',True)
      right  = find_border(center_x,im.width,'x',False)

      im = im.crop((left,top,right,bottom))
      im.save(filename)

    os.remove(tempfile)
    os.remove(tempfile2)