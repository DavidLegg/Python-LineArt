import tkinter
from random import randint
from functools import reduce
from itertools import starmap

class Drawing:
  """Randomized line drawing"""

  def __init__(self, **kargs):
    self._settings = {
      'background': 'white',
      'lines'    : 10,
      'weight'   : 1,
      'color'    : 'black',
      'points'   : 4,
      'variation': 30,
      'bounded'  : False
    }
    self.apply_settings(**kargs)

  def background_color(self):
    return self._background

  def apply_settings(self,**kargs):
    # Derived classes should call this after changing the settings.
    for key,value in self._settings.items():
      self.__dict__['_' + key] = kargs.get(key, value)

  def change_setting(self, key, value):
    key = '_' + key;
    if key in self._settings.keys():
      self.__dict__[key] = value

  def draw(self, display):
    self._width  = display.winfo_width();
    self._height = display.winfo_height();
    self._coords = self.gen_coords()
    self.init_draw()
    for _ in range(self._lines):
      display.create_line(*reduce(list.__add__,self._coords), smooth=True, fill=self._color, width=self._weight)
      self._coords = self.shift_coords(self._coords)
      self.iterate_draw()
    self.end_draw()
    del self._width,self._height

  def gen_coords(self):
    return [[randint(0,self._width),randint(0,self._height)] for _ in range(self._points)]

  def shift_coords(self, coords):
    return list(starmap(self._shift_coords, coords))

  def _shift_coords(self, x, y):
    shift = lambda v: v + randint(-self._variation, self._variation)
    x = shift(x)
    y = shift(y)
    if self._bounded:
      x = max(0,min(self._width, x))
      y = max(0,min(self._height,y))
    return [x,y]

  def init_draw(self):
    pass

  def iterate_draw(self):
    pass

  def end_draw(self):
    pass