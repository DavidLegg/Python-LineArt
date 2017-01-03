from random import uniform
from drawing import Drawing
from itertools import starmap

class LinearShiftDrawing(Drawing):
  """Shifts control points linearly"""

  def init_draw(self):
    super().init_draw()
    self._offsets = list(starmap(self._gen_offset,self._coords))

  def _gen_offset(self, x, y):
    if self._bounded:
      rand = lambda v, dim: uniform(- min(v/self._lines, self._variation),
                                    min((dim - v)/self._lines, self._variation))
    else:
      rand = lambda v, dim: uniform(-self._variation, self._variation)
    return [rand(x, self._width), rand(y, self._height)]


  def shift_coords(self, coords):
    return [[x + x_off, y + y_off] for (x,y),(x_off,y_off) in zip(coords, self._offsets)]

  def end_draw(self):
    super().end_draw()
    del self._offsets