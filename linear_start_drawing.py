from drawing import Drawing
from random import randint
from functools import reduce

class LinearStartDrawing(Drawing):
  """Drawing that with starting points that are near a straight line."""
  def __init__(self, **kargs):
    super().__init__(**kargs)
    self._settings.update({
      'start_variation' : 20
    })
    self.apply_settings(**kargs)

  def gen_coords(self):
    x1,y1,x2,y2 = self._gen_endpoints()
    gen = ( lambda v1, v2, i:
      randint(-self._start_variation,self._start_variation) + 
      (((v1 * (self._points - i - 1)) + (v2 * i)) / (self._points - 1)) )
    return [[gen(x1,x2,i),gen(y1,y2,i)] for i in range(self._points)]

  def _gen_endpoints(self):
    return randint(0,self._width),randint(0,self._height),randint(0,self._width),randint(0,self._height)