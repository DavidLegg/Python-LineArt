from random import uniform
from linear_shift_drawing import LinearShiftDrawing

class LinearTaperDrawing(LinearShiftDrawing):
  """Shifts control points linearly"""

  def init_draw(self):
    super().init_draw()
    scale = lambda v, i: (min(i, self._points - i - 1) * 2 / self._points) * v
    self._offsets = [[scale(x,i),scale(y,i)] for i,(x,y) in enumerate(self._offsets)]