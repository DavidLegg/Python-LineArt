from drawing import Drawing
from random import randint

class FadeDrawing(Drawing):
  """Drawing that changes the colors of its lines"""

  def __init__(self, **kargs):
    super().__init__(**kargs)
    self._settings.update({
      'start_rgba' : [255,255,255,255],
      'end_rgba'   : [0,0,0,255],
      'start_rgba_variation' : [0,0,0,0],
      'end_rgba_variation'   : [0,0,0,0],
      'use_alpha' : False
    })
    self.apply_settings(**kargs)

  def init_draw(self):
    super().init_draw()
    self._working_rgba    = self._color_shift(self._start_rgba, self._start_rgba_variation)
    self._rgba_increments = [(end - start) / self._lines for start,end in zip(self._working_rgba,self._color_shift(self._end_rgba,self._end_rgba_variation))]
    self._set_color()

  def _color_shift(self, rgba, color_var):
    return [min(255,max(0,x + randint(-v,v))) for x,v in zip(rgba,color_var)]

  def iterate_draw(self):
    super().iterate_draw()
    self._working_rgba = [x + inc for x,inc in zip(self._working_rgba,self._rgba_increments)]
    self._set_color()

  def _set_color(self):
    self._color = '#' + ''.join('{:02X}'.format(int(x)) for x in self._working_rgba)
    if not self._use_alpha:
      self._color = self._color[:-2]