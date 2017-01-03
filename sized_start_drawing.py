from linear_start_drawing import LinearStartDrawing

from random import randint,choice
from math import sqrt,ceil
from itertools import chain

class SizedStartDrawing(LinearStartDrawing):
  """A LinearStartDrawing with a minimum length for the starting line."""
  def __init__(self, **kargs):
    super().__init__(**kargs)
    self._settings.update({
      'start_length' : 400
    })
    self.apply_settings(**kargs)

  def _gen_endpoints(self):
    # Brute force and ignorance:
    # This runs much faster than figuring out which points are actually acceptable,
    # and then choosing from those.
    while True:
      x1,y1,x2,y2 = super()._gen_endpoints()
      if ((x1 - x2)**2) + ((y1 - y2)**2) >= self._start_length**2:
        return x1,y1,x2,y2