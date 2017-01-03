# import wx
# from drawing_frame_wx import DrawingFrame
import tkinter
from drawing_frame_tk import DrawingFrame

from drawing import Drawing
from linear_shift_drawing import LinearShiftDrawing
from linear_taper_drawing import LinearTaperDrawing
from linear_start_drawing import LinearStartDrawing
from sized_start_drawing  import SizedStartDrawing
from fade_drawing import FadeDrawing
from multiplier_drawing import MultiplierDrawing

class ShiftCombo(FadeDrawing,MultiplierDrawing,LinearStartDrawing,LinearShiftDrawing):
  pass

class TaperCombo(FadeDrawing,MultiplierDrawing,LinearStartDrawing,LinearTaperDrawing):
  pass


STANDARDS = {
  'blueshift': (ShiftCombo,{
    'background'          : 'black',
    'start_length'        : 600,
    'start_variation'     : 20,
    'variation'           : 8,
    'lines'               : 70,
    'weight'              : 0.5,
    'points'              : 5,
    'strokes'             : 5,
    'start_rgba'          : [0,0,0,255],
    'start_rgba_variation': [0,0,0,0],
    'end_rgba'            : [50,150,200,255],
    'end_rgba_variation'  : [20,50,50,0],
    'bounded'             : True
  }),
  'redshift' : (ShiftCombo,{
    'background'          : 'black',
    'start_length'        : 600,
    'start_variation'     : 20,
    'variation'           : 8,
    'lines'               : 70,
    'weight'              : 0.5,
    'points'              : 5,
    'strokes'             : 5,
    'start_rgba'          : [0,0,0,255],
    'start_rgba_variation': [0,0,0,0],
    'end_rgba'            : [200,50,50,255],
    'end_rgba_variation'  : [50,30,20,0],
    'bounded'             : True
  }),
  'bluetaper': (TaperCombo,{
    'background'          : 'black',
    'start_length'        : 600,
    'start_variation'     : 20,
    'variation'           : 15,
    'lines'               : 70,
    'weight'              : 0.5,
    'points'              : 5,
    'strokes'             : 5,
    'start_rgba'          : [0,0,0,255],
    'start_rgba_variation': [0,0,0,0],
    'end_rgba'            : [50,150,200,255],
    'end_rgba_variation'  : [20,50,50,0],
    'bounded'             : True
  }),
  'redtaper' : (TaperCombo,{
    'background'          : 'black',
    'start_length'        : 600,
    'start_variation'     : 20,
    'variation'           : 15,
    'lines'               : 70,
    'weight'              : 0.5,
    'points'              : 5,
    'strokes'             : 5,
    'start_rgba'          : [0,0,0,255],
    'start_rgba_variation': [0,0,0,0],
    'end_rgba'            : [200,50,50,255],
    'end_rgba_variation'  : [50,30,20,0],
    'bounded'             : True
  })
}


def invoke(drawing_class, **kargs):
  tk = tkinter.Tk()
  DrawingFrame(tk,drawing_class(**kargs),**kargs)
  tk.mainloop()

def quick(standard_type, **kargs):
  if standard_type not in STANDARDS:
    print('Unknown type.')
    return
  drawing,settings = STANDARDS.get(standard_type.lower(),(None,None))
  settings.update(kargs)
  invoke(drawing,**settings)

def autosave(standard_type, num=10, folder='Images/AutoBackgrounds/', name_pattern='image_{i}.png', **kargs):
  if standard_type not in STANDARDS:
    print('Unknown type.')
    return
  if folder[-1] != '/':
    folder += '/'
  drawing,settings = STANDARDS.get(standard_type.lower(),(None,None))
  settings.update(kargs)
  tk = tkinter.Tk()
  df = DrawingFrame(tk, drawing(**settings), **settings)

  def _save(i):
    if i > num:
      tk.destroy() # TODO: check this
      return
    df.redraw()
    df.save(name = folder + name_pattern.format(i=i))
    tk.after(200, _save, i + 1)

  tk.after(1000, _save, 1)
