from drawing import Drawing

class MultiplierDrawing(Drawing):
  """Draws multiple times, like making multiple 'brushstrokes'."""
  def __init__(self, **kargs):
    super().__init__(**kargs)
    self._settings.update({
      'strokes' : 3
    })
    self.apply_settings(**kargs)

  def draw(self, display):
    for _ in range(self._strokes):
      super().draw(display)
