import wx
from functools import reduce

class DrawingFrame(wx.Frame):

  class _Line:
    def __init__(self, coords, karg_dict):
      assert len(coords) % 2 == 0 and len(coords) > 0
      if len(coords) <= 4:
        self.coords = coords
        self.type   = 'point' if len(coords) == 2 else 'line'
      else:
        self.coords = list(zip(*[iter(coords)]*2))
        self.type   = 'spline'
      self.color = karg_dict.get('fill', 'black')
      self.width = karg_dict.get('width', 1)

  def __init__(self, parent, drawing, title='Drawing', size=(800,800)):
    super().__init__(parent, title=title, size=size)
    self._drawing = drawing
    self._image   = wx.Image(*size)
    self._image.SetMask()
    if not self._image.HasAlpha():
      print('No Alpha present') #DEBUG
      self._image.InitAlpha()
      print('Alpha initialized') #DEBUG
    self._dc      = wx.MemoryDC(wx.Bitmap(self._image))
    self._reset()
    
    self.Bind(wx.EVT_PAINT, self.on_paint)
    self.Bind(wx.EVT_LEFT_DOWN, self.on_click)

    self.Centre()
    self.Show()
    print('Init done') #DEBUG

  def _reset(self):
    self._dc.Clear()
    self._dc.SetBackground(wx.Brush(self._drawing.background_color()))

  def on_click(self, event):
    print('Click') #DEBUG
    self._reset()
    self._drawing.draw(self)
    self.Refresh(False)

  def on_paint(self, event):
    print('Paint') #DEBUG
    dc = wx.PaintDC(self)
    dc.Blit(0,0,self._image.Width,self._image.Height,self._dc,0,0)

  ### tkinter Canvas compatibility:
  def create_line(self, *coords, **kargs):
    line = DrawingFrame._Line(coords, kargs) # handles conversions
    self._dc.SetPen(wx.Pen(line.color,width=line.width))
    # select method and call with coords
    if line.type == 'point':
      self._dc.DrawPoint(*line.coords)
    elif line.type == 'line':
      self._dc.DrawLine(*line.coords)
    else: # line.type == 'spline'
      self._dc.DrawSpline(line.coords) # don't unroll arguments
    self.Refresh(False)

  def winfo_width(self):
    return self.ClientSize[0]

  def winfo_height(self):
    return self.ClientSize[1]
