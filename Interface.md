Interface
=========

Methods
-------

The following methods are used for all drawings. To modify behavior, override these as appropriate.

 * `__init__()` - Apply settings. For proper overriding, call `super().__init__()`, then make changes to `self._settings`, then call `self.apply_settings()` to apply those changes.
 * `gen_coords()` - Generate a list of coordinates which will be the basis of the drawing.
 * `init_draw()` - Called after `gen_coords` but before anything else in `draw`. Use to generate any auxililary values needed.
 * `shift_coords(coords)` - Shift the given list of coordinates to form the next list.
 * `iterate_draw()` - Called once per line drawn, after `shift_coords`. Use to update auxiliary values, if necessary.
 * `end_draw()` - Called after all lines have been drawn. Use to clean up auxiliary values, for example.
 * `change_setting(key, value)` - **Warning:** Overriding this method can be done, if changing one setting must change others. However, a call to super().change_setting(...) should be included, to maintain consistent behavior.
 * `draw(display)` - **Warning:** This is the basic drawing method. Override this method only for radically different drawing styles, or include super().draw(...) as appropriate.

Settings
--------

The following details how each of the included classes uses the settings given. Derived classes should, as much as possible, try to retain the original function for each setting.

__Drawing__

 * `background` - The color of the background, as a hex code or common name.
 * `lines` - The number of lines produced when draw() is called.
 * `weight` - The width of each line in pixels.
 * `color` - The color of the line, as a hex code or common name.
 * `points` - The number of points used for each line.
 * `variation` - The maximum distance any given point can travel between subsequent lines.
 * `bounded` - Whether all points must remain within the canvas.

__Fade Drawing__

 * Everything in __Drawing__, except `color` (see below)
 * `start_rgba` - The red, green, blue, and alpha values (0-255) of the first line drawn. Overrides `color` setting.
 * `end_rgba` - Same format as `start__rgba`, but defines the color of the last line drawn.
 * `start_rgba_variation` - The maximum allowable random variation in the start red, green, blue, and alpha values.
 * `end_rgba_variation` - The maximum allowable random variation in the end red, green, blue, and alpha values.
 * `use_alpha` - Whether to include the alpha channel.

__Multiplier Drawing__

 * Everything in __Drawing__
 * `strokes` - The number of times the drawing is repeated.

__Linear Start Drawing__

 * Everything in __Drawing__
 * `start_variation` - The amount by which the first points can vary from the starting line.

__Sized Start Drawing__

 * Everything in __Linear Start Drawing__
 * `start_length` - The minimum length of the starting line.